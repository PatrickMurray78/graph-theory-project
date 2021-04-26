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

## Research
Throughout the semester I have been watching the videos that have been posted on learnonline and completing the corresponding labs for each week of content. 
I have never used python before so I felt this was a good opportunity to take a quick [course](https://youtu.be/_uQrJ0TkZlc) in python at the beginning of the semester as I knew it would help me understand the language. Towards the end of the video there were some exercises to complete which were challenging but I found it very useful and it gave me a headstart for this module which has helped me throughout the semester.

The videos on learnonline were very well put together and I understood everything for the most part until we began the shunting yard algorithm. This was mainly with converting infix to postfix and what they meant. I found this [video](https://youtu.be/b6miFHYFaVI) on youtube which went through infix and postfix in depth. With my newfound understanding of converting infix to postfix, I finished off implementing the [shunting yard algorithm](https://en.wikipedia.org/wiki/Shunting-yard_algorithm) which converts infix regular expressions to postfix. This was not too difficult to do as most of the code was provided through the lab videos.

Thompson's construction was the next topic covered and it proved to be a hard topic to grasp. I spent a lot of time on the [wiki](https://en.wikipedia.org/wiki/Thompson%27s_construction) which helped me understand how I could join NFAs together using special symbols. I also took this time to look more in depth into NFA's as I had never came across them before. Although automatons are similar to NFA's, an NFA can transition to and be in multiple states at once. I found lots of information on NFA's [here](https://en.wikipedia.org/wiki/Nondeterministic_finite_automaton).

The next step was searching a text file using a regular expression. I understand the logic after I read in a text file but I did not know how to actually read in the text file. We were provided with the code `with open('file.txt', 'r') as f:`. I checked out the python docs on [reading and writing files](https://realpython.com/read-write-files-python/) which gave me all the information I needed to implement this part of the project.

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
