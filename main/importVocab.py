#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  importVocab.py
#  
#  Copyright 2020 Victor <victor@victor-linux>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.

outputVocab = open("vocab.txt", "a")
inputVocab = open("rawVocab.txt", "r")

inputLines = inputVocab.read().split("\n")
for i in range(len(inputLines)):
	try:
		if not inputLines[i] or inputLines[i] == " ":
			inputLines.pop(i)
	except:
		print(str(i) + " was deletus")
		
print(inputLines)
for i in range(len(inputLines)):
	outputVocab.write(inputLines[i] + "\n")

print("Done!")
