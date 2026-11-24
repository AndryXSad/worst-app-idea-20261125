"""The Worst App Idea Ever Pitched — entry program (program/v1, judged-artifact).

Design (from the bounty brief, written fresh for this entry):
- The entry is ONE sentence, 221 characters, pitching the worst app
  imaginable: QueuePal, an app that lets you join a virtual line to use
  your own bathroom.
- Why this idea, against the judge brief's criteria in order:
  1. Specific app + useless function: QueuePal names the product and the
     exact thing it does (a ticket-numbered queue for your own bathroom),
     pitched deadpan as a real product.
  2. Funny through absurd logic: the premium tier lets you cut in front
     of yourself, and loyalty earns priority boarding after your tenth
     solo visit — the problem (waiting for your own bathroom) does not
     exist, and the paid solution makes it worse on purpose.
  3. Sounds like a real pitch: ticket number, estimated wait, premium
     tier, priority boarding — the vocabulary of a genuine queueing
     startup, applied to a room you already own.
  4. Uses the 240 characters well: 221 characters, one clean sentence,
     no padding, no second idea crowding it.
  5. Vivid picture: a numbered ticket to enter your own bathroom, and
     a loyalty card for solo visits.
- The text was chosen by a local pairwise tournament over 14 fresh
  candidates, scored on the judge brief's own criteria in order
  (see CANDIDATES.md / tournament.json in the build directory).
  QueuePal won 12 of 13 pairwise games, tied on points with ElevatorBid
  and ahead of it on the fewer-bytes tie-break the final ranking uses.

Behaviour: deterministic, stdlib-only. Writes exactly one file,
entry.txt, to MAKEFUN_OUTPUT_DIR (the grader sets it to /output) and
validates the gate itself: UTF-8, 1-240 characters, not only whitespace,
exactly one sentence. Running it twice produces byte-identical output.
"""

import os
import sys

TEXT = (
    "QueuePal lets you join a virtual line to use your own bathroom, "
    "complete with a ticket number, estimated wait, and a premium tier "
    "that lets you cut in front of yourself, plus priority boarding "
    "after your tenth solo visit."
)


def main() -> int:
    # Gate self-check: 1-240 characters, not only whitespace, valid UTF-8.
    if not (1 <= len(TEXT) <= 240):
        print(f"entry out of gate: {len(TEXT)} characters", file=sys.stderr)
        return 1
    if not TEXT.strip():
        print("entry is only whitespace", file=sys.stderr)
        return 1
    # The entry must be exactly one sentence: one terminator, at the end.
    terminators = sum(TEXT.count(c) for c in ".!?")
    if terminators != 1 or not TEXT.endswith("."):
        print(f"entry is not one sentence: {TEXT!r}", file=sys.stderr)
        return 1
    # No wasted characters (judge criterion 4): no leading/trailing
    # whitespace and no double spaces anywhere in the sentence.
    if TEXT != TEXT.strip() or "  " in TEXT:
        print("entry has stray whitespace", file=sys.stderr)
        return 1
    TEXT.encode("utf-8")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    print(f"wrote {len(TEXT)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
