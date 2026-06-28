#!/usr/bin/env bash
#
#  install-buff-term.sh
#  ─────────────────────────────────────────────────────────────────
#  Fonctionnalités du shell buff  +  look du terminal buff
#
#  - NE TOUCHE PAS aux dépôts : aucun dépôt externe ajouté sur Ubuntu
#    (on évite le « frankendebian » qui brise le système).
#  - Reproduit les commodités buff (alias, historique, complétion,
#    couleurs, command-not-found, helpers réseau).
#  - Applique le prompt buff :  ┌──[user@host]──[ip]──[heure]──[~]
#                                 └──→ $
#  - Installe la config dans un fichier séparé, sourcé depuis ~/.bashrc
#    -> non destructif, idempotent, réversible.
#
#  Usage :
#     bash install-buff-term.sh              # config seule
#     bash install-buff-term.sh --with-tools # + boîte à outils CLI
#     bash install-buff-term.sh --uninstall  # retire la config
# ─────────────────────────────────────────────────────────────────

set -euo pipefail

# ── Couleurs pour les messages de l'installateur ─────────────────
c_ok='\e[01;32m'; c_warn='\e[01;33m'; c_err='\e[01;31m'; c_info='\e[01;36m'; c_off='\e[0m'
say()  { printf "${c_info}[ * ]${c_off} %s\n" "$1"; }
ok()   { printf "${c_ok}[ + ]${c_off} %s\n" "$1"; }
warn() { printf "${c_warn}[ ! ]${c_off} %s\n" "$1"; }
die()  { printf "${c_err}[ x ]${c_off} %s\n" "$1" >&2; exit 1; }

# ── Chemins ──────────────────────────────────────────────────────
CONF_DIR="${HOME}/.config/buff"
CONF_FILE="${CONF_DIR}/buff.bashrc"
BASHRC="${HOME}/.bashrc"
MARK_BEGIN="# >>> buff term >>>"
MARK_END="# <<< buff term <<<"

WITH_TOOLS=0
DO_UNINSTALL=0
for arg in "$@"; do
    case "$arg" in
        --with-tools) WITH_TOOLS=1 ;;
        --uninstall)  DO_UNINSTALL=1 ;;
        -h|--help)
            grep -E '^#( |$)' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
        *) die "Option inconnue : $arg" ;;
    esac
done

# ── Désinstallation ──────────────────────────────────────────────
if [ "$DO_UNINSTALL" -eq 1 ]; then
    if grep -qF "$MARK_BEGIN" "$BASHRC" 2>/dev/null; then
        sed -i "/$(printf '%s' "$MARK_BEGIN" | sed 's/[][\.*^$/]/\\&/g')/,/$(printf '%s' "$MARK_END" | sed 's/[][\.*^$/]/\\&/g')/d" "$BASHRC"
        ok "Bloc retiré de ~/.bashrc"
    fi
    rm -rf "$CONF_DIR" && ok "Config supprimée : $CONF_DIR"
    say "Ouvre un nouveau terminal pour revenir au prompt par défaut."
    exit 0
fi

# ── Vérifs de base ───────────────────────────────────────────────
[ -n "${BASH_VERSION:-}" ] || warn "Lance ce script avec bash (pas sh/zsh)."
command -v apt-get >/dev/null 2>&1 || warn "apt introuvable : l'install d'outils (--with-tools) sera ignorée."

