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

The next step was searching a text file using a regular expression. I understand the logic after I read in a text file but I did not know how to actually read in the text file. We were provided with the code `with open('file.txt', 'r') as f:`. I checked out the python docs on [reading and writing files](https://realpython.com/read-write-files-python/) where I found an example of [iterating over each line in a file](https://realpython.com/read-write-files-python/#iterating-over-each-line-in-the-file) which was exactly what I needed to accomplish.

## What is a regular expression?
A regular expression is a specially encoded string of text that is used as a pattern for matching sets of strings. A  regular expressions is also known as a regex or regexp and is also referred to as a rational expression.  Usually these patterns are used by string-serching algorithms for "find" or "find and replace" operations on strings, or for input validation. They began to emerge in the 1940s as a way to describe regular languages, but they really began to show up in the programming world during the 1970s. Regular expressions later became an important part of the tool suite that emerged from the Unix operating system—the ed, sed and vi (vim) editors, grep, AWK, among others. There have been different syntaxes for writing regular expressions since the 1980s, one being the [POSIX](https://en.wikipedia.org/wiki/POSIX) standard and another, widely used, being the [Perl](https://en.wikipedia.org/wiki/Perl) syntax. Many programming languages provide regex capabilities either built-in or via libraries, as it has uses in many situations. Each character in a regular expression is either a [metacharacter](https://en.wikipedia.org/wiki/Metacharacter) which is a character that has a special meaning or a regular character that has a literal meaning. For example, in the regex `b.`, 'b' is a literal character that matches just 'b', while '.' is a metacharacter that matches every character that except a newline. Therefore, this regex matches, for example, 'b%', or 'bx', or 'b5'. Together, metacharacters and literal characters can be used to identifiy text of a given pattern or process a number of instances of it. The metacharacter syntax is designed specifically to represent prescribed targets in a concise and flexible way to direct the automation of text processing of a variety of input data, in a form easy to type using a standard ASCII keyboard. A [formalism](https://en.wikipedia.org/wiki/Formalism_(philosophy_of_mathematics)) is the view that holds that statements of mathematics and logic can be considered to be statements about the consequences of the manipulation of strings using established manipulation rules and most formalisms provide the following operations to construct regular expressions.
### Boolean "or"
A vertical bar seperates alternatives. For example, `gray|grey` can match "gray" or "grey".
### Grouping
Parentheses are used to define the scope and precedence of the operators (among other uses). For example, `gray|grey` and `gr(a|e)y` are equivalent patterns which both describe the set of "gray" or "grey".
### Quantification
A quantifier after a token (such as a character) or group specifies how often that a preceding element is allowed to occur. The most common quantifiers are the question mark `?`, the asterisk `*` (derived from the Kleene star), and the plus sign `+` (Kleene plus).
- `?` The question mark indicates zero or one occurrences of the preceding element. For example, `colou?r` matches both "color" and "colour".
- `*` The asterisk indicates zero or more occurrences of the preceding element. For example, `ab*c` matches "ac", "abc", "abbc", "abbbc", and so on.
- `+` The plus sign indicates one or more occurrences of the preceding element. For example, `ab+c` matches "abc", "abbc", "abbbc", and so on, but not "ac".
- `{n}` The preceding item is matched exactly n times.
- `{min,}` The preceding item is matched min or more times.
- `{,max}` The preceding item is matched up to max times.
- `{min,max}` The preceding item is matched at least min times, but not more than max times.
### Wildcard
The wildcard `.` matches any character. For example, `a.b` matches any string that contains an "a", then any other character and then "b", `a.*b` matches any string that contains an "a", and then the character "b" at some later point.

## How do regular expressions differ across implementations?
The differences in implementations are usually the way special characters `{}()[]^$` are handled and occasionally substituted, the handling/availability of POSIX character classes e.g `[:digit:]` and the use of options e.g `g` `i` etc. There is a very informative table on the [comparison of regular-expression engines wiki](https://en.wikipedia.org/wiki/Comparison_of_regular-expression_engines) page


* How special characters `{}()[]^$` are handled and occasionally substituted.
* The handling/availability of POSIX character classes e.g `[:digit:]`.
* The use of options e.g `g` `i` etc.
* https://stackoverflow.com/questions/4644847/list-of-all-regex-implementations

## Can all formal languages be encoded as regular expressions?
