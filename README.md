# SpellCheck

SpellCheck is a Python project designed as a learning exercise to implement the [Wagner-Fischer algorithm](https://en.wikipedia.org/wiki/Wagner%E2%80%93Fischer_algorithm) for word validation and suggesting corrections for misspelled words. While useful for educational purposes, it's important to note that this project does not utilize the advanced techniques found in modern spellcheckers, such as neural networks and statistical models that take into account contextual information and typists' common errors. 

## Features
- Validates words against a dictionary.
- Suggests corrections for misspellings.
- Configurable dictionary size in `settings.py`.
- Configurable suggestion threshold in `settings.py`.

## Setup
- Requires Python 3.
- Files: `dictionary.py`, `settings.py`, `words.txt`.

## Usage
- Run `python3 main.py`.
- Input a word to check or get suggestions.

## Example
```
$ python3 main.py
Enter a word: spellign
Did you mean:
spelling
```

## Contributing
Contributions are welcome. Please fork and submit pull requests.