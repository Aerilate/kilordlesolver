# Kilordle Solver

Generates a list of words that solves [Kilordle](https://jonesnxt.github.io/kilordle/), the 1000-word variant of Wordle.

## Method
Since Kilordle automatically accepts words that have had letters in the correct position across previous guesses, you really just need a list of words that collectively have all 26 letters in all 5 positions. If Kilordle allowed guesses that weren't valid words, you could solve it in 26 guesses with just:
```python
[
  'aaaaa',
  'bbbbb',
  'ccccc',
  ...,
  'zzzzz'
]
```

But Kilordle does in fact only permit valid words as guesses. One approach to solve this is to formulate a linear program, which this script does.
