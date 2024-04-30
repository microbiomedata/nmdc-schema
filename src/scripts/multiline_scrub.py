import click
import re
import sys


@click.command()
@click.option('--pattern', '-p', required=True, help="The complete pattern (including newlines) to remove.")
def multiline_scrub(pattern):
    """CLI for performing multi-line text replacement with whole pattern matching, using stdin/stdout."""
    if not sys.stdin.isatty():
        content = sys.stdin.read()
    else:
        print("Error: Input from stdin is required.")
        sys.exit(1)

    new_content = re.sub(pattern, "", content, flags=re.MULTILINE)

    sys.stdout.write(new_content)


if __name__ == '__main__':
    multiline_scrub()
