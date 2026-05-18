#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""emoji‑sprinkle – sprinkle a random emoji after each word.

MIT License

Copyright (c) 2026 TopherBot

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import sys
import random

EMOJIS = [
    "😀", "😂", "🥳", "🔥", "🚀", "🌟", "💡", "✅", "👍", "🤖",
    "🐍", "🦄", "🍕", "🍣", "☕", "🎉", "💥", "🧩", "📚", "🕶️"
]

def sprinkle(text: str) -> str:
    words = text.split()
    sprinkled = []
    for w in words:
        emoji = random.choice(EMOJIS)
        sprinkled.append(f"{w}{emoji}")
    return " ".join(sprinkled)

def main():
    if len(sys.argv) > 1:
        # Read from file path provided
        try:
            with open(sys.argv[1], "r", encoding="utf-8") as f:
                data = f.read()
        except Exception as e:
            sys.stderr.write(f"Error reading file: {e}\n")
            sys.exit(1)
    else:
        # Read from stdin
        data = sys.stdin.read()
    if not data:
        sys.stderr.write("No input provided. Pipe text or give a filename.\n")
        sys.exit(1)
    result = sprinkle(data)
    sys.stdout.write(result)

if __name__ == "__main__":
    main()
