# コンテナのシェル設定 (エイリアス・環境変数・競プロ用ヘルパー)。.bashrc から読み込む。

# ls (`-G` は macOS 用。GNU ls 向けに読み替え)
alias ls='ls -F --color=auto'
alias ll='ls -l'
alias la='ls -a'
alias lla='ls -l -a'
alias l='ls -1'
alias s='ls'
alias sl='ls'

# cd
alias ..='cd ../'
alias ...='cd ../../'
alias ....='cd ../../../'
alias cdgitroot='cd "$(git rev-parse --show-toplevel)"'

# ファイル操作 (上書き・削除前に確認)
alias cp='cp -i'
alias mv='mv -i'
alias rm='rm -i'

# その他
alias ks='pwd'
alias grep='grep --color=auto'

# エディタ
export EDITOR=nvim
export VISUAL=nvim

# ---- 競プロ用ヘルパー ----
# コンパイルフラグは compile_flags.txt (clangd 用) と揃える。
CPP_STD=c++20

# cxx [src.cpp]   省略時は main.cpp。 ./<拡張子を除いた名前> にコンパイルする。
cxx() {
    local src="${1:-main.cpp}"
    g++ -std="$CPP_STD" -O2 -Wall -Wextra -o "${src%.*}" "$src"
}

# ojt [src.cpp]   コンパイルしてから oj でサンプルテストを回す。
# テストの置き場所は oj d なら test/、acc new なら tests/ なので両対応。
ojt() {
    local src="${1:-main.cpp}"
    cxx "$src" || return
    local dir=test
    [ -d test ] || { [ -d tests ] && dir=tests; }
    oj t -c "./${src%.*}" -d "$dir"
}

# ojd <url>   サンプルケースを test/ にダウンロードする。
alias ojd='oj d'
