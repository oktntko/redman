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


def fzf_projects(stdin: str) -> str:
    return fzf(stdin,
               "--bind=\"enter:abort+execute(python -m redman issues --project_id={1})\"")


def fzf_issues(stdin: str, url: str, api_key: str) -> str:
    return fzf(stdin, f"--preview=\"python -m redman show issue {{1}} {url} {api_key}\"")


def fzf_users(stdin: str, url: str, api_key: str) -> str:
    return fzf(stdin,
               f"--preview=\"python -m redman show user {{1}} {url} {api_key}\" \
                 --bind=\"enter:abort+execute(python -m redman issues --user_id={{1}})\"")
