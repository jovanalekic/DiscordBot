def lowercaseFirstLetter(input):
  return input.casefold()

def reverse_sorted_words(filename):
  file = open(filename, "r")
  fileContents = file.read()
  print(fileContents)
  wordList1 = fileContents.split(",")
  print(wordList1)
  wordList2 = []
  for word in wordList1:
    if(len(word.split("\n"))>1):
      for splitWord in word.split("\n"):
        wordList2.append(splitWord)
    else:
      wordList2.append(word)
  print(wordList2)
  print("sorting")
  wordList2.sort(reverse = True, key = lowercaseFirstLetter)
  print(wordList2)
  return wordList2

print(reverse_sorted_words("hwFile.txt"))
  