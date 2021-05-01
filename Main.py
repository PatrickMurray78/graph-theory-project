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

args = parser.parse_args()

if args.command == 'test':
    tests.tests()

def searchFile(infix, filePath):
    count = 1
    print(f"\nThe following lines match your regular expression {infix}")
    print("================================================================\n")
    with open(filePath, 'r') as reader:
        for line in reader.readlines():
            line = line.rstrip('\n')
            postfix = shunt.shunt(infix)
            nfa = thompson.re_to_nfa(postfix)
            match = nfa.match(line)
            if match == True:
                print(f"Line {count}: {line}")
            count = count + 1

# GUI for menu
keepRunning = True
while keepRunning:
    print("\n1. Search text file using regular expression")
    print("2. Exit")
    option = input("=> ")

    if option == "1":
        infix = input("\nEnter the regular expression: ")
        filePath = input("Enter the path to file: ")
        searchFile(infix, filePath)
    elif option == "2":
        print("Goodbye!")
        keepRunning = False
    else:
        print("Invalid option entered!")

