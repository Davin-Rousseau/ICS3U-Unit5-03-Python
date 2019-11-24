#!/usr/bin/env python3

# Created by: Davin Rousseau
# Created on: November 2019
# This program uses return values
# To return a level mark into a percentage


def percentage(level):
    # calculate percentage mark

    percentage = None

    if level == "4+":
        percentage = 97
    elif level == "4":
        percentage = 90.5
    elif level == "4-":
        percentage = 83
    elif level == "3+":
        percentage = 78
    elif level == "3":
        percentage = 74.5
    elif level == "3-":
        percentage = 71
    elif level == "2+":
        percentage = 68
    elif level == "2":
        percentage = 64.5
    elif level == "2-":
        percentage = 61
    elif level == "1+":
        percentage = 58
    elif level == "1":
        percentage = 54.5
    elif level == "1-":
        percentage = 51
    elif (level == "R" or level == "N/A"):
        percentage = 0
    else:
        percentage = -1

    return percentage


def main():
    # This function gets grade level and calls percentage
    # function

    # input
    grade_level = str(input("Enter your grade level in number form(4+): "))

    print("")

    # call functions
    percentage_mark = percentage(grade_level)

    if percentage_mark == -1:
        print("Invalid input")
    else:
        print("Your percentage mark is: {}%".format(percentage_mark))


if __name__ == "__main__":
    main()
