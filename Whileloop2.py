#!/usr/bin/env python3

# Created by: Manuel Garcia Yuste
# Created on : October 2019
# This program do a while loop


def main():
    # variables
    answer = 1
    counter = 1

    # input
    number = int(input("Enter a number to loop it and add its results: "))

    # process & output
    while counter <= number:
        answer = answer * counter
        counter = counter + 1
    print("The multiplication of all the numbers is {}".format(answer))


if __name__ == "__main__":
    main()
