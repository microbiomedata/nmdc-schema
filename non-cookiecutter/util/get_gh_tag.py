from subprocess import run


def publish():
    completed = run(
        "git describe --tags $(git rev-list --tags --max-count=1)",
        shell=True,
        capture_output=True,
        encoding="utf-8",
    )

    vtag = completed.stdout.strip()

    print(vtag)


publish()
