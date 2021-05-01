# Patrick Murray - G00344530

import shunt
import thompson
import argparse
import tests

# Use argeparse to allow user to run --test which runs all the tests
parser = argparse.ArgumentParser(description='Search a text file using a regular expression.')
parser.add_argument('--test', dest='command', action='store_const',
                    const='test',
                    help='run tests')

# Let args equal the args parsed from the parser
args = parser.parse_args()

# If the command in args equals test, run the tests function in tests.py
if args.command == 'test':
    tests.tests()

# This function searches through a file and returns every line which matches the regular expression
def searchFile(infix, filePath):
    try:
        # Open the file located at filePath in read mode
        with open(filePath, 'r') as reader:
            print(f"\nThe following lines match your regular expression {infix}")
            print("================================================================\n")
            # Use count to keep track of which line we are on in file
            count = 1
            # For each line in the file
            for line in reader.readlines():
                # Remove the newline character
                line = line.rstrip('\n')
                # Get the postfix of the infix regex using shunt.py
                postfix = shunt.shunt(infix)
                # Get the nfa of the postfix using thompson.py
                nfa = thompson.re_to_nfa(postfix)
                # Match the nfa to the line of the file
                match = nfa.match(line)
                # The line matches!
                if match == True:
                    # Output the line number and the line which match
                    print(f"Line {count}: {line}")
                # Increment count
                count = count + 1
    except FileNotFoundError:
        print("\nCould not find file, please try again!")
        return

# GUI for menu
keepRunning = True
# Keep running menu until keepRunning is set to false by selecting option 2 to exit
while keepRunning:
    print("\n1. Search text file using regular expression")
    print("2. Exit")
    option = input("=> ")

    # Search text file for lines matching the regular expression
    if option == "1":
        infix = input("\nEnter the regular expression: ")
        filePath = input("Enter the path to file: ")
        # Call the searchFile function and pass the regular expression and file path as parameters
        searchFile(infix, filePath)
    # Exit
    elif option == "2":
        print("Goodbye!")
        # Set keepRunning to false which stops loop from running
        keepRunning = False
    else:
        print("Invalid option entered!")

