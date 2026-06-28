#!/usr/bin/env bash
#
#  install-buff-extras.sh
#  ─────────────────────────────────────────────────────────────────
#  Complément à install-buff-term.sh :
#
#   - ble.sh : auto-suggestions (texte fantôme) + coloration syntaxique
#              + menu de complétion amélioré  -> le « feeling » zsh,
#              mais en bash.
#   - fzf    : Ctrl-R (historique flou), Ctrl-T (fichiers), Alt-C (cd flou).
#   - ~/.inputrc réglé : complétion insensible à la casse, colorée, etc.
#   - JetBrainsMono Nerd Font installée + appliquée à Konsole.
#   - Fond Konsole forcé en noir absolu #000000 (palette préservée).
#
#  Idempotent, non destructif (sauvegardes), réversible (--uninstall).
#
#  Usage :
#     bash install-buff-extras.sh                # tout
#     bash install-buff-extras.sh --no-font      # sans la police
#     bash install-buff-extras.sh --size 13      # taille police Konsole
#     bash install-buff-extras.sh --uninstall    # retire les greffons
# ─────────────────────────────────────────────────────────────────

set -euo pipefail

c_ok='\e[01;32m'; c_warn='\e[01;33m'; c_err='\e[01;31m'; c_info='\e[01;36m'; c_off='\e[0m'
say()  { printf "${c_info}[ * ]${c_off} %s\n" "$1"; }
ok()   { printf "${c_ok}[ + ]${c_off} %s\n" "$1"; }
warn() { printf "${c_warn}[ ! ]${c_off} %s\n" "$1"; }
die()  { printf "${c_err}[ x ]${c_off} %s\n" "$1" >&2; exit 1; }

# ── Chemins / constantes ─────────────────────────────────────────
BASHRC="${HOME}/.bashrc"
CONF_DIR="${HOME}/.config/buff"
EXTRAS_FILE="${CONF_DIR}/extras.bashrc"
BLE_SRC="${HOME}/.local/src/ble.sh"
BLE_SH="${HOME}/.local/share/blesh/ble.sh"
INPUTRC="${HOME}/.inputrc"

FONT_NAME="JetBrainsMono Nerd Font Mono"
FONT_DIR="${HOME}/.local/share/fonts/JetBrainsMonoNerdFont"
FONT_URL="https://github.com/ryanoasis/nerd-fonts/releases/latest/download/JetBrainsMono.zip"
FONT_SIZE=12

# Marqueurs (chacun son bloc dans ~/.bashrc)
B_INIT_OPEN="# >>> buff ble init >>>"
B_INIT_CLOSE="# <<< buff ble init <<<"
B_XTRA_OPEN="# >>> buff extras >>>"
B_XTRA_CLOSE="# <<< buff extras <<<"
B_ATCH_OPEN="# >>> buff ble attach >>>"
B_ATCH_CLOSE="# <<< buff ble attach <<<"

WITH_FONT=1
DO_UNINSTALL=0
while [ $# -gt 0 ]; do
    case "$1" in
        --no-font)   WITH_FONT=0 ;;
        --size)      shift; FONT_SIZE="${1:?taille manquante}" ;;
        --uninstall) DO_UNINSTALL=1 ;;
        -h|--help)   grep -E '^#( |$)' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
        *) die "Option inconnue : $1" ;;
    esac
    shift
done

# Supprime un bloc balisé d'un fichier (échappe les méta-caractères)
strip_block() {  # $1=fichier $2=open $3=close
    local f="$1" o="$2" c="$3"
    grep -qF "$o" "$f" 2>/dev/null || return 0
    local eo ec
    eo="$(printf '%s' "$o" | sed 's/[][\.*^$/]/\\&/g')"
    ec="$(printf '%s' "$c" | sed 's/[][\.*^$/]/\\&/g')"
    sed -i "/$eo/,/$ec/d" "$f"
}

