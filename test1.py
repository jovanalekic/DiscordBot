

print(5)
print("ASDFASDF")

print("hi:3")
print("PISS")
print("rawr")

print("sdfsf")

#creates and clears output file
outputFileName = "pageNames.txt"
outputFile = open(outputFileName, "w")
outputFile.write("")
outputFile.close()

outputFile = open(outputFileName, "a")

sourceFileName = "wikiSource.txt"
sourceFile = open(sourceFileName, 'r', encoding='utf8', errors='ignore')

contents = sourceFile.read()
contentsByLine = contents.split("\n")

pageArray = []

prefix = "title="

def returnThemeOfLine(line):
  x = 0
  while x < len(line) - (len(prefix)):
    if line[x:x+len(prefix)] == prefix:
      i = x + len(prefix) + 1
      while line[i:i+1] != "\"":
        i += 1
      return line[x + len(prefix)+1:i]
      x = i
    x += 1
  return "NO THEME"
    
for line in contentsByLine:
  
  if(len(line) > 150):
    continue
  
  theme = returnThemeOfLine(line)
  if theme == "NO THEME":
    continue
  
  pageArray.append(theme)
  

for k in pageArray:
  try:
    outputFile.write(k + "\n")
  except UnicodeEncodeError:
    print("could not write \"" + k +"\"")
    continue
    
sourceFile.close()
outputFile.close()