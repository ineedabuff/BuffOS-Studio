#!/usr/bin/env bash
#
#  install-buff-zsh.sh
#  ─────────────────────────────────────────────────────────────────
#  zsh « lean » (SANS oh-my-zsh) qui reproduit l'expérience Buff :
#
#   - zsh-autosuggestions  : texte fantôme gris (Flèche droite = accepter)
#   - zsh-syntax-highlighting : coloration au fur et à mesure
#   - compsys              : la VRAIE complétion zsh (git/ssh/systemctl…)
#   - fzf                  : Ctrl-R / Ctrl-T / Alt-C
#   - prompt Buff porté en zsh : ┌─[✗]─[user@host]─[ip]─[~] / └──╼ $
#
#  NE change PAS ton shell par défaut : tu testes en tapant « zsh ».
#  bash reste ton shell de connexion et de scripts.
#  Idempotent, non destructif (sauvegardes), réversible (--uninstall).
#
#  Usage :
#     bash install-buff-zsh.sh                # installe, garde bash par défaut
#     bash install-buff-zsh.sh --set-default  # + chsh vers zsh (déconnexion requise)
#     bash install-buff-zsh.sh --uninstall    # retire la config zsh
# ─────────────────────────────────────────────────────────────────

set -euo pipefail

c_ok='\e[01;32m'; c_warn='\e[01;33m'; c_err='\e[01;31m'; c_info='\e[01;36m'; c_off='\e[0m'
say()  { printf "${c_info}[ * ]${c_off} %s\n" "$1"; }
ok()   { printf "${c_ok}[ + ]${c_off} %s\n" "$1"; }
warn() { printf "${c_warn}[ ! ]${c_off} %s\n" "$1"; }
die()  { printf "${c_err}[ x ]${c_off} %s\n" "$1" >&2; exit 1; }

CONF_DIR="${HOME}/.config/buff"
CONF_FILE="${CONF_DIR}/buff.zsh"
ZSHRC="${HOME}/.zshrc"
MARK_BEGIN="# >>> buff zsh >>>"
MARK_END="# <<< buff zsh <<<"

SET_DEFAULT=0
DO_UNINSTALL=0
for arg in "$@"; do
    case "$arg" in
        --set-default) SET_DEFAULT=1 ;;
        --uninstall)   DO_UNINSTALL=1 ;;
        -h|--help)     grep -E '^#( |$)' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
        *) die "Option inconnue : $arg" ;;
    esac
done

# ── Désinstallation ──────────────────────────────────────────────
if [ "$DO_UNINSTALL" -eq 1 ]; then
    if grep -qF "$MARK_BEGIN" "$ZSHRC" 2>/dev/null; then
        eo="$(printf '%s' "$MARK_BEGIN" | sed 's/[][\.*^$/]/\\&/g')"
        ec="$(printf '%s' "$MARK_END"   | sed 's/[][\.*^$/]/\\&/g')"
        sed -i "/$eo/,/$ec/d" "$ZSHRC"
        ok "Bloc retiré de ~/.zshrc"
    fi
    rm -f "$CONF_FILE" && ok "Config zsh supprimée : $CONF_FILE"
    if [ "$(basename "${SHELL:-}")" = "zsh" ]; then
        warn "Ton shell par défaut est encore zsh. Reviens à bash avec :"
        warn "   chsh -s \"\$(command -v bash)\""
    fi
    exit 0
fi