# ── Désinstallation ──────────────────────────────────────────────
if [ "$DO_UNINSTALL" -eq 1 ]; then
    if [ -f "$BASHRC" ]; then
        strip_block "$BASHRC" "$B_INIT_OPEN" "$B_INIT_CLOSE"
        strip_block "$BASHRC" "$B_XTRA_OPEN" "$B_XTRA_CLOSE"
        strip_block "$BASHRC" "$B_ATCH_OPEN" "$B_ATCH_CLOSE"
        ok "Blocs ble.sh/extras retirés de ~/.bashrc"
    fi
    rm -f "$EXTRAS_FILE" && ok "extras.bashrc supprimé"
    warn "Conservés (à retirer à la main si voulu) : $BLE_SRC , ~/.local/share/blesh , $FONT_DIR"
    warn "Fond noir : le schéma Konsole 'BuffBlack' reste en place."
    warn "  -> pour revenir en arrière : Konsole > Modifier le profil > Apparence > choisis un autre schéma."
    say "Ouvre un nouveau terminal pour appliquer."
    exit 0
fi

# ── Dépendances (dépôts Ubuntu uniquement) ───────────────────────
ensure_deps() {
    command -v apt-get >/dev/null 2>&1 || { warn "Pas d'apt : installe à la main git make gawk fzf unzip curl."; return 0; }
    local need=() ; local map=( "git:git" "make:make" "gawk:gawk" "fzf:fzf" "unzip:unzip" "curl:curl" )
    for pair in "${map[@]}"; do
        local cmd="${pair%%:*}" pkg="${pair##*:}"
        command -v "$cmd" >/dev/null 2>&1 || need+=("$pkg")
    done
    [ ${#need[@]} -eq 0 ] && { ok "Dépendances déjà présentes."; return 0; }
    say "Installation des dépendances : ${need[*]} (sudo requis)…"
    sudo apt-get update -qq || warn "apt update a échoué."
    sudo apt-get install -y -qq "${need[@]}" || warn "Certaines deps n'ont pas pu s'installer."
}

# ── ble.sh : auto-suggestions + coloration syntaxique ────────────
install_blesh() {
    if [ -f "$BLE_SH" ]; then
        ok "ble.sh déjà présent ($BLE_SH). (mets-le à jour en shell avec : ble-update)"
        return 0
    fi
    command -v git  >/dev/null 2>&1 || die "git requis pour ble.sh."
    command -v make >/dev/null 2>&1 || die "make requis pour ble.sh."
    command -v gawk >/dev/null 2>&1 || warn "gawk recommandé pour ble.sh."
    say "Clonage et compilation de ble.sh…"
    rm -rf "$BLE_SRC"; mkdir -p "$(dirname "$BLE_SRC")"
    git clone --recursive --depth 1 --shallow-submodules \
        https://github.com/akinomyoga/ble.sh.git "$BLE_SRC" \
        || die "Clonage de ble.sh échoué (réseau ?)."
    make -C "$BLE_SRC" install PREFIX="$HOME/.local" >/dev/null \
        || die "Compilation de ble.sh échouée."
    [ -f "$BLE_SH" ] && ok "ble.sh installé." || die "ble.sh introuvable après install."
}

# ── ~/.inputrc (readline) : complétion confortable ───────────────
write_inputrc() {
    if [ -f "$INPUTRC" ] && ! grep -q "buff inputrc" "$INPUTRC"; then
        cp -a "$INPUTRC" "${INPUTRC}.bak.$(date +%Y%m%d-%H%M%S)"
        ok "Sauvegarde de ~/.inputrc"
    fi
    cat > "$INPUTRC" <<'EOF'
# buff inputrc
$include /etc/inputrc

set completion-ignore-case on
set completion-map-case on
set show-all-if-ambiguous on
set show-all-if-unmodified on
set colored-stats on
set colored-completion-prefix on
set menu-complete-display-prefix on
set mark-symlinked-directories on
set visible-stats on
set bell-style none

# Flèches haut/bas = recherche dans l'historique selon ce qui est déjà tapé
"\e[A": history-search-backward
"\e[B": history-search-forward
EOF
    ok "~/.inputrc réglé."
}

# ── extras.bashrc (sourcé entre l'init et l'attach de ble.sh) ────
write_extras() {
    mkdir -p "$CONF_DIR"
    cat > "$EXTRAS_FILE" <<'EOF'
# ─────────────────────────────────────────────────────────────────
#  extras.bashrc  —  ble.sh (options) + fzf
#  Sourcé APRÈS l'init ble.sh et AVANT ble-attach.
# ─────────────────────────────────────────────────────────────────
case $- in *i*) ;; *) return ;; esac

# ── Options ble.sh (uniquement si ble.sh est chargé) ─────────────
if [[ ${BLE_VERSION-} ]]; then
    # Suggestions automatiques depuis l'historique (texte fantôme)
    bleopt complete_auto_complete=1
    bleopt complete_ambiguous=1
    bleopt complete_menu_style=desc
    # Couleur du texte fantôme (gris discret, façon zsh-autosuggestions)
    ble-face -s auto_complete fg=242
    # Accepter la suggestion : Flèche droite ou Fin (défaut ble.sh).
    # Compléter mot par mot : Ctrl-Flèche droite.
    # La coloration syntaxique (commande valide=vert / invalide=rouge)
    # est active par défaut dans ble.sh.
fi

# ── fzf : Ctrl-R historique, Ctrl-T fichiers, Alt-C cd ───────────
if command -v fzf >/dev/null 2>&1; then
    export FZF_DEFAULT_OPTS='--height 40% --layout=reverse --border --info=inline'
    if fzf --bash >/dev/null 2>&1; then           # fzf récent (>= 0.48)
        eval "$(fzf --bash)"
    else                                          # fzf plus ancien
        for f in key-bindings.bash completion.bash; do
            [ -f "/usr/share/doc/fzf/examples/$f" ] && . "/usr/share/doc/fzf/examples/$f"
        done
    fi
fi
EOF
    ok "extras.bashrc écrit."
}