# ── Boîte à outils CLI optionnelle (dépôts Ubuntu UNIQUEMENT) ─────
install_tools() {
    command -v apt-get >/dev/null 2>&1 || { warn "Pas d'apt, on saute les outils."; return 0; }
    local pkgs=(
        # Réseau / recon
        nmap net-tools dnsutils whois netcat-openbsd tcpdump traceroute
        curl wget rsync openssh-client
        # Manipulation de données / texte
        jq ripgrep fd-find bat tree unzip p7zip-full xclip
        # Dev / base
        git python3-pip build-essential
        # Confort shell
        bash-completion command-not-found htop
    )
    say "Installation des outils via apt (sudo requis)…"
    sudo apt-get update -qq || warn "apt update a échoué (réseau ?)."
    # On installe paquet par paquet pour ne pas tout faire planter si un seul manque
    local failed=()
    for p in "${pkgs[@]}"; do
        if sudo apt-get install -y -qq "$p" >/dev/null 2>&1; then
            printf '  %b+%b %s\n' "$c_ok" "$c_off" "$p"
        else
            failed+=("$p")
        fi
    done
    if command -v update-command-not-found >/dev/null 2>&1; then
        sudo update-command-not-found 2>/dev/null || true
    fi
    [ ${#failed[@]} -eq 0 ] && ok "Tous les outils sont installés." \
        || warn "Non disponibles dans tes dépôts : ${failed[*]}"
}

# ── Génération du fichier de config (sourcé à chaque shell) ───────
write_config() {
    mkdir -p "$CONF_DIR"
    # Heredoc EN QUOTES ('EOF') : rien n'est interprété à l'écriture,
    # tout le contenu reste littéral dans le fichier généré.
    cat > "$CONF_FILE" <<'EOF'
# ─────────────────────────────────────────────────────────────────
#  buff.bashrc  —  généré par install-buff-term.sh
#  Fonctionnalités shell façon buff + prompt façon buff
# ─────────────────────────────────────────────────────────────────

# Ne rien faire si on n'est pas en mode interactif
case $- in *i*) ;; *) return ;; esac

# ── Historique (réglages) ────────────────────────────
HISTCONTROL=ignoreboth          # pas de doublons ni lignes commençant par espace
HISTSIZE=10000
HISTFILESIZE=20000
HISTTIMEFORMAT='%F %T  '        # horodatage de l'historique
shopt -s histappend             # on append au lieu d'écraser
shopt -s checkwinsize           # met à jour LINES/COLUMNS après chaque commande
shopt -s globstar 2>/dev/null   # ** récursif
shopt -s autocd   2>/dev/null   # taper un dossier = cd dedans
shopt -s cdspell  2>/dev/null   # corrige les petites fautes de cd

# ── Couleurs ls/grep (LS_COLORS via dircolors) ───────────────────
if command -v dircolors >/dev/null 2>&1; then
    if [ -r "$HOME/.dircolors" ]; then
        eval "$(dircolors -b "$HOME/.dircolors")"
    else
        eval "$(dircolors -b)"
    fi
fi

# ── lesspipe : less sur archives, binaires, etc. ─────────────────
[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"

# ── Complétion bash ──────────────────────────────────────────────
if ! shopt -oq posix; then
    if [ -f /usr/share/bash-completion/bash_completion ]; then
        . /usr/share/bash-completion/bash_completion
    elif [ -f /etc/bash_completion ]; then
        . /etc/bash_completion
    fi
fi

# ── Alias (équivalents buff) ─────────────────────────────────────
alias ls='ls --color=auto'
alias ll='ls -alFh --color=auto'
alias la='ls -Ah --color=auto'
alias l='ls -CF --color=auto'
alias grep='grep --color=auto'
alias egrep='grep -E --color=auto'
alias fgrep='grep -F --color=auto'
alias diff='diff --color=auto'
alias ip='ip --color=auto'
alias ..='cd ..'
alias ...='cd ../..'
alias mkdir='mkdir -pv'
alias ports='ss -tulanp'                       # ports en écoute
alias myip='curl -s https://ifconfig.me; echo' # IP publique
alias path='echo -e ${PATH//:/\\n}'            # PATH lisible

# bat/fd s'appellent batcat/fdfind sur Debian/Ubuntu
command -v batcat >/dev/null 2>&1 && alias bat='batcat' && alias cat='batcat --paging=never'
command -v fdfind >/dev/null 2>&1 && alias fd='fdfind'

# ── Helper : IP locale/VPN pour le prompt (style buff) ───
# Priorité au tunnel VPN (tun*/wg*), sinon IP source de la route par défaut.
__buff_ip() {
    local ip=""
    for ifc in tun0 tun1 wg0; do
        ip="$(ip -4 -o addr show "$ifc" 2>/dev/null | awk '{print $4}' | cut -d/ -f1 | head -n1)"
        [ -n "$ip" ] && { printf '%s' "$ip"; return; }
    done
    ip="$(ip route get 1.1.1.1 2>/dev/null | awk '{for(i=1;i<=NF;i++) if($i=="src"){print $(i+1); exit}}')"
    printf '%s' "${ip:---}"
}

# ── Prompt buff ──────────────────────────────────────────────────
#   ┌──[✗]──[user@host]──[ip]──[heure]──[~]
#   └──→ $   (rouge #FF3131 · heure #ddff24 · host bleu · $ vert)
# Le segment [✗] n'apparaît que si la dernière commande a échoué.
__buff_prompt() {
    local x=$?
    # Couleurs (entre \[ \] pour un calcul de largeur correct)
    local Rd='\[\e[38;2;255;49;49m\]'    # rouge boîte       #FF3131
    local RdB='\[\e[1;38;2;255;49;49m\]' # rouge gras (root) #FF3131
    local Bf='\[\e[38;2;221;255;36m\]'   # buff (heure)      #ddff24
    local Gy='\[\e[0;37m\]'     # gris
    local Ye='\[\e[0;33m\]'     # jaune/olive (@)
    local Bl='\[\e[01;34m\]'    # bleu    (hostname)
    local Gn='\[\e[1;32m\]'     # vert vif (chemin et $)
    local Wh='\[\e[1;97m\]'     # blanc gras (user et ip)
    local Z='\[\e[0m\]'         # reset

    # Segment d'erreur (✗) seulement si code de sortie != 0
    local errseg=""
    [ "$x" -ne 0 ] && errseg="[${Rd}✗${Gy}]${Rd}──"

    # Bloc user@host (rouge si root)
    local userhost
    if [ "${EUID:-$(id -u)}" -eq 0 ]; then
        userhost="${RdB}root${Ye}@${Bl}\h"
    else
        userhost="${Wh}\u${Ye}@${Bl}\h"
    fi

    PS1="${Rd}┌──${errseg}[${userhost}${Rd}]──[${Wh}$(__buff_ip)${Rd}]──[${Bf}\t${Rd}]──[${Gn}\w${Rd}]\n"
    PS1+="${Rd}└──→ ${Gn}\$${Z} "
}
PROMPT_COMMAND="__buff_prompt${PROMPT_COMMAND:+; $PROMPT_COMMAND}"

# Titre de fenêtre xterm : user@host: chemin
case "$TERM" in
    xterm*|rxvt*|*256color)
        PS1="\[\e]0;\u@\h: \w\a\]$PS1" ;;
esac

# ── command-not-found (suggère le paquet quand une commande manque)
if [ -x /usr/lib/command-not-found ] || [ -x /usr/share/command-not-found/command-not-found ]; then
    command_not_found_handle() {
        if [ -x /usr/lib/command-not-found ]; then
            /usr/lib/command-not-found -- "$1"; return $?
        elif [ -x /usr/share/command-not-found/command-not-found ]; then
            /usr/share/command-not-found/command-not-found -- "$1"; return $?
        else
            printf '%s : commande introuvable\n' "$1" >&2; return 127
        fi
    }
fi
EOF
    ok "Config écrite : $CONF_FILE"
}

