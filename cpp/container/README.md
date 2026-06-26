# C++競プロ環境

C++でAtCoderを解くためのコンテナ環境。コンパイラ、Neovim、AtCoder用CLIが一通り入っている。

## 含まれるもの

- **C++ツールチェイン**: GCC (g++), GDB, C++20
- **エディタ**: Neovim + LSP (clangd) + 補完 + シンタックスハイライト
- **AtCoderツール**: online-judge-tools (oj), atcoder-cli (acc)

## ビルドと起動

```bash
# イメージをビルド
./run.sh build

# bash に入る (引数でサブディレクトリを指定でき、なければ作成される)
./run.sh bash
./run.sh bash abc/abc413
```

docker, podman, Apple Container (container) のいずれかが必要。インストール済みのものを自動検出する。
明示したい場合は `--runtime` で指定する。

```bash
./run.sh --runtime podman build
```

## 問題を解く

```bash
# コンテナ内で。問題ごとにディレクトリを切る
mkdir -p abc/abc999/a && cd abc/abc999/a

# テストケースを取得 (ojd = oj d)
ojd https://atcoder.jp/contests/abc999/tasks/abc999_a

# 編集
nvim main.cpp

# コンパイルしてテスト (ojt = コンパイル + oj t。省略時は main.cpp)
ojt

# 提出
oj s https://atcoder.jp/contests/abc999/tasks/abc999_a main.cpp
```

`ojd` / `ojt` はコンテナに入れてあるヘルパー。素の `oj`, `g++` ももちろん使える。

## acc でまとめて解く

atcoder-cli (acc) を使うと、コンテストの全問題ディレクトリ作成・サンプル取得・提出をまとめて行える。

### 初回だけの設定

ログイン状態とテンプレートはホスト側 (`~/.local/share/atcoder-cpp/`) に永続化されるので、設定は一度だけでよい。

```bash
acc login                          # AtCoder にログイン
oj login https://atcoder.jp/       # oj 側のログイン (取得・提出用)
acc config default-template cpp    # main.cpp の雛形を自動配置する
```

### 普段の流れ

```bash
# コンテストの作業ディレクトリを一括生成 (対話で問題を選ぶ。サンプルも取得される)
acc new abc999
cd abc999/a

# 編集 (main.cpp は雛形から生成済み)
nvim main.cpp

# コンパイルしてテスト (ojt は test/ と acc の tests/ 両方に対応)
ojt

# 提出
acc submit main.cpp
```

テンプレートの実体は `acc-template/` (`main.cpp` + `template.json`)。`run.sh` が初回起動時に acc の設定ディレクトリへ配置する。

### エイリアス・ヘルパー

`shell/bashrc.sh` をシェル起動時に読み込んでいる。主なもの:

- `cxx [src.cpp]` - コンパイル (省略時 main.cpp、`-std=c++20 -O2 -Wall -Wextra`)
- `ojt [src.cpp]` - コンパイルして `oj t` でサンプルテスト
- `ojd <url>` - サンプルケースを `test/` にダウンロード (`oj d`)
- ほかに `ll`, `la`, `..`, `cdgitroot`, `cp/mv/rm -i` など

`EDITOR` / `VISUAL` は `nvim` に設定済み。

### Neovimのキーバインド

`<leader>` = Space。

- `<Space>cc` - コンパイル (g++ -std=c++20 -O2)
- `<Space>cr` - 実行
- `<Space>ct` - コンパイルして oj でテスト
- `<Space>ff` - ファイル検索
- `<Space>fg` - grep検索
- `gd` - 定義へジャンプ
- `K` - ホバー

## ファイル構成

- `CONTAINERFILE` - コンテナ定義
- `run.sh` - ビルド・起動スクリプト
- `compile_flags.txt` - clangd用のコンパイルフラグ (C++20, -Wall, -Wextra)
- `config/nvim/init.lua` - Neovim設定 (lazy.nvim, clangd, nvim-cmp, treesitter, telescope, catppuccin)
- `shell/bashrc.sh` - エイリアス・エディタ設定・競プロ用ヘルパー (cxx, ojt, ojd)
- `acc-template/` - acc 用のコードテンプレート (main.cpp, template.json)
