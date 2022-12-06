# Advent of Code

My solutions for AoC! Generally do a solution myself first, then look up what others have done and refactor my own solution on order to learn how to do them better in the future.\
I generally aim for a clean solution (at least with python) that scales to bigger input files/larger ranges in the inputs, etc. My modus operandi is generally to clear the puzzle by myself, then look at other peoples solutions in order to learn from people who solved it in a better way than me and to improve my own skills.

## Setup (self)
Running in a virtual environment where I add my tools folder to pythonpath to access the utils script.\
Add `export PYTHONPATH=/Users/lauri/code/advent-of-code/tools:$PYTHONPATH` to the venv's activate file (probably `/Users/lauri/.venvs/advent-of-code/bin/activate`).\
Update the path as needed.

## Formatting
Uses [Black](https://github.com/psf/black) and [isort](https://pycqa.github.io/isort/) for code formatting/readability.\
Fully type hinted with [mypy](http://mypy-lang.org/).\
Linting handled with [flake8](https://flake8.pycqa.org/en/latest/).

## Repo structure
Each year has it's own directory (example: `2022`) containing a directory for each day (example `07`) where at least one part has been solved.\
Within each directory there is a file for the first part (`a.py`) of the puzzle, and another (`b.py`) if the second part of the puzzle has been solved.\
In addition to this, a `README.md` is provided with the puzzle description from AoC, as well as the user input `input.user` to run the puzzles.

Optional files include `og.py` which contains my original solution if I have been tinkering around/refactoring with the a/b files and the new solution diverges somewhat far from my original solution. Additionally there is sometimes/usually an `input.sample` present if there was an example present in the task that can be solved in the same way as the actual input.\
Additionally there might be a `part-a.log` or `part-b.log` with some logging for my own attempts, mostly to see how long i spend on the task when i actually do it.

## Tests
All day's have a test created which tests that the solution outputs the correct answer for each puzzle, and also for the sample file where applicable.\
Tests are located in `tests/YYYY/test_YYYY_DD.py` where `YYYY` is the year in question and `DD` is the day in question.
