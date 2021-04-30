#!/usr/bin/python3

import time


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
mix =  "ETAOINSHRDLCUMWFGYPBVKJXQZ"

text = input("What would you like to encrypt? ").upper()
test2 = "NWY BHI HWYO!"

intext = "" 
outtext = ""
outtext2 = ""

print (text + " TURN IN TO!!!!")

time.sleep(1.5)

print ("\n""NWY BHI HWYO!""\n")

##################################################
time.sleep(1.5)
##################################################
#OVER 9000 Vigenere_encryption



print ("FOR THE HORD!")

time.sleep(1.5)
print ("Wait thats not it...")
##################################################
time.sleep(1.5)
##################################################
#Vigenere_encryption

for let in text:
	if let in alphabet:
		outtext += alphabet[mix.find(let)]

	else:
		outtext += let
##################################################
# print output 
print ("\n" + outtext)
time.sleep(1)
print ("There we go :)")