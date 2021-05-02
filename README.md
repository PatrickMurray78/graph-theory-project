# Project: Graph Theory 2021

# What is this?
This is a Python 3 project that searches a text file using a [regular expression](https://en.wikipedia.org/wiki/Regular_expression). The program takes a regular expression and the name of the file as command line arguments and outputs the lines of the file matching the regular expression. [Nondeterministic finite automata](https://en.wikipedia.org/wiki/Nondeterministic_finite_automaton) are used to parse the regular expressions.

# What do the files in the repository do?
1. **Labs folder** - contains all labs completed for this module.
2. **Main.py** - contains the main code for the application.
3. **shunt.py** - contains the code for shunting yard algorithm for regular expressions
4. **thompson.py** - contains the code for thompsons construction and match function
5. **tests.py** - contains tests that can be ran through command line
6. **README.md** - contains useful information about the project (How to run, explantion of algorithm etc).

# How to run the program
1. Python 3 is required to run this project.
2. Clone repository by using the following command in your terminal `git clone https://github.com/PatrickMurray78/graph-theory-project.git`.
3. Using the command line change your directory to the folder where you cloned this repository.
4. Once inside the folder, run `python3 main.py` which will run the program.
5. Tests can be run by running `python3 main.py --test`.

Note: Depending on your setup you may need to run `python main.py` or `python main.py --test`

# User Guide
To run the program, follow the steps above. Once the program has launched you will be presented with this screen.
![](https://github.com/PatrickMurray78/graph-theory-project/blob/main/Images/MenuTest.png)  
You will have two options.
1.	Search text file using regular expression. This allows the user  to enter a regular expression and also the name of or path to file to match the regular expression against. This returns the lines that match the regular expression entered and also the string on the line.  
![](https://github.com/PatrickMurray78/graph-theory-project/blob/main/Images/FileTest.png)
2.	Exit. This allows the user to exit the program and return to the command line.  
![](https://github.com/PatrickMurray78/graph-theory-project/blob/main/Images/ExitTest.png)
## Run tests
When the tests are ran by adding `--test` as a param when running the code the following is displayed.  
![](https://github.com/PatrickMurray78/graph-theory-project/blob/main/Images/Tests.png)

# How does it work?
When the program is ran, the menu is loaded which allows the user to enter one of two options. Option 1 allows the user to search a text file using a regular expression to find matches and option 2 will exit the program. When option 1 is selected the user will be prompted to enter the regular expression they wish to use to find matches for and also the name or path to the file which contains the strings to compare the regular expression against. The first function that is called from here is `searchFile`.

### searchFile(infix, filePath)
The searchFile function takes in two parameters which are infix and filePath. Infix is the regular expression that was entered by the user and filePath is the name of the file or the filepath to the file. This function then tries to open that file and if it is successful it iterates through each line and removes the newline character from the end. We then get the postfix of the infix regex entered  using shunt.py, then proceed to get the nfa of the postfix using thompson.py and finally we match the nfa to the line of the file we are on. If the line matches the nfa then we output the line number and also the text on that line. If the file is not found then an error message is returned.

### Shunting Yard Algorithm
The shunting yard algorithm converts an infix regular expression to a postfix regular expression. It does so by looping through the infix regular expression which was passed from the searchFile function. If the first character is a ‘(‘ we add this to the stack. When the corresponding ‘)’ is then encountered we add whats on the stack until the ‘(‘ is encountered and then we remove it. If the character is an operator and the stack is empty, push the character to the stack. If the character is an operator and has a higher precedence than the operator on the top of the stack or has the same precedence as the operator on the top of the stack  and is right associative we push it to the stack. If the character is an operator and has a lower precedence than the operator on top of the stack or has the same precedence as the operator on top of the stack and is left associative, continue to pop the stack until this is not true, then push the character to the top of the stack. If the character is none of the above then push it to the stack. After this has finished remove all additional characters from the stack and return the postfix string.

### Thompson Contruction Algorithm
The thompson contruction algorithm converts a postfix regular expression to an NFA. This NFA can then be used to match strings against the regular expression. It begins by looping through the postfix regular expression which was passed from the searchFile function after getting it from the shunting yard algorithm. It then checks each character to see if it matches any of the operators (. | * ? +) and creates an NFA which is added to the NFA stack. By using the NFA class and constructor we can set up initial and accept states. I will briefly explain what happens when each operator is encountered.

#### Concatenation operator `.`
Pop first two NFA’s from the stack. Make the acccept state of NFA1 non-accept and make it point at the start state of NFA2 to connect them. Make a new NFA and push it to the stack.
**Or operator `|`**
Pop first two NFA’s from the stack and create new start and end states. Make  the new start state point at the old start states. Make the old accept states non-acept and point the old end states to the new one. Make a new NFA and push it to the stack.

#### Kleene star operator `*`
Pop one NFA from the stack. Create new start and end states and make the new start state point at the old start state and the new end state. Make the old accept state non-accept and make it point to the new end state and also the old start state. Make a new NFA and push it to stack.

#### `?` operator
Pop one NFA from the stack and create new start and end states. Make new start state point at old start state and at the new end state. Make the old accept state pointto the new end state. Make a new NFA and push it to the stack.

#### `+` operator
Pop one NFA from the stack and create new start and end states. Make new start state point at old start state. Make old accept state point to new end state and old start state. Make a new NFA and push it to stack.

#### Non-special character
If a character is encountered which is not an operator, we create an end state and a start state which points at the end state. Point the new start state at new end state. Make a new NFA and push it to stack.

### match(self, s)
The match function checks if a string matches an infix regular expression and returns true if this NFA (instance) matches the string. First we get a list of all previous states we were in by calling the followes() function which I will describe below. We then loop through the string s, a character at a time. We start with an empty set of current states and loop  through the previous states while checking if there is a c arrow from state. If there is add followes for the  next  state and replace the previious with current. If the final state is in previous, then return true as it matches otherwise return false.

### followes(self)
The followes function returns  the set of states that are gotten from following this NFA (instance) and all of its e arrows. First we include this state in the returned set. If this state has e arrows, i.e the label is None it will check all arrows and follow them if possible. If it is able to follow them then it will start the process again from that arrow until it can follow no more arrows. Finally it will return the set of states.

### tests()
The tests function allows the user to run some predefined tests. To do this I used argparse which allows the user to run the `--test` command in command line when running the code which will run the tests. Once the command is ran, the tests array is looped through. For each test in tests we set the infix to  the first field in test. Then we get the postfix of the infix regex using shunt.py. Using this infix we get the NFA using thompson.py. We can then loop through the second field of each test as this contains another array of strings to match against the NFA. If the string matches the NFA it will output true, else will output false.

# Research
Throughout the semester I have been watching the videos that have been posted on learnonline and completing the corresponding labs for each week of content. 
I have never used python before so I felt this was a good opportunity to take a quick [course](https://youtu.be/_uQrJ0TkZlc) in python at the beginning of the semester as I knew it would help me understand the language. Towards the end of the video there were some exercises to complete which were challenging but I found it very useful and it gave me a headstart for this module which has helped me throughout the semester.

The videos on learnonline were very well put together and I understood everything for the most part until we began the shunting yard algorithm. This was mainly with converting infix to postfix and what they meant. I found this [video](https://youtu.be/b6miFHYFaVI) on youtube which went through infix and postfix in depth. With my newfound understanding of converting infix to postfix, I finished off implementing the [shunting yard algorithm](https://en.wikipedia.org/wiki/Shunting-yard_algorithm) which converts infix regular expressions to postfix. This was not too difficult to do as most of the code was provided through the lab videos.

Thompson's construction was the next topic covered and it proved to be a hard topic to grasp. I spent a lot of time on the [wiki](https://en.wikipedia.org/wiki/Thompson%27s_construction) which helped me understand how I could join NFAs together using special symbols. I also took this time to look more in depth into NFA's as I had never came across them before. Although automatons are similar to NFA's, an NFA can transition to and be in multiple states at once. I found lots of information on NFA's [here](https://en.wikipedia.org/wiki/Nondeterministic_finite_automaton).

The next step was searching a text file using a regular expression. I understand the logic after I read in a text file but I did not know how to actually read in the text file. We were provided with the code `with open('file.txt', 'r') as f:`. I checked out the python docs on [reading and writing files](https://realpython.com/read-write-files-python/) where I found an example of [iterating over each line in a file](https://realpython.com/read-write-files-python/#iterating-over-each-line-in-the-file) which was exactly what I needed to accomplish.

To allow the user to run the tests by running `python3 main.py --test`, I had to implement argparse. I began by watching the [Python: argparse](https://learnonline.gmit.ie/mod/url/view.php?id=188219) video and had a look through the [docs](https://docs.python.org/3/library/argparse.html). I had a good understanding of arparse after learning what I could from both resources, however I was still unable to get it working. While browsing through stackoverflow I came across this [post](https://stackoverflow.com/questions/42818876/python-3-argparse-call-function) where it became clear that I was using the `dest` param incorrectly. I quickly fixed this and used the `dest` param to check if it equalled tests which then ran the tests function.

At this stage I was finished with all the main functionality for the project. I wanted to add the operators `?` and `+` which I had found by reading through the regular expression [wiki](https://en.wikipedia.org/wiki/Regular_expression). I found out that `?` indicates zero or one occurrences of the preceding element. For example, `colou?r` matches both "color" and "colour". `+` on the other hand indicates one or more occurences of the preceding element. For example, `ab+c` matches "abc", "abbc" and "abbc". Both of these operators have the same precendence as the kleene star `*`.

After the project was completed I wanted to change the way the tests were output by having columns of equal width. Figuring out how to do this would result in my whole program looking neater and more pleasing to the eye as currently it looks messy when I output different columns of data if they are different lengths. I was unable to find what I was looking for in the python documentation but I came across this [stackoverflow post](https://stackoverflow.com/questions/4302166/format-string-dynamically) where the top answer was exactly the solution I was looking for. This way of formatting was very similar to what I had used in java previously but there were some slight differences. This proved to be very easy to implement and greatly improved the aesthetics of my program in the command prompt.

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
The differences in implementations are usually the way special characters `{}()[]^$` are handled and occasionally substituted, the handling/availability of POSIX character classes e.g `[:digit:]` and the use of options e.g `g` `i` etc. There is a very informative table on the [comparison of regular-expression engines wiki](https://en.wikipedia.org/wiki/Comparison_of_regular-expression_engines) page. Python has two major implementations which are the built in [re]( https://docs.python.org/3/library/re.html) and the [regex]( https://pypi.org/project/regex/) library. The main implementation in python is the re library which provides regular expression matching operations similar to those found in perl. The regular expression syntax is almost the same between python in perl however the usage in perl is quite different. It is more compact which makes it more unreadable. There are even differences in regular expressions between Python 2 and 3 depending on which flags are used. Python2 regexes handle ASCII strings while Python 3 handle unicode strings.Both patterns and strings to be searched can be Unicode strings as well as 8-bit strings. However, Unicode strings and 8-bit strings cannot be mixed. Regular expressions use the backslash character `\` to indicate special forms or to allow special characters to be used without invoking their special meaning. However, in Java regular expressions are written as strings in source code and all backslashes must be doubled which harms the readability. Lua uses a simplified, limited dialect that can be bound to a more powerful library like PCRE or an alternative parser like Lpeg. Java and Lua do not allow recursion and this makes the Python implementation that much more efficient. PHP also uses the PCRE library and has the POSIX-compatible regex engine. Grep, vim and perl regexes differ in how to handle things like ( ) for grouping / capturing a pattern for back referencing in search & replace. IIRC, Perl uses them straight while grep and bim require them to be escaped. There are many different implementations of regular expressions but for the most part they are similar.

## Can all formal languages be encoded as regular expressions?
A formal language consists of words whose letters are taken from an alphabet and are well-formed according to a specific set of  rules. These are designed for use in situations in which natural language is unsuitable, as for example in mathematics, logic or computer programming. The symbols and formulas of such languages stand in precisely specified syntactic and semantic relations to one another. A regular expression on the other hand is a sequence of characters that specify a search patter. A formal language that can be defined by a regular expression, in the strict sense in theoretical computer science is known as a regular language. It is clear that every formal language  that can be recognized by a DFA can also be recognized by a NFA.
