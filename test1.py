

print(5)
print("ASDFASDF")

print("hi:3")
print("PISS")
print("rawr")

print("sdfsf")

# creates output file if it does not exist.
# if it exists, clears output file
outputFileName = "pageNames.txt"
outputFile = open(outputFileName, "w")
outputFile.write("")
outputFile.close()

# opens file for appending new lines of text
outputFile = open(outputFileName, "a")

# opens source of the wiki page to read
sourceFileName = "wikiSource.txt"
sourceFile = open(sourceFileName, 'r', encoding='utf8', errors='ignore')


# returns the substring from the prefix to the first "\""
def returnThemeInLine(line):
  prefix = "title=\""
  return returnBetweenInLine(line, prefix, "\"")

# returns the substring from the prefix to the first "\""
def returnHRefInLine(line):
  prefix = "href=\""
  return returnBetweenInLine(line, prefix, "\"")

# returns 

def returnBetweenInLine(line, startTarget, endTarget):
  x = 0
  while x < len(line) - (len(startTarget)):
    if line[x:x+len(startTarget)] == startTarget:
      i = x + len(startTarget)
      while line[i:i+1] != endTarget:
        i += 1
      return line[x + len(startTarget):i]
    x += 1
  return "NONE"

# string array of page titles
pageTitlesAndLinks = []

# string array of source file by line
contentsByLine = sourceFile.read().split("\n")

for line in contentsByLine:
  
  if(len(line) > 150):
    continue
  
  page_title = returnThemeInLine(line)
  if page_title == "NONE":
    continue
  
  url = "https://aesthetics.fandom.com" + returnHRefInLine(line)
  #newArr = [page_title, url]
  pageTitlesAndLinks.append(url)
  

for k in pageTitlesAndLinks:
  try:
    outputFile.write(k + "\n")
  except UnicodeEncodeError:
    print("could not write \"" + k +"\"")
    continue
    
sourceFile.close()
outputFile.close()