# ── Branchements dans ~/.bashrc (init en haut, attach en bas) ────
hook_bashrc() {
    [ -f "$BASHRC" ] || touch "$BASHRC"

    # 1) Init ble.sh -> tout en HAUT du fichier (requis par ble.sh)
    if ! grep -qF "$B_INIT_OPEN" "$BASHRC"; then
        cp -a "$BASHRC" "${BASHRC}.bak.$(date +%Y%m%d-%H%M%S)"
        local tmp; tmp="$(mktemp)"
        {
            printf '%s\n' "$B_INIT_OPEN"
            printf '[[ $- == *i* ]] && [ -f "%s" ] && source "%s" --noattach\n' "$BLE_SH" "$BLE_SH"
            printf '%s\n\n' "$B_INIT_CLOSE"
            cat "$BASHRC"
        } > "$tmp"
        mv "$tmp" "$BASHRC"
        ok "Init ble.sh ajouté en haut de ~/.bashrc"
    else
        ok "Init ble.sh déjà présent."
    fi

    # 2) Source de extras.bashrc
    if ! grep -qF "$B_XTRA_OPEN" "$BASHRC"; then
        {
            printf '\n%s\n' "$B_XTRA_OPEN"
            printf '[ -f "%s" ] && . "%s"\n' "$EXTRAS_FILE" "$EXTRAS_FILE"
            printf '%s\n' "$B_XTRA_CLOSE"
        } >> "$BASHRC"
        ok "Source extras.bashrc ajoutée."
    else
        ok "Source extras.bashrc déjà présente."
    fi

    # 3) Attach ble.sh -> tout en BAS (doit rester en dernier)
    if ! grep -qF "$B_ATCH_OPEN" "$BASHRC"; then
        {
            printf '\n%s\n' "$B_ATCH_OPEN"
            printf '[[ ! ${BLE_VERSION-} ]] || ble-attach\n'
            printf '%s\n' "$B_ATCH_CLOSE"
        } >> "$BASHRC"
        ok "Attach ble.sh ajouté en bas."
    else
        ok "Attach ble.sh déjà présent."
    fi
}

# ── JetBrainsMono Nerd Font + Konsole ────────────────────────────
install_font() {
    if fc-list 2>/dev/null | grep -qi "JetBrainsMono Nerd Font"; then
        ok "JetBrainsMono Nerd Font déjà installée."
    else
        command -v unzip >/dev/null 2>&1 || die "unzip requis pour la police."
        say "Téléchargement de JetBrainsMono Nerd Font…"
        mkdir -p "$FONT_DIR"
        local tmp; tmp="$(mktemp -d)"
        if command -v curl >/dev/null 2>&1; then
            curl -fL "$FONT_URL" -o "$tmp/jbm.zip" || die "Téléchargement échoué (réseau ?)."
        elif command -v wget >/dev/null 2>&1; then
            wget -qO "$tmp/jbm.zip" "$FONT_URL" || die "Téléchargement échoué (réseau ?)."
        else
            die "curl ou wget requis."
        fi
        unzip -oq "$tmp/jbm.zip" -d "$FONT_DIR" -x '*.txt' '*.md' >/dev/null
        rm -rf "$tmp"
        fc-cache -f "$FONT_DIR" >/dev/null 2>&1 || fc-cache -f >/dev/null 2>&1 || true
        ok "Police installée -> $FONT_DIR"
    fi
    configure_konsole
}

