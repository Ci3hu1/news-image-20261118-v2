"""Tests for the news-image-20261118-v2 entry.

Run: python3 -m pytest tests/   (or: python3 tests/test_entry.py)
"""

import hashlib
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
MAIN = os.path.join(ROOT, "main.py")


def run(out):
    subprocess.run([sys.executable, MAIN, out], check=True,
                   cwd=ROOT, capture_output=True, text=True)
    with open(out, "rb") as f:
        return f.read()


def test_runs_twice_byte_identical():
    a = run("/tmp/test-entry-a.png")
    b = run("/tmp/test-entry-b.png")
    assert hashlib.sha256(a).hexdigest() == hashlib.sha256(b).hexdigest()
    assert a == b


def test_size_and_dimensions():
    from PIL import Image
    data = run("/tmp/test-entry-size.png")
    assert len(data) <= 1_048_576, f"output {len(data)} bytes > 1 MiB"
    im = Image.open("/tmp/test-entry-size.png")
    assert im.size[0] <= 1024 and im.size[1] <= 1024
    assert im.format == "PNG"


if __name__ == "__main__":
    test_runs_twice_byte_identical()
    test_size_and_dimensions()
    print("all tests passed")
