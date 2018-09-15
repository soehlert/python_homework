#!/usr/bin/env python3
import sys

#########
# Q1
#########
def string_to_number(x):
    """Suppose you want to determine whether an arbitrary text string can be
    converted to a number. Write a function that uses a try/except clause to solve
    this problem. Can you think of another way to solve this problem?"""
    try:
        return int(x)
    except ValueError as e:
        return e


def string_2_number(x):
    if isinstance(x, int):
        return True
    else:
        return False


string_to_number(5)
string_to_number("five")
string_to_number("5")
string_2_number(5)
string_2_number("five")
string_2_number("5")

#########
# Q2
#########
"""The input function will read a single line of text from the terminal. If you
wanted to read several lines of text, you could embed this function inside a
while loop and terminate the loop when the user of the program presses the
interrupt key (Ctrl-C under UNIX, Linux and Windows.) Write such a program, and
note its behavior when it receives the interrupt signal. Use a try/except
clause to make the program behave more gracefully."""

lines = []
while True:
    try:
        line = input("Enter text: \n")
        lines.append(line)
    except KeyboardInterrupt:
        print("\nReceived keyboard interrupt\n")
        sys.exit()
    finally:
        print(lines)
