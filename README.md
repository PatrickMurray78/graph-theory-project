# Project: Graph Theory 2021

## What is this?
This is a Python 3 project that searches a text file using a [regular expression](https://en.wikipedia.org/wiki/Regular_expression). The program takes a regular expression and the name of the file as command line arguments and outputs the lines of the file matching the regular expression. [Nondeterministic finite automata](https://en.wikipedia.org/wiki/Nondeterministic_finite_automaton) are used to parse the regular expressions.

## What do the files in the repository do?
1. **Labs folder** - contains all labs completed for this module.
2. **Main.py** - contains the main code for the application.
3. **README.md** - contains useful information about the project (How to run, explantion of algorithm etc).

## How to run the program
1. Python 3 is required to run this project.
2. Clone repository by using the following command in your terminal `git clone https://github.com/PatrickMurray78/graph-theory-project.git`.
3. Using the command line change your directory to the folder where you cloned this repository.
4. Once inside the folder, run `python3 main.py` which will run the program.

## What is a regular expression?
* Sequence of characters that specifies a search pattern.
* Helps match, locate and manage text.
* Each character in a regex is either a metacharacter (has a special meaning) or a regular character (has a literal meaning).
* Boolean, Grouping, Quantification, Wildcard
* Formal language theory.
* Regular expression equivalence.

## How do regular expressions differ across implementations?
* How special characters `{}()[]^$` are handled and occasionally substituted.
* The handling/availability of POSIX character classes e.g `[:digit:]`.
* The use of options e.g `g` `i` etc.
* https://stackoverflow.com/questions/4644847/list-of-all-regex-implementations

## Can all formal languages be encoded as regular expressions?
