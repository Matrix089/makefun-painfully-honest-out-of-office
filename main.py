"""The Painfully Honest Out-of-Office entry.

Writes one original out-of-office email auto-reply to /output/entry.txt
(or to the directory named by MAKEFUN_OUTPUT_DIR when the grader sets
it).

The reply is painfully honest about the inbox and still polite enough
to survive being forwarded to a manager: the sender admits the email
will join 400 unread messages that get opened in order of dread, and
thanks the reader for their patience.
"""

import os

REPLY = "I'm out until Monday, and I should be honest: your email will join 400 unread messages that I will open in order of dread, so thank you for your patience."


def main():
    reply = REPLY.strip()
    if len(reply) != 154:
        raise SystemExit(f"Reply must be exactly 154 characters, got {len(reply)}")
    if not 1 <= len(reply) <= 200:
        raise SystemExit(f"Reply must be 1 to 200 characters, got {len(reply)}")
    if "\n" in reply:
        raise SystemExit("Reply must be a single line")
    if reply.count(".") != 1 or not reply.endswith("."):
        raise SystemExit("Reply must be a single sentence ending with one period")
    if "in order of dread" not in reply:
        raise SystemExit("Reply lost its turn of phrase: 'in order of dread'")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(reply)
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != reply:
        raise SystemExit("Read-back check failed: entry.txt does not match the reply")
    print(f"Wrote {len(reply)} characters to {path}")


if __name__ == "__main__":
    main()
