sourceFileName = "pageNamesBlacklistRaw.txt"
sourceFile = open(sourceFileName, 'r')
 
contentsByLine = sourceFile.read().split("\n")

outputArr = []

# returns the substring from the start of the line to the first " " or "\n" it encounters 
def returnOnlyLinkInLine(line):
  print("cleaning \""+ line + "\"")
  index = 0
  curChar = line[index:index+1]
  while(curChar != " " and curChar != "\n" and index < len(line)):
    index += 1
    curChar = line[index:index+1]
  print("output: \"" + line[0:index] + "\"")
  return line[0:index]

for line in contentsByLine:
  cleanedLine = returnOnlyLinkInLine(line)
  outputArr.append(cleanedLine)

print("\noutputArr\n")
for line in outputArr:
  print("\""+line+"\"")
  
outputFileName = "pageNamesBlacklistCleaned.txt"

outputFile = open(outputFileName, "w")
outputFile.write("")
outputFile.close()

outputFile = open(outputFileName, "a")

for k in outputArr:
    outputFile.write(k + "\n")