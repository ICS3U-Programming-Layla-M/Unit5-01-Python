#!/usr/bin/env python3

# Created by: Layla Michel
# Created on: June 1, 2021
# This program converts Celsius to Fahrenheit using a number the user inputs

def fahrenheit():
    while True:
        # ask user to input temperature in celsius
        celsius_string = input("Enter a temperature in Celsius: ")
        try:
            # convert from string to int
            celsius_int = int(celsius_string)

            # convert from celsius to fahrenheit
            fahrenheit_temp = (9/5) * celsius_int + 32
            print("{0} °C = {1} °F". format(celsius_int, fahrenheit_temp))
            break
        except ValueError:
            # error message
            print("{} is not a valid number, try again.\
". format(celsius_string))


def main():
    # call fahrenheit function
    fahrenheit()


if __name__ == "__main__":
    main()