configure_konsole() {
    command -v konsole >/dev/null 2>&1 || { warn "Konsole non détecté : configure la police à la main dans ton terminal."; return 0; }
    local kdir="${HOME}/.local/share/konsole"; mkdir -p "$kdir"
    local kw kr prof=""
    kw="$(command -v kwriteconfig6 || command -v kwriteconfig5 || true)"
    kr="$(command -v kreadconfig6 || command -v kreadconfig5 || true)"
    [ -n "$kr" ] && prof="$($kr --file konsolerc --group "Desktop Entry" --key DefaultProfile 2>/dev/null || true)"

    local fontval="${FONT_NAME},${FONT_SIZE},-1,5,50,0,0,0,0,0"

    local target=""
    if [ -n "$prof" ] && [ -f "$kdir/$prof" ]; then
        # Profil existant -> on touche SEULEMENT la police (tes couleurs buff restent)
        if [ -n "$kw" ]; then
            $kw --file "$kdir/$prof" --group "Appearance" --key "Font" "$fontval"
        else
            cp -a "$kdir/$prof" "$kdir/${prof}.bak.$(date +%s)"
            grep -q '^\[Appearance\]' "$kdir/$prof" || printf '\n[Appearance]\n' >> "$kdir/$prof"
            sed -i '/^\[Appearance\]/,/^\[/{/^Font=/d}' "$kdir/$prof"
            sed -i "/^\[Appearance\]/a Font=$fontval" "$kdir/$prof"
        fi
        target="$prof"
        ok "Police appliquée au profil Konsole existant : $prof"
    else
        cat > "$kdir/Buff.profile" <<PROF
[Appearance]
Font=$fontval

[General]
Name=Buff
Parent=FALLBACK/
PROF
        [ -n "$kw" ] && $kw --file konsolerc --group "Desktop Entry" --key "DefaultProfile" "Buff.profile"
        target="Buff.profile"
        ok "Profil Konsole 'Buff' créé et défini par défaut."
    fi

    force_black_bg "$kdir" "$target"
    warn "Konsole : ouvre une NOUVELLE fenêtre pour voir police + fond noir."
}

