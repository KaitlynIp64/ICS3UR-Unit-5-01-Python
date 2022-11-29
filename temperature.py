#!/usr/bin/env python3

# Created by: Kaitlyn Ip
# Created on: Nov 2022
# This program converts temperature

import random


def fahrenheit():

    # input
    str_celsius = input("Enter a number in degrees Celsius: ")

    # process
    try:
        int_celsius = int(str_celsius)
        fahrenheit = (9 / 5) * int_celsius + 32
        print("{0}°C is equal to {1}°F.".format(int_celsius, fahrenheit))
    except ValueError:
        print("That is not a valid input.")
    # output

    print("\nDone.")


def main():
    # this function calls other functions

    # call functions
    fahrenheit()


if __name__ == "__main__":
    main()
