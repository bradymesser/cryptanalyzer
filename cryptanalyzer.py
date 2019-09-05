import sys
import operator

if len(sys.argv) != 2:
    print("Incorrect usage.  Correct usage is python3 cryptanalyzer.py inputText.txt\n")
    sys.exit()

try:
    inputFile = open(sys.argv[1],"r")
except OSError:
    print("Could not open file, exiting.")
    sys.exit()

text = inputFile.read()
frequencies = {}
doubles = {}
triples = {}
index = 0
text_iter = iter(text)

# iterate through text
for c in text:
    c = c.lower()
    #first count each occurence
    if c in frequencies:
        frequencies[c] += 1
    else:
        frequencies[c] = 1

    index += 1
    if index < len(text):
        #if the next character is the same as current character
        if text[index].lower() == c:
            if index + 1 < len(text):
                # if the next character is the same as the previous 2
                if text[index + 1].lower() == c and text[index].lower() == c:
                    if c in triples:
                        triples[c] += 1
                    else:
                        triples[c] = 1
                    
                    continue;
            if c in doubles:
                doubles[c] += 1
            else:
                doubles[c] = 1

print("Overall character occurences:")
sorted_freq = sorted(frequencies.items(), key=operator.itemgetter(1), reverse=True)
print(sorted_freq)

print("-----------------------------------")
print("Bigram occurences:")

sorted_doubles = sorted(doubles.items(), key=operator.itemgetter(1), reverse=True)
print(sorted_doubles)

print("-----------------------------------")
print("Trigram occurences:")

sorted_triples = sorted(triples.items(), key=operator.itemgetter(1), reverse=True)
print(sorted_triples)
