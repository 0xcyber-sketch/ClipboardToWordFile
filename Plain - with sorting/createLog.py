#!/usr/bin/env python
from os import path
file = "path.txt"
def makeLog():


    with open(file, "w") as f:
        f.write("")
        f.close()

def openLog():
    with open(file, "r") as f:
        data = f.read()
        f.close()

    return data

def updateLog(newpath):
    with open(file, "a") as f:
        f.write(newpath)
        f.close()