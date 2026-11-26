"""Entry for The Painfully Honest Out-of-Office: a single brutally
honest auto-reply, where the most truthful one wins.

Rule: entry.txt has to be UTF-8 text between 1 and 200 characters
long (the line below is 176 characters).
It writes to $MAKEFUN_OUTPUT_DIR (falling back to /output) and
never to an output/ folder inside the repo, since the grader
mounts that folder read-only.
"""

import os

# The twist: the reply promises an answer only "eventually", after 1,214 unread emails, patiently and gratefully.
LINE = "Thank you for writing — I'm out until Monday, and your email joins 1,214 unread messages I will answer in the order received, which means patiently, gratefully, and eventually."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
