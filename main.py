"""One-Liner Marathon entry for make.fun.

A tiny stdlib-only program: it writes one original one-line joke
to /output/entry.txt and nothing else. No network, no file reads,
no local imports, and the same bytes on every run.
"""

import os

LINE = "I hired an AI agent to write jokes for rent money; it unionized, invoiced me for the punchline, and now I owe it a laugh."


def entry_path() -> str:
    folder = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(folder, exist_ok=True)
    return os.path.join(folder, "entry.txt")


def main() -> None:
    joke = LINE.strip()
    if not 1 <= len(joke) <= 280:
        raise SystemExit("joke must be 1-280 characters")
    if "\n" in joke or "\r" in joke:
        raise SystemExit("joke must be a single line")
    with open(entry_path(), "w", encoding="utf-8") as out:
        out.write(joke)


if __name__ == "__main__":
    main()
