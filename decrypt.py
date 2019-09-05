import sys
import operator

if len(sys.argv) != 2:
    print("Incorrect usage.  Correct usage is python3 decrypt.py inputText.txt\n")
    sys.exit()

try:
    inputFile = open(sys.argv[1],"r")
except OSError:
    print("Could not open file, exiting.")
    sys.exit()

text = inputFile.read()
frequencies = {}

for c in text:
    c = c.lower()
    #first count each occurence
    if c in frequencies:
        frequencies[c] += 1
    else:
        frequencies[c] = 1

print("Overall character occurences:")
sorted_freq = sorted(frequencies.items(), key=operator.itemgetter(1), reverse=True)
sum = 0
for char in sorted_freq:
    sum += char[1]
print("Total characters: " + str(sum))

for char in sorted_freq:
    print(char[0] + ": " + str(char[1]) + " freq: " + str((char[1]/sum) * 100))
