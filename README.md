# caracaro-tech-exam

Technical exam submission repository for admission at CaraCaro. Includes instructions on how to properly run test cases.

## Instructions on running the test cases

1. Make sure the [latest version of Python 3](https://www.python.org/downloads/) is installed.
2. For seamless execution of running the test cases, make sure running Python as `python` in a terminal is enabled in the current project repository directory. This can be done by [having the Python executable accessible in PATH](https://realpython.com/add-python-to-path/).
3. Create a test file (preferably `input.txt`) in the current project repository directory to include the test cases.
4. Open a terminal instance in the current project repository directory.
5. In the terminal instance, type `python3 $SOLUTION_FILE < $INPUT_FILE` to run `$SOLUTION_FILE` with the given test cases inside `$INPUT_FILE`.

* `$SOLUTION_FILE` is either `the_trigram.py` or `expand_the_acronyms.py`.
* `$INPUT_FILE` is your named `.txt` (or `input.txt`) input file.
* Example usage: `python3 the_trigram.py < input.txt`.

## Some notes

* I structured running the solutions with test cases as `python3 $SOLUTION_FILE < $INPUT_FILE` to accommodate newline-separated inputs that are also present in HackerRank.
* I ran the solutions online in HackerRank, so I assume that running the solution in a machine works regardless of its operating system, as long as Python 3 is compatible in that machine. Links are as follows:
  * [The trigram](https://www.hackerrank.com/challenges/the-trigram/problem)
  * [Expand the acronyms](https://www.hackerrank.com/challenges/expand-the-acronyms/problem)