# ── Branchement dans ~/.bashrc (idempotent + sauvegarde) ─────────
hook_bashrc() {
    [ -f "$BASHRC" ] || touch "$BASHRC"
    if grep -qF "$MARK_BEGIN" "$BASHRC"; then
        ok "~/.bashrc déjà branché (aucune duplication)."
        return
    fi
    local backup="${BASHRC}.bak.$(date +%Y%m%d-%H%M%S)"
    cp -a "$BASHRC" "$backup"
    ok "Sauvegarde de ~/.bashrc -> $backup"
    {
        printf '\n%s\n' "$MARK_BEGIN"
        printf '[ -f "%s" ] && . "%s"\n' "$CONF_FILE" "$CONF_FILE"
        printf '%s\n' "$MARK_END"
    } >> "$BASHRC"
    ok "Ligne de source ajoutée à ~/.bashrc"
}

# ── Migration : retirer l'ancienne version « parrot-kali » ───────
migrate_old() {
    local old_dir="${HOME}/.config/parrot-kali"
    if grep -qF "# >>> parrot-kali term >>>" "$BASHRC" 2>/dev/null; then
        sed -i '/# >>> parrot-kali term >>>/,/# <<< parrot-kali term <<</d' "$BASHRC"
        ok "Ancien bloc 'parrot-kali term' retiré de ~/.bashrc"
    fi
    rm -f "${old_dir}/parrot-kali.bashrc"
    rmdir "$old_dir" 2>/dev/null || true
}

# ── Exécution ────────────────────────────────────────────────────
say "Mise en place du terminal buff…"
migrate_old
write_config
hook_bashrc
[ "$WITH_TOOLS" -eq 1 ] && install_tools || say "Astuce : relance avec --with-tools pour la boîte à outils CLI."

echo
ok "Terminé."
say "Active maintenant :  source ~/.bashrc   (ou ouvre un nouveau terminal)"
say "Pour tout retirer  :  bash $0 --uninstall"
