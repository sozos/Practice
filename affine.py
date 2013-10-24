#!/usr/bin/python
# MATH533 Number Theory

import re

#=======================================#
# Convert from letters to digits mod 26 #
#=======================================#
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

#========================#
# Given frequency tables #
#========================#
# Percentage occurrence of letters of the alphabet in a sample text
freqTable1 = {	'A' : 7.3,
				'B' : 0.9,
				'C' : 3.0,
				'D' : 4.4,
				'E' : 13.0,
				'F' : 2.8,
				'G' : 1.6,
				'H' : 3.5,
				'I' : 7.4,
				'J' : 0.2,
				'K' : 0.3,
				'L' : 3.5,
				'M' : 2.5,
				'N' : 7.8,
				'O' : 7.4,
				'P' : 2.7,
				'Q' : 0.3,
				'R' : 7.7,
				'S' : 6.3,
				'T' : 9.3,
				'U' : 2.7,
				'V' : 1.3,
				'W' : 1.6,
				'X' : 0.5,
				'Y' : 1.9,
				'Z' : 0.1}

# Most frequent digraphs (out of 80,000 characters of text)
freqTable2 = {	'TH' : 2161,
				'HE' : 2053,
				'IN' : 1550,
				'ER' : 1436,
				'RE' : 1280,
				'ON' : 1232,
				'AN' : 1216,
				'EN' : 1029,
				'AT' : 1019,
				'ES' : 917,
				'ED' : 890,
				'TE' : 872,
				'TI' : 865,
				'OR' : 861,
				'ST' : 823,
				'AR' : 764,
				'ND' : 761,
				'TO' : 756}

# Frequency count of trigraphs (in 80,000 character text)
freqTable3 = {	'THE' : 1717,
				'AND' : 483,
				'TIO' : 384,
				'ATI' : 287,
				'FOR' : 284,
				'THA' : 255,
				'TER' : 232,
				'RES' : 219,
				'ERE' : 212,
				'CON' : 206,
				'TED' : 187,
				'COM' : 185}

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

def calcFrequencies(text, blockSize):
	textFreq = dict()
	for i in range(blockSize, len(text)+1):
		key = text[i-blockSize:i]
		if (key not in textFreq):
			textFreq[key] = 0 # Add new key
		textFreq[key] += 1 # Increase count
	return textFreq

def getHighestCount(lookUpDict):
	highestKey = None
	highestCount = 0
	for key in lookUpDict.iterkeys():
		if (lookUpDict[key] > highestCount):
			highestKey = key
			highestCount = lookUpDict[key]
	return [highestKey, highestCount]

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

# a = 17
# b = 9
# HW = "A guy meets a hooker in a bar. She says, 'This is your lucky night. I will do absolutely anything you want for three hundred dollars, as long as you can say it in three words.' The guy pulled out his wallet, lays down three hundred dollar bills on the bar, and says, slowly: 'Paint my house.'"
# print HW
# plainText = list(letterToDigit[item] for item in re.sub("[^a-zA-Z]", "", HW).replace(" ","").upper())
# cipherText = list(affine(p, a, b) for p in plainText)
# output = "".join(list(digitToLetter[item] for item in cipherText))
# print output
# # bruteForce(output)

# Q2 = "PXPXKXENVDRUXVTNLXHYMXGMAXYKXJNXGVRFXMAHWGXXWLEHGZXKVBIAXKMXQM"
# Q2Numbers = list(letterToDigit[item] for item in Q2)
# Q2Decode = list(affine(p, 1, -19) for p in Q2Numbers)
# Q2Decoded = list(digitToLetter[item] for item in Q2Decode)
# print Q2Numbers, "\n"
# print Q2Decode, "\n"
# print Q2Decoded, "\n"

# Q4 = "QAOOYQQEVHEQV"
# Q4Numbers = list(letterToDigit[item] for item in Q4)
# Q4Decode = list(affine(p, 5, -19) for p in Q4Numbers)
# Q4Decoded = list(digitToLetter[item] for item in Q4Decode)
# print Q4Numbers, "\n"
# print Q4Decode, "\n"
# print Q4Decoded, "\n"
# # bruteForce(Q4)

# LastQn = "RIPGZRCUAEVXAHZIPRCCLJAWSCUPWVMWVMSLCIPIVXZPECUWVMWVMSIPALWVFPIWUCUURAEZWVMVSERIWLZAZRCNPWMRZCUZUZIPAHILLSLCIPWZUPIXWIVSEURWVCSIPALWVIUFPWSCLCUUMCQPCSCWJCILLFPIWUCUZRWVC"
# print LastQn
# bruteForce(LastQn)

# block1Freq = calcFrequencies(Q2,1)
# block2Freq = calcFrequencies(Q2,2)
# block3Freq = calcFrequencies(Q2,3)
# print "Block size 1:\n", block1Freq, "\n", getHighestCount(block1Freq), "\n"
# print "Block size 2:\n", block2Freq, "\n", getHighestCount(block2Freq), "\n"
# print "Block size 3:\n", block3Freq, "\n", getHighestCount(block3Freq), "\n"
# print "1 letter freq:\n", freqTable1, "\n", getHighestCount(freqTable1), "\n"
# print "2 letter freq:\n", freqTable2, "\n", getHighestCount(freqTable2), "\n"
# print "3 letter freq:\n", freqTable3, "\n", getHighestCount(freqTable3), "\n"