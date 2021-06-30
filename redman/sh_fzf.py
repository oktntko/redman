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


def fzf_projects(echo: str) -> None:
    subprocess.run(
        f"echo \"{echo}\" | fzf {FZF_OPTIONS} \
            --bind=\"enter:abort+execute(python -m redman issues {{1}})\"",
        shell=True, check=False, stdout=subprocess.PIPE) \
        .stdout.decode("utf-8").strip()


def fzf_issues(echo: str, url: str, api_key: str) -> None:
    subprocess.run(
        f"echo \"{echo}\" | fzf {FZF_OPTIONS} \
            --preview=\"python -m redman show issue {{1}} {url} {api_key}\"",
        shell=True, check=False, stdout=subprocess.PIPE) \
        .stdout.decode("utf-8").strip()