# ── Fond noir absolu #000000 (préserve le reste de ta palette) ────
force_black_bg() {
    local kdir="$1" proffile="$2"
    local scheme_name="BuffBlack"
    local scheme_path="$kdir/${scheme_name}.colorscheme"
    local kw kr
    kw="$(command -v kwriteconfig6 || command -v kwriteconfig5 || true)"
    kr="$(command -v kreadconfig6 || command -v kreadconfig5 || true)"

    # Schéma de couleurs actuel du profil (pour conserver ta palette), défaut Breeze
    local cur=""
    [ -n "$kr" ] && [ -f "$kdir/$proffile" ] && \
        cur="$($kr --file "$kdir/$proffile" --group "Appearance" --key "ColorScheme" 2>/dev/null || true)"
    [ -z "$cur" ] && cur="Breeze"

    # Créer BuffBlack en repartant de la palette existante (user dir, puis système)
    if [ ! -f "$scheme_path" ]; then
        local src="" cand
        for cand in "$kdir/${cur}.colorscheme" "/usr/share/konsole/${cur}.colorscheme" "/usr/share/konsole/Breeze.colorscheme"; do
            [ -f "$cand" ] && { src="$cand"; break; }
        done
        if [ -n "$src" ]; then
            cp "$src" "$scheme_path"
        else
            cat > "$scheme_path" <<'CS'
[General]
Description=BuffBlack
Opacity=1

[Foreground]
Color=255,255,255
CS
        fi
    fi

    # Forcer le noir absolu + opacité pleine (le reste de la palette est conservé)
    if [ -n "$kw" ]; then
        $kw --file "$scheme_path" --group "Background"        --key "Color" "0,0,0"
        $kw --file "$scheme_path" --group "BackgroundIntense" --key "Color" "0,0,0"
        $kw --file "$scheme_path" --group "BackgroundFaint"   --key "Color" "0,0,0"
        $kw --file "$scheme_path" --group "General"           --key "Opacity" "1"
        $kw --file "$scheme_path" --group "General"           --key "Description" "BuffBlack"
        $kw --file "$kdir/$proffile" --group "Appearance"     --key "ColorScheme" "$scheme_name"
    else
        # Repli sans kwriteconfig : pas de doublon de section [Background]
        if grep -q '^\[Background\]' "$scheme_path"; then
            sed -i '/^\[Background\]/,/^\[/{s/^Color=.*/Color=0,0,0/}' "$scheme_path"
            grep -qE '^\[Background\]' "$scheme_path" && ! sed -n '/^\[Background\]/,/^\[/p' "$scheme_path" | grep -q '^Color=' \
                && sed -i '/^\[Background\]/a Color=0,0,0' "$scheme_path"
        else
            printf '\n[Background]\nColor=0,0,0\n' >> "$scheme_path"
        fi
        if grep -q '^ColorScheme=' "$kdir/$proffile" 2>/dev/null; then
            sed -i "s/^ColorScheme=.*/ColorScheme=$scheme_name/" "$kdir/$proffile"
        else
            sed -i "/^\[Appearance\]/a ColorScheme=$scheme_name" "$kdir/$proffile"
        fi
    fi
    ok "Fond noir absolu #000000 appliqué (schéma '$scheme_name', palette préservée)."
}

# ── Migration : retirer l'ancienne version « parrot-kali » ───────
migrate_old() {
    local old_dir="${HOME}/.config/parrot-kali"
    if [ -f "$BASHRC" ]; then
        for m in "ble init" "extras" "ble attach"; do
            if grep -qF "# >>> parrot-kali $m >>>" "$BASHRC"; then
                sed -i "/# >>> parrot-kali $m >>>/,/# <<< parrot-kali $m <<</d" "$BASHRC"
            fi
        done
        ok "Anciens blocs 'parrot-kali' nettoyés dans ~/.bashrc (si présents)."
    fi
    rm -f "${old_dir}/extras.bashrc"
    rmdir "$old_dir" 2>/dev/null || true

    # Ancien profil Konsole 'ParrotKali.profile' -> 'Buff.profile'
    local kdir="${HOME}/.local/share/konsole"
    if [ -f "$kdir/ParrotKali.profile" ]; then
        mv -f "$kdir/ParrotKali.profile" "$kdir/Buff.profile"
        sed -i 's/^Name=ParrotKali/Name=Buff/' "$kdir/Buff.profile" 2>/dev/null || true
        local kw; kw="$(command -v kwriteconfig6 || command -v kwriteconfig5 || true)"
        local kr; kr="$(command -v kreadconfig6 || command -v kreadconfig5 || true)"
        local def=""
        [ -n "$kr" ] && def="$($kr --file konsolerc --group "Desktop Entry" --key DefaultProfile 2>/dev/null || true)"
        if [ "$def" = "ParrotKali.profile" ] && [ -n "$kw" ]; then
            $kw --file konsolerc --group "Desktop Entry" --key "DefaultProfile" "Buff.profile"
        fi
        ok "Ancien profil Konsole renommé : ParrotKali -> Buff"
    fi
}

# ── Exécution ────────────────────────────────────────────────────
say "Greffons : ble.sh + fzf + inputrc + Nerd Font"
ensure_deps
migrate_old
install_blesh
write_inputrc
write_extras
hook_bashrc
[ "$WITH_FONT" -eq 1 ] && install_font || say "Police ignorée (--no-font)."

echo
ok "Terminé."
say "Active maintenant :  source ~/.bashrc   (ou ouvre un nouveau terminal)"
say "Essaie : tape le début d'une vieille commande -> suggestion grise -> Flèche droite."
say "Ctrl-R = historique flou (fzf)   |   Ctrl-T = fichiers   |   Alt-C = cd"
say "Konsole : nouvelle fenêtre pour voir la Nerd Font + le fond noir #000000."
say "Pour retirer les greffons :  bash $0 --uninstall"
