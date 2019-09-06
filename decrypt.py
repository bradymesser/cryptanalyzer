import sys
import operator
import random

def getMatches(char, freq, actual):
    # print("Matches for " + char)
    matches = list()
    for item in actual:
        if abs(actual[item] - freq) <= 2:
            matches.append(item)
    return matches

if len(sys.argv) != 2:
    print("Incorrect usage.  Correct usage is python3 decrypt.py inputText.txt\n")
    sys.exit()

try:
    inputFile = open(sys.argv[1],"r")
except OSError:
    print("Could not open file, exiting.")
    sys.exit()

chars = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
actualFreq = {'e':12.7,'t':9.1,'a':8.2,'o':7.5,'i':7.0,'n':6.7,'s':6.3,'h':6.1,'r':6.0,'d':4.3,'l':4.0,'c':2.8,'u':2.8,'m':2.4,'w':2.4,'f':2.2,'g':2.0,'y':2.0,'p':1.9,'b':1.5,'v':1.0,'k':0.8,'j':0.15,'x':0.15,'q':0.10,'z':0.07}
text = inputFile.read()
characters = {}
frequencies = {}
possibleMatches = {}
for c in text:
    c = c.lower()
    if c in chars:
        #first count each occurence
        if c in characters:
            characters[c] += 1
        else:
            characters[c] = 1

print("Overall character occurences:")
sorted_chars = sorted(characters.items(), key=operator.itemgetter(1), reverse=True)
sum = 0
for char in sorted_chars:
    sum += char[1]
print("Total characters: " + str(sum))

for char in sorted_chars:
    frequencies[char[0]] = (char[1]/sum) * 100
    # print(char[0] + ": " + str(char[1]) + " freq: " + str((char[1]/sum) * 100))
    # print(str(char[0]) + " " + str(frequencies[char[0]]))
    # print(frequencies[char[0]])

for char in frequencies:
    possibleMatches[char] = getMatches(char, frequencies[char], actualFreq)
    print(str(char) + " " + str(possibleMatches[char]))

# for char in text:
#     if char not in chars:
#         sys.stdout.write("\n")
#     else:
#         for match in possibleMatches[char]:
#             sys.stdout.write(match + "/")
#         sys.stdout.write("(" + char + ")")
#         sys.stdout.write(":")

usedMatches = {}
alphabetList = list()
j = 0
for i in range(10):
    for char in text:
        if char in chars:
            if char not in usedMatches.keys():
                choice = random.choice(possibleMatches[char])
                while choice in usedMatches.values():
                    choice = random.choice(possibleMatches[char])
                    j+=1
                    if j >= 26:
                        print("please write better code you suck at programming")
                        choice = possibleMatches[char][0]
                        j = 0
                        break
                # if choice not in usedMatches.values():
                usedMatches[char] = choice
    alphabetList.append(usedMatches.copy())
    usedMatches.clear()

print("Alphabets generated.")
# for alphabet in alphabetList:
#     for char in text:
#         if char in chars:
#             sys.stdout.write(alphabet[char])
#         else:
#             sys.stdout.write(char)
#     sys.stdout.write("******************************\n")

output = open("dcOut.txt", "w")

for alphabet in alphabetList:
    for char in text:
        if char in chars:
            output.write(alphabet[char])
        else:
            output.write(char)
    output.write(str(alphabet))
    output.write("\n")
    output.write("******************************\n")
