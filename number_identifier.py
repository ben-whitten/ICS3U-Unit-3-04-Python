#!/usr/bin/env python3

# Created by: Ben Whitten
# Created on: October 2019
# This is a program which tells you if you number is - or +.


def main():

    # Input
    number = int(input("Input a number: "))

    # Process
    if number == 0:
        # Output
        print("")
        print("It is neither + or - (0)")
    # Process
    elif number > 0:
        # Output
        print("")
        print("It is: +")
    # Process
    elif number < 0:
        # Output
        print("")
        print("It is: -")
    # Process
    else:
        # It is impossible to get here because of the int(input) so if you do
        # here you most likely did something wrong.
        print("Error, check you number and try again.")


if __name__ == "__main__":
    main()
