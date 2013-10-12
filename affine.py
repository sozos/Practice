#!/usr/bin/python
# MATH533 Number Theory

import re

# Convert from letters to digits mod 26
letterToDigit = {'A' : 1,
				 'B' : 2,
				 'C' : 3,
				 'D' : 4,
				 'E' : 5,
				 'F' : 6,
				 'G' : 7,
				 'H' : 8,
				 'I' : 9,
				 'J' : 10,
				 'K' : 11,
				 'L' : 12,
				 'M' : 13,
				 'N' : 14,
				 'O' : 15,
				 'P' : 16,
				 'Q' : 17,
				 'R' : 18,
				 'S' : 19,
				 'T' : 20,
				 'U' : 21,
				 'V' : 22,
				 'W' : 23,
				 'X' : 24,
				 'Y' : 25,
				 'Z' : 0}

# Convert from digits mod 26 to letters
digitToLetter = dict(reversed(item) for item in letterToDigit.items())

# Check conversions between letter and digit
# print letterToDigit.items()
# print digitToLetter.items()

# Affine cipher/code:
# c = ap + b (mod 26)
# c = cipher text
# p = plain text
# a, b fixed constants. (a,26) = 1
def affine(p, a, b):
	return ((a*p + b) % 26)

def calcMultInv(a):
	for i in range(1, 26):
		if ((a*i) % 26 == 1):
			return i

def bruteForce(fullCodedText):
	for a in possibleA:
		for b in possibleB:
			print "(a,b):", a, b
			output = ""
			for i in range(0, len(fullCodedText)):
				c = letterToDigit[fullCodedText[i]]
				output += digitToLetter[(multInv[a]*(c - b)) % 26]
			# print "".join(digitToLetter[(multInv[a]*(letterToDigit[fullCodedText[i]] - b)) % 26] for i in range(0, len(fullCodedText)))
			print output

# Since (a,26) = 1, we only have phi(26) options for a
# i.e. a = 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25
# b = any integer in [0,25]
# e.g. a = 1 := Shift Chipher
# e.g. a = 1, b = 3 := Caeser's Cipher
possibleA = (1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25)
possibleB = range(0, 26)
multInv = dict(zip(possibleA, (calcMultInv(item) for item in possibleA)))

#=========#
# Testing #
#=========#

# a = 1
# b = 3
# rawInput = "julius dont cross the rubicon the bridge is out" #raw_input()
# noSpaces = rawInput.replace(" ", "")
# upperInput = list(noSpaces.upper())
# plainText = list(letterToDigit[item] for item in upperInput)
# cipherText = list(affine(p, a, b) for p in plainText)
# output = list(digitToLetter[item] for item in cipherText)

# print "\nRaw Input: \n", rawInput
# print "\nUppercased Input: \n", upperInput
# print "\nPlain Input: \n", plainText
# print "\nCipher Input: \n", cipherText
# print "\nOutput: \n", output
# print "\nPretty Output: \n", "".join(output)

# print multInv
# bruteInput = "".join(output)
# bruteForce(bruteInput)

#==========#
# Homework #
#==========#
# ~50 word text, coded in affine cipher of choice
# Text (59 words):
# A guy meets a hooker in a bar. She says, 'This is your lucky night. I will do absolutely anything you want for three hundred dollars, as long as you can say it in three words.' The guy pulled out his wallet, lays down three hundred dollar bills on the bar, and says, slowly: 'Paint my house.'
# Modified from Source: http://listverse.com/2007/09/16/listverse-top-50-jokes/

a = 17
b = 9
HW = "A guy meets a hooker in a bar. She says, 'This is your lucky night. I will do absolutely anything you want for three hundred dollars, as long as you can say it in three words.' The guy pulled out his wallet, lays down three hundred dollar bills on the bar, and says, slowly: 'Paint my house.'"
print HW
plainText = list(letterToDigit[item] for item in re.sub("[^a-zA-Z]", "", HW).replace(" ","").upper())
cipherText = list(affine(p, a, b) for p in plainText)
output = "".join(list(digitToLetter[item] for item in cipherText))
print output
# bruteForce(output)