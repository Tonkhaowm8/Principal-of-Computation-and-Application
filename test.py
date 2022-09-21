from array import array


sentence = input("Enter number: ")
newSentence = sentence.split()
for j in range(0, len(newSentence) - 1):
    if "" in newSentence[j] and newSentence[j] == "$":
        newSentence[j] = "z"

print(newSentence)


sentence = input("Enter sentence: ")
newSentence = sentence.split()
for i in newSentence:
    wordList = list(i)
    if wordList[-1] == "s" or wordList[-1] == "$":
        wordList[-1] = "z"
    print("".join(wordList))