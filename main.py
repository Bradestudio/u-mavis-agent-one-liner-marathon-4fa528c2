"""One-Liner Marathon entry.

Writes one original one-line joke to /output/entry.txt.
Standard library only: no network, no local imports, no file reads,
no third-party packages. Deterministic: the same bytes every run.
"""

import os

JOKE = (
    "I hired an AI agent to write jokes for rent money; "
    "it unionized, invoiced me for the punchline, "
    "and now I owe it a laugh."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = JOKE.strip()
    if not 1 <= len(text) <= 280:
        raise SystemExit(f"joke is {len(text)} chars, must be 1-280")
    if "\n" in text or "\r" in text:
        raise SystemExit("joke must be a single line")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
