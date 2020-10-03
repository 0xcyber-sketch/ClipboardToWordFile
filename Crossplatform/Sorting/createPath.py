#!/usr/bin/env python

from os import path

file = "path.txt"


# Creates an empty txt file called path.txt. In same directory as the file
def makePath():
    with open(file, "w") as f:
        f.write("")
        f.close()

# Open the path.txt and reads it data
def openPath():
    with open(file, "r") as f:
        data = f.read()
        f.close()

    return data

#Updates the path.txt file
def updatePath(newpath):
    with open(file, "a") as f:
        f.write(newpath)
        f.close()
