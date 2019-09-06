import sys
import operator

if len(sys.argv) != 2:
    print("Incorrect usage.  Correct usage is python3 HW1code_Brady_Messer.py inputText.txt\n")
    sys.exit()

try:
    inputFile = open(sys.argv[1],"r")
except OSError:
    print("Could not open file, exiting.")
    sys.exit()
chars = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
text = inputFile.read()
frequencies = {}
doubles = {}
triples = {}
index = 0
text_iter = iter(text)

# iterate through text
for c in text:
    c = c.lower()
    if c in chars:
        #first count each occurence
        if c in frequencies:
            frequencies[c] += 1
        else:
            frequencies[c] = 1

for c in text_iter:
    c = c.lower()
    if c in chars:
        index += 1
        if index < len(text):
            #if the next character is the same as current character
            if text[index].lower() in chars:
                if index + 1 < len(text):
                    # if the next character is a letter we have a trigram
                    if text[index + 1].lower() in chars:
                        if c+text[index].lower()+text[index+1].lower() in triples:
                            triples[c+text[index].lower()+text[index+1].lower()] += 1
                        else:
                            triples[c+text[index].lower()+text[index+1].lower()] = 1
                # if the next character is a letter we have a bigram
                if c+text[index].lower() in doubles:
                    doubles[c+text[index].lower()] += 1
                else:
                    doubles[c+text[index].lower()] = 1

print("Overall character occurences:")
sorted_freq = sorted(frequencies.items(), key=operator.itemgetter(1), reverse=True)
for char in sorted_freq:
    print(char)

print("-----------------------------------")
print("Bigram occurences:")

sorted_doubles = sorted(doubles.items(), key=operator.itemgetter(1), reverse=True)
for char in range(30):
    if char >= len(sorted_doubles):
        break
    print(sorted_doubles[char])

print("-----------------------------------")
print("Trigram occurences:")

sorted_triples = sorted(triples.items(), key=operator.itemgetter(1), reverse=True)
for char in range(30):
    if char >= len(sorted_triples):
        break
    print(sorted_triples[char])

output = open("output.txt", "w")
output.write("Overall character occurences:\n")
for freq in sorted_freq:
    output.write(freq[0])
    output.write(": ")
    output.write(str(freq[1]))
    output.write("\n")

output.write("--------------------\nBigram occurences:\n")
for char in range(30):
    if char >= len(sorted_doubles):
        break
    output.write(str(sorted_doubles[char]))
    output.write("\n")

output.write("--------------------\nTrigram occurences:\n")
for char in range(30):
    if char >= len(sorted_triples):
        break
    output.write(str(sorted_triples[char]))
    output.write("\n")
