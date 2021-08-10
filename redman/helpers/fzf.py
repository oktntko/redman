import subprocess

FZF_OPTIONS = "--header-lines=2 \
    --ansi \
    --no-multi \
    --no-mouse \
    --cycle \
    --reverse \
    --bind=alt-p:toggle-preview \
    --bind=alt-w:toggle-preview-wrap \
    --bind=ctrl-w:abort \
    --bind=shift-down:preview-down \
    --bind=shift-up:preview-up \
    --bind=shift-down:preview-down \
    --bind=shift-left:preview-page-up \
    --bind=shift-right:preview-page-down \
    --preview-window=down:50%:rounded:wrap"


def fzf(stdin: str, options: str = "") -> str:
    return subprocess.run(
        f"echo \"{stdin}\" | fzf {FZF_OPTIONS} {options}",
        shell=True, check=False, stdout=subprocess.PIPE) \
        .stdout.decode("utf-8").strip()
