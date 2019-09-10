import sys
import operator
import random

alphabet = {'x':'e','t':'n','j':'t','m':'a','p':'h','c':'o','r':'s','b':'i','n':'d','v':'r','g':'l','w':'g','y':'w','a':'c','l':'m','i':'f','u':'u','h':'k','f':'b','e':'y','q':'p','d':'v','o':'z','k':'q','s':'j','z':'x'}
chars = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}


try:
    inputFile = open(sys.argv[1],"r")
except OSError:
    print("Could not open file, exiting.")
    sys.exit()

text = inputFile.read()
output = open("dcOut.txt", "w")

for char in text:
    if char in chars:
        output.write(alphabet[char])
        sys.stdout.write(alphabet[char])
    else:
        output.write(char)
        sys.stdout.write(char)