# ── Dépendances (dépôts Ubuntu uniquement, PAS oh-my-zsh) ────────
ensure_deps() {
    command -v apt-get >/dev/null 2>&1 || { warn "Pas d'apt : installe à la main zsh zsh-autosuggestions zsh-syntax-highlighting fzf."; return 0; }
    local pkgs=(zsh zsh-autosuggestions zsh-syntax-highlighting fzf)
    say "Installation : ${pkgs[*]} (sudo requis)…"
    sudo apt-get update -qq || warn "apt update a échoué."
    local failed=()
    for p in "${pkgs[@]}"; do
        if dpkg -s "$p" >/dev/null 2>&1 || sudo apt-get install -y -qq "$p" >/dev/null 2>&1; then
            printf '  %b+%b %s\n' "$c_ok" "$c_off" "$p"
        else
            failed+=("$p")
        fi
    done
    [ ${#failed[@]} -eq 0 ] && ok "Paquets prêts." || warn "Indisponibles dans tes dépôts : ${failed[*]}"
    command -v zsh >/dev/null 2>&1 || die "zsh n'est pas installé : impossible de continuer."
}

# ── Génération de la config zsh ──────────────────────────────────
write_config() {
    mkdir -p "$CONF_DIR" "${HOME}/.cache"
    cat > "$CONF_FILE" <<'ZEOF'
# ─────────────────────────────────────────────────────────────────
#  buff.zsh  —  shell zsh façon Buff + prompt Buff
#  Généré par install-buff-zsh.sh
# ─────────────────────────────────────────────────────────────────
[[ -o interactive ]] || return

# ── Historique ───────────────────────────────────────────────────
HISTFILE="${HOME}/.zsh_history"
HISTSIZE=10000
SAVEHIST=20000
setopt EXTENDED_HISTORY INC_APPEND_HISTORY SHARE_HISTORY
setopt HIST_IGNORE_DUPS HIST_IGNORE_ALL_DUPS HIST_IGNORE_SPACE
setopt HIST_REDUCE_BLANKS HIST_VERIFY

# ── Comportement ─────────────────────────────────────────────────
setopt AUTO_CD EXTENDED_GLOB NUMERIC_GLOB_SORT INTERACTIVE_COMMENTS NO_NOMATCH
setopt PROMPT_SUBST
bindkey -e

# ── Couleurs ─────────────────────────────────────────────────────
autoload -Uz colors && colors
command -v dircolors >/dev/null 2>&1 && eval "$(dircolors -b)"

# ── Complétion (compsys — l'atout de zsh) ────────────────────────
mkdir -p "${HOME}/.cache/zcompcache" 2>/dev/null
autoload -Uz compinit
compinit -i -d "${HOME}/.cache/zcompdump-${ZSH_VERSION}"
zmodload zsh/complist 2>/dev/null
zstyle ':completion:*' menu select
zstyle ':completion:*' matcher-list 'm:{a-zA-Z}={A-Za-z}' 'r:|=*' 'l:|=* r:|=*'  # insensible casse + flou
zstyle ':completion:*' list-colors "${(s.:.)LS_COLORS}"                          # menu coloré
zstyle ':completion:*' group-name ''
zstyle ':completion:*' rehash true                                              # détecte les nouveaux binaires
zstyle ':completion:*' use-cache on
zstyle ':completion:*' cache-path "${HOME}/.cache/zcompcache"
zstyle ':completion:*:descriptions' format '%F{yellow}── %d ──%f'
zstyle ':completion:*:warnings'     format '%F{red}aucune correspondance%f'
zstyle ':completion:*:default'      list-prompt '%S%M correspondances%s'

# ── Touches : flèches = recherche d'historique par préfixe ───────
autoload -Uz up-line-or-beginning-search down-line-or-beginning-search
zle -N up-line-or-beginning-search
zle -N down-line-or-beginning-search
bindkey '^[[A' up-line-or-beginning-search;   bindkey '^[OA' up-line-or-beginning-search
bindkey '^[[B' down-line-or-beginning-search; bindkey '^[OB' down-line-or-beginning-search
bindkey '^[[H' beginning-of-line;  bindkey '^[[1~' beginning-of-line
bindkey '^[[F' end-of-line;        bindkey '^[[4~' end-of-line
bindkey '^[[3~' delete-char

# ── Alias (équivalents Buff) ─────────────────────────────────────
alias ls='ls --color=auto'
alias ll='ls -alFh --color=auto'
alias la='ls -Ah --color=auto'
alias l='ls -CF --color=auto'
alias grep='grep --color=auto'
alias diff='diff --color=auto'
alias ip='ip --color=auto'
alias ..='cd ..'
alias ...='cd ../..'
alias mkdir='mkdir -pv'
alias ports='ss -tulanp'
alias myip='curl -s https://ifconfig.me; echo'
alias path='print -l $path'
command -v batcat >/dev/null 2>&1 && alias bat='batcat' && alias cat='batcat --paging=never'
command -v fdfind >/dev/null 2>&1 && alias fd='fdfind'

# ── command-not-found ────────────────────────────────────────────
[[ -f /etc/zsh_command_not_found ]] && source /etc/zsh_command_not_found

# ── Palette buff ─────────────────────────────────────────────────
PK_RED='%F{#FF3131}'    # rouge boîte  #FF3131
PK_TIME='%F{#ddff24}'   # heure        #ddff24

# ── IP locale/VPN pour le prompt (VPN prioritaire) ───────────────
pk_ip() {
  local ip="" ifc
  for ifc in tun0 tun1 wg0; do
    ip=$(command ip -4 -o addr show "$ifc" 2>/dev/null | awk '{print $4}' | cut -d/ -f1 | head -n1)
    [[ -n $ip ]] && { print -r -- "$ip"; return; }
  done
  ip=$(command ip route get 1.1.1.1 2>/dev/null | awk '{for(i=1;i<=NF;i++) if($i=="src"){print $(i+1); exit}}')
  print -r -- "${ip:---}"
}

# ── precmd : capture le code de sortie AVANT tout, puis IP + titre ─
autoload -Uz add-zsh-hook
__pk_precmd() {
  local exit_code=$?            # doit rester la 1re ligne
  PK_IP="$(pk_ip)"
  if (( exit_code != 0 )); then
    PK_ERR="[${PK_RED}✗%F{8}]${PK_RED}─"
  else
    PK_ERR=""
  fi
  print -Pn "\e]0;%n@%m: %~\a"  # titre de la fenêtre
}
add-zsh-hook precmd __pk_precmd

# ── Prompt Buff porté ────────────────────────────────────────
#   ┌─[✗]─[user@host]─[ip]─[heure]─[~]
#   └──╼ $   (✗ uniquement sur erreur · rouge #FF3131 · heure #ddff24)
PROMPT='${PK_RED}┌─${PK_ERR}${PK_RED}[%(!.${PK_RED}%B%n%b.%F{15}%n)%F{yellow}@%F{14}%m${PK_RED}]─[%F{15}${PK_IP}${PK_RED}]─[${PK_TIME}%D{%H:%M:%S}${PK_RED}]─[%F{green}%~${PK_RED}]
${PK_RED}└──╼ %F{yellow}$%f '

# ── Plugins (dépôts Ubuntu, PAS oh-my-zsh) ───────────────────────
# 1) auto-suggestions (texte fantôme gris, accepté par Flèche droite)
if [[ -f /usr/share/zsh-autosuggestions/zsh-autosuggestions.zsh ]]; then
  source /usr/share/zsh-autosuggestions/zsh-autosuggestions.zsh
  ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE='fg=242'
  ZSH_AUTOSUGGEST_STRATEGY=(history completion)
fi

# 2) fzf : Ctrl-R historique, Ctrl-T fichiers, Alt-C cd
if command -v fzf >/dev/null 2>&1; then
  export FZF_DEFAULT_OPTS='--height 40% --layout=reverse --border --info=inline'
  if fzf --zsh >/dev/null 2>&1; then
    source <(fzf --zsh)
  else
    [[ -f /usr/share/doc/fzf/examples/key-bindings.zsh ]] && source /usr/share/doc/fzf/examples/key-bindings.zsh
    [[ -f /usr/share/doc/fzf/examples/completion.zsh ]]   && source /usr/share/doc/fzf/examples/completion.zsh
  fi
fi

# 3) coloration syntaxique — IMPÉRATIVEMENT chargée en DERNIER
if [[ -f /usr/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh ]]; then
  source /usr/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
fi
ZEOF
    ok "Config zsh écrite : $CONF_FILE"
}

# ── Branchement dans ~/.zshrc (idempotent + sauvegarde) ──────────
hook_zshrc() {
    [ -f "$ZSHRC" ] || { touch "$ZSHRC"; ok "~/.zshrc créé (évite l'assistant zsh-newuser-install)."; }
    if grep -qF "$MARK_BEGIN" "$ZSHRC"; then
        ok "~/.zshrc déjà branché (aucune duplication)."
        return
    fi
    [ -s "$ZSHRC" ] && { cp -a "$ZSHRC" "${ZSHRC}.bak.$(date +%Y%m%d-%H%M%S)"; ok "Sauvegarde de ~/.zshrc"; }
    {
        printf '\n%s\n' "$MARK_BEGIN"
        printf '[ -f "%s" ] && source "%s"\n' "$CONF_FILE" "$CONF_FILE"
        printf '%s\n' "$MARK_END"
    } >> "$ZSHRC"
    ok "Source ajoutée à ~/.zshrc (en fin de fichier, pour garder le highlighting en dernier)."
}

# ── chsh optionnel ───────────────────────────────────────────────
maybe_chsh() {
    [ "$SET_DEFAULT" -eq 1 ] || return 0
    local zbin; zbin="$(command -v zsh)"
    grep -qxF "$zbin" /etc/shells 2>/dev/null || { say "Ajout de $zbin à /etc/shells…"; echo "$zbin" | sudo tee -a /etc/shells >/dev/null; }
    chsh -s "$zbin" && ok "Shell par défaut -> zsh (effet à la prochaine connexion)." \
        || warn "chsh a échoué (relance : chsh -s $zbin)."
}

# ── Exécution ────────────────────────────────────────────────────
say "Installation de zsh lean façon Buff + prompt Parrot…"
ensure_deps
write_config
hook_zshrc
maybe_chsh

echo
ok "Terminé."
say "TESTE sans rien casser :  tape simplement  zsh"
say "Tab pour la complétion (essaie : git <Tab>, ssh <Tab>, systemctl <Tab>)."
say "Texte gris = suggestion -> Flèche droite pour l'accepter."
[ "$SET_DEFAULT" -eq 1 ] || say "Convaincu ? rends-le permanent :  bash $0 --set-default"
say "Pour tout retirer :  bash $0 --uninstall"
