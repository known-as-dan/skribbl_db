# About
This is a pile-of-shit python database front-end that was meant to fulfil a boring idea and was written on a whim.
You basically just add words as you play skribbl.io, hoping that at some point you'll have every word available to you.

The "words" database that's included, already contains a set of words that I stuffed into it, but it's far from complete.

# Usage
```
python skdb.py search <length(including spaces)> [spaces=0] [characters...]

python skdb.py add <word>

python skdb.py remove <word>
```

# Database File - Structure
```
CREATE TABLE words(
  word TEXT PRIMARY KEY,
  length INTEGER,
  spaces INTEGER
)
```
