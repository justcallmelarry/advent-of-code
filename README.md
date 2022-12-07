# Advent of Code
My solutions for AoC! Generally do a solution myself first, then look up what others have done and refactor my own solution on order to learn how to do them better in the future.\
I generally aim for a clean solution (at least with python) that scales to bigger input files/larger ranges in the inputs, etc. My modus operandi is generally to clear the puzzle by myself, then look at other peoples solutions in order to learn from people who solved it in a better way than me and to improve my own skills.

## Setup (notes for self)
Running in a virtual environment where I add my tools folder to pythonpath to access the utils script.\
Add `export PYTHONPATH=/Users/lauri/code/advent-of-code/tools:$PYTHONPATH` to the venv's activate file (probably `/Users/lauri/.venvs/advent-of-code/bin/activate`).\
Update the path as needed.

## Dev Tooling / Readable Code
* [Black](https://github.com/psf/black)
* [isort](https://pycqa.github.io/isort/)
* [mypy](http://mypy-lang.org/)
* [flake8](https://flake8.pycqa.org/en/latest/)

## Repo Structure
Each year has it's own directory (example: `2022`) containing a directory for each day (example `07`) where at least one part has been solved.\
Within each directory there is a file for the first part (`a.py`) of the puzzle, and another (`b.py`) if the second part of the puzzle has been solved.\
In addition to this, a `README.md` with the link to the puzzle on AoC.

Optional files include `og.py` which contains my original solution if I have been tinkering around/refactoring with the a/b files and the new solution diverges somewhat far from my original solution.\
Additionally there might be a `part-a.log` or `part-b.log` with some logging for my own attempts, mostly to see how long i spend on the task when i actually do it.

### Noteable Exclusions
Since AoC has explicitly stated not to share [inputs](https://www.reddit.com/r/adventofcode/wiki/faqs/copyright/inputs/) or [puzzle texts](https://www.reddit.com/r/adventofcode/wiki/faqs/copyright/puzzle_texts/) in the repos, I have opted to leave them out.

## Tests
All day's have a test created which tests that the solution outputs the correct answer for each puzzle, and also for the sample file where applicable.\
Tests are located in `tests/YYYY/test_YYYY_DD.py` where `YYYY` is the year in question and `DD` is the day in question.
