#!/usr/bin/python3

import time


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
mix =  "ETAOINSHRDLCUMWFGYPBVKJXQZ"

text = input("What would you like to encrypt? ")
test2 = "OMG! IT'S OVER 9000!"

intext = "" 
outtext = ""
outtext2 = "WUSZZRBZPZWKIYZZZZZZ"

print (text + " TURN IN TO!!!!")

time.sleep(1.5)

print ("\n""OMG! IT'S OVER 9000!""\n")

##################################################
time.sleep(1.5)
##################################################
#OVER 9000 Vigenere_encryption



print (outtext2)

time.sleep(1.5)
print ("Wait thats not it...")
##################################################
time.sleep(1.5)

##################################################
#Vigenere_encryption

for let in text.upper():
	if let in alphabet:
		outtext += mix[alphabet.find(let)]

	else:
		outtext += let
##################################################
# print output 
print ("\n" + outtext)
time.sleep(1)
print ("There we go :)")
