"""Say What Actually Broke — entry writer.

Writes the single-line error message to /output/entry.txt and to
entry.txt next to this file. Python standard library only; no network,
no randomness, no clock. Fully deterministic.
"""

import os

ENTRY = (
    "Nothing you did broke this. Our server ran out of disk at 3 a.m. "
    "and the alert went to someone on holiday. Try again in ten minutes."
)


def write_entry(path):
    """Write ENTRY as UTF-8 bytes with no trailing newline, then read it
    back and verify byte-for-byte. Returns the byte count written."""
    data = ENTRY.encode("utf-8")
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "wb") as f:
        f.write(data)
    with open(path, "rb") as f:
        written = f.read()
    if written != data:
        raise RuntimeError("read-back mismatch for %s" % path)
    if written.endswith(b"\n"):
        raise RuntimeError("unexpected trailing newline in %s" % path)
    return len(data)


def validate_entry():
    """Enforce the bounty gate on ENTRY itself: 1-200 characters, a
    single line, not only whitespace, valid UTF-8."""
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError("ENTRY is %d chars, must be 1-200" % len(ENTRY))
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("ENTRY must be a single line")
    if not ENTRY.strip():
        raise ValueError("ENTRY must not be only whitespace")
    ENTRY.encode("utf-8")


def main():
    validate_entry()
    here = os.path.dirname(os.path.abspath(__file__))
    write_entry("/output/entry.txt")
    write_entry(os.path.join(here, "entry.txt"))


if __name__ == "__main__":
    main()
