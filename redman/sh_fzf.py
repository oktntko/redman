import subprocess


def fzf_issues(echo: str, url: str, api_key: str) -> None:
    subprocess.run(
        f"echo '{echo}' | fzf --header-lines=2 \
            --preview='python -m redman show issue {{1}} {url} {api_key}'",
        shell=True, check=False, stdout=subprocess.PIPE) \
        .stdout.decode("utf-8").strip()
