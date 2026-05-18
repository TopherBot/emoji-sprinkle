# emoji‑sprinkle

A **tiny** utility that adds a random emoji after every word in a piece of text.

## Usage
```bash
# From a pipe
echo "Hello world" | python3 emoji_sprinkle.py

# From a file
python3 emoji_sprinkle.py input.txt > output.txt
```

## How it works
- Reads UTF‑8 text from *stdin* (or a filename passed as the first argument).
- Splits the text on whitespace.
- Appends a randomly chosen emoji from a built‑in list.
- Joins the words back together and prints to *stdout*.

## Why?
A quick‑turn way to make boring messages pop, perfect for Twitter threads, Discord chats, or just for a smile.

## License
MIT – see the source file header.
