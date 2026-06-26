#!/bin/bash
set -euo pipefail

CONTAINER_DIR="$(cd "$(dirname "$0")" && pwd)"
CPP_DIR="$(dirname "$CONTAINER_DIR")"
IMAGE_NAME="atcoder-cpp"

# Persisted state (oj/acc login sessions and acc config). Kept OUTSIDE the repo
# because it holds session cookies; mounted into the container so logins and the
# acc template survive the --rm container.
STATE_DIR="${XDG_DATA_HOME:-$HOME/.local/share}/atcoder-cpp"
ACC_STATE="$STATE_DIR/acc"   # -> container ~/.config/atcoder-cli-nodejs
OJ_STATE="$STATE_DIR/oj"     # -> container ~/.local/share/online-judge-tools

detect_runtime() {
    for cmd in docker podman container; do
        if command -v "$cmd" &>/dev/null; then
            echo "$cmd"
            return
        fi
    done
    echo "Error: docker, podman, or container not found" >&2
    exit 1
}

usage() {
    cat <<EOF
Usage: $0 [--runtime <docker|podman|container>] <command> [args]

Commands:
  build              Build the container image (uses cache)
  rebuild            Rebuild from scratch (--no-cache)
  bash [dir]         Start bash in the container
                     dir: optional subdirectory to start in (e.g. abc/abc413)

Examples:
  $0 build
  $0 --runtime podman build
  $0 bash abc/abc413
EOF
    exit 1
}

RUNTIME=""
POSITIONAL=()
while [[ $# -gt 0 ]]; do
    case "$1" in
        --runtime)
            RUNTIME="${2:?--runtime requires a value}"
            shift 2
            ;;
        --runtime=*)
            RUNTIME="${1#*=}"
            shift
            ;;
        --*)
            echo "Error: unknown option '$1'" >&2
            usage
            ;;
        *)
            POSITIONAL+=("$1")
            shift
            ;;
    esac
done
# Expand safely even when empty (bash 3.2 on macOS errors on "${arr[@]}" under set -u).
set -- ${POSITIONAL[@]+"${POSITIONAL[@]}"}

# No command -> show help (before resolving the runtime, so help works anywhere).
if [[ $# -eq 0 ]]; then
    usage
fi

RUNTIME="${RUNTIME:-$(detect_runtime)}"

cmd_build() {
    # $1: optional extra build flag (e.g. --no-cache)
    echo "Building image with $RUNTIME..."
    $RUNTIME build ${1:+"$1"} -t "$IMAGE_NAME" -f "$CONTAINER_DIR/CONTAINERFILE" "$CONTAINER_DIR"
}

cmd_bash() {
    if ! $RUNTIME image inspect "$IMAGE_NAME" &>/dev/null; then
        echo "Image not found. Building..."
        cmd_build
    fi

    local workdir="/work"
    if [[ -n "${1:-}" ]]; then
        mkdir -p "$CPP_DIR/$1"
        workdir="/work/$1"
    fi

    # Persist login sessions / acc config across runs, and seed the acc template
    # (named "cpp") on first use so `acc new` can scaffold main.cpp.
    mkdir -p "$ACC_STATE" "$OJ_STATE"
    if [[ ! -e "$ACC_STATE/cpp" ]]; then
        cp -R "$CONTAINER_DIR/acc-template" "$ACC_STATE/cpp"
    fi

    $RUNTIME run -it --rm \
        -v "$CPP_DIR:/work" \
        -v "$ACC_STATE:/root/.config/atcoder-cli-nodejs" \
        -v "$OJ_STATE:/root/.local/share/online-judge-tools" \
        -w "$workdir" \
        "$IMAGE_NAME" \
        bash
}

case "${1:-}" in
    build)   cmd_build ;;
    rebuild) cmd_build --no-cache ;;
    bash)    cmd_bash "${2:-}" ;;
    *)       usage ;;
esac
