#!/usr/bin/env python
import re


# Return true if input contains digit
def hasNumber(inputString):
    return bool(re.search(r'\d+', inputString))


# Return true if input contains bullet
def hasBullet(inputString):
    return bool(re.search(r'•', inputString))


def sorting(input):
    # Declare variables
    string = ""
    stringList = []
    newStringList = []
    # Check if the input contains digits and not bullets
    if hasNumber(input) and not (hasBullet(input)):
        # Split string into a list/array evry time there is a digigt
        stringList = re.split(r"\d+", input)
        # iterate list and add each elemt
        for i in range(len(stringList)):
            newStringList.append(str(i) + stringList[i] + "\n")
        # Reverse list to get the proper sequence
        newStringList = newStringList[::1]

        # Add each element from list to a string
        for i in range(1, len(newStringList)):
            string += newStringList[i]



    # Check if the input contains  bullets (Does the as above just looking for bullets instead of digits
    elif hasBullet(input):
        stringList = re.split(r"•", input)
        for i in range(len(stringList)):
            newStringList.append(str("•") + stringList[i] + "\n")
        newStringList = newStringList[::1]

        for i in range(1, len(newStringList)):
            string += newStringList[i]

    else:
        string = input
    #Return string
    return string
