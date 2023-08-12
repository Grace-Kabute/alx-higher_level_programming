#!/usr/bin/python3
if __name__ == "__main__":
    """gets the number of aurguments passed and their numbers"""
import sys
argument = len(sys.argv) -1
if argument == 0:
    print("0 arguments.")
else:
    print("{} arguments:".format(argument))
    for i in range(argument):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
