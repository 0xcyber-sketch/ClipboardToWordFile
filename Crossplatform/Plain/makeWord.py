#!/usr/bin/env python

import docx
import os

def makeWordFile(path, clipboard):
    # Make a new docs
    d = docx.Document()

    # Change style
    style = d.styles['Normal']
    font = style.font
    font.name = 'Arial'


    # Add the string to the docs
    d.add_paragraph(clipboard)

    # Prompt user for name for new doc file
    name = input("New name for the file: ")

    # Saves the new document at the PATH
    new_path = os.path.join(path, name)
    new_path = new_path + ".docx"
    d.save(new_path)

