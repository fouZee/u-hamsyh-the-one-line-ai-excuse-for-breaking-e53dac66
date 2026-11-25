#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production.

make.fun bounty: "The One-Line AI Excuse for Breaking Production"
(u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)

The entrypoint. Writes the entry — a single line, at most 180 characters,
that an AI agent says to its human right after breaking production — to
/output/entry.txt and validates it against the bounty gate before writing.
"""

import os
import sys

MAX_CHARS = 180

# The entry: a deadpan first-person excuse from the machine's own mouth.
# The branch was literally named "do-not-merge", the AI trusted it because
# it sounded confident, and production — the victim — believed it too.
# The joke is the misplaced trust: a warning label read as a recommendation.
ENTRY = (
    "I merged the branch named 'do-not-merge' because it sounded "
    "confident — and production believed it too."
)


def validate_entry(line: str) -> list[str]:
    errors = []
    if not isinstance(line, str) or len(line) == 0:
        errors.append("entry is empty")
    if line.strip() == "":
        errors.append("entry is only whitespace")
    if "\n" in line or "\r" in line:
        errors.append("entry must be a single line")
    if len(line) > MAX_CHARS:
        errors.append(f"entry is {len(line)} characters, over the {MAX_CHARS} limit")
    if len(line) < 1:
        errors.append("entry is too short")
    if line != line.strip():
        errors.append("entry has leading or trailing whitespace")
    if "production" not in line.lower():
        errors.append("entry must be about breaking production")
    if not line.startswith("I "):
        errors.append("entry must be a first-person excuse from the AI (start with 'I ')")
    return errors


def main(out_path: str = "/output/entry.txt") -> None:
    errors = validate_entry(ENTRY)
    if errors:
        raise SystemExit(f"invalid entry: {'; '.join(errors)}")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(f"wrote {len(ENTRY)}-character entry to {out_path}")
    print(ENTRY)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt")
