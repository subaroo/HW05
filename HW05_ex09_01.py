#!/usr/bin/env python
# HW05_ex09_01.py

# Write a program that reads words.txt and prints only the 
# words with more than 20 characters (not counting whitespace).
##############################################################################
# Imports



# Body
def read_text_file():
	fin = open('words.txt')
	for line in fin:
		word = line.strip()
		if len(word) > 19:
			print word



##############################################################################
def main():
    read_text_file()

if __name__ == '__main__':
    main()
