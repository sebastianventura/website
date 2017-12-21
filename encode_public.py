#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import listdir
from os.path import isfile, join
import sys
import os

def encode(dir):
    files = [f for f in listdir(dir)]

    for file in files:
        path = join(dir, file)

        if isfile(path):
            filename, file_extension = os.path.splitext(path)

            if file_extension == '.html':
                source = open(path, "r", encoding="utf-8")
                content = source.read()
                source.close()

                target = open(path, "w", encoding="iso-8859-1")
                try:
                    target.write(content)
                except UnicodeEncodeError:
                   print("UnicodeEncodeError in " + path)
                
                target.close()
        else:
            encode(path)

def main(argv):
    encode("public")

if __name__ == "__main__":
    main([])