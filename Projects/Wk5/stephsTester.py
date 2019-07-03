import time
import math
import string
import re
def main():
   
    #asking for phrase to encrypt
    phrase = input("Enter the phrase to encrypt and decrypt: ")
    #making entire phrase capitalized
    CapPhrase = phrase.upper()
    #loop to remove special chars if any are present
    for k in CapPhrase.split("\n"):
        noChars = " ".join(re.findall(r"[a-zA-Z0-9]+", k))
    #string to use to replace phrase being encrypted
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    #place holders for variables being used later in program
    encoded = ""
    decoded = ""
    #loops to iterate over the string
    for letter in noChars:
        #managing whitespace
        if letter ==chr(32):
            encoded +=' '
        else:
            #finding the index value that corresponds with the letter position
            index = alphabet.find(letter)
            #moving index 4 spaces down alphabet and replacing with letter in that position
            substitute = (index + 4) % 26
            #rebuilding encrypted phrase adding each letter every pass in loop
            encoded += alphabet[substitute]
    #decoding for loop besically reversing what happended above
    for ch in encoded:
        #handling whitespace
        if ch ==chr(32):
            decoded += ' '
           
        else:
            #finding charactor position in alphabet
            index2 = alphabet.find(ch)
            #switching encrypted letter for decrypted
            swap = (index2 - 4) % 26
            #rebuilding phrase
            decoded += alphabet[swap]
    #printing 3 different phrases, original, encrypted, decrypted       
