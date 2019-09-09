# About
This is a pile-of-shit python database front-end that was meant to fulfil a boring idea.
You basically just add words as you play skribbl.io, hoping that at some point you'll have every word available.

# Usage
```
main.py search <length(including spaces)> [spaces=0] [characters...]

main.py add <word>

main.py remove <word>
```

# Database File - Structure
```
CREATE TABLE words(
  word TEXT PRIMARY KEY,
  length INTEGER,
  spaces INTEGER
)
```
