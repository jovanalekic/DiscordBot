curI = 0

def getGPA(arg, si):
    global curI
    output = ""
    start = getNextIntIndex(arg, si)
    #print("start finding gpa at " + arg[si: si+1])
    end = start+1
    if arg[end:end+1] == ".":
        end = getNextNonIntIndex(arg, end)
    output = arg[start:end]
    curI += end-si
    #print(f"end of gpa at {curI} \"" + arg[end: end+1] + f"\", content length = {len(arg)}")
    return output


def getMajor(arg, si):
    global curI
    output = ""
    start = getNextIntIndex(arg, si)
    endIndex = start+3
    output = arg[start:endIndex]
    curI += endIndex-si
    #print(f"getMajor starting at {arg[start:start+1]} and ends at {arg[curI:curI+1]}")
    return output

def getLastName(arg, si):
    global curI
    output = ""
    start = getNextUppercaseIndex(arg, si)
    #print("starting at " + arg[si: si+1])
    end = start
    end = getNextNonLetterIndex(arg, start+1)
    #print("nextNonLetter at " + arg[i1: i1+1])\
    output = arg[start:end]
    curI += end-si
    return output

def getFirstName(arg, si):
    global curI
    output = ""
    start = getNextUppercaseIndex(arg, si) 
    end1 = getNextNonLetterIndex(arg, start+1) 
    end2 = getNextUppercaseIndex(arg, start+1) 
    end = min(end1,end2) #first non-letter/non-uppercase
    output = arg[start:end]
    curI += end-si
    return output

def getNetID(arg, si):
    global curI
    output = ""
    start = getNextLetterIndex(arg, si)
    i = start
    i = getNextNonLetterIndex(arg, i)
    i = getNextNonIntIndex(arg, i)
    output = arg[start:i]
    curI += i-si
    #print(f"curI = {curI}")
    return output

def getNextUppercaseIndex(arg, si):
    for i in range(si,len(arg)):
        c = arg[i:i+1]
        if c.isalpha() and not c.islower():
            return i
    return len(arg)

def getNextNonIntIndex(arg, si):
    for i in range(si+1,len(arg)):
        if not arg[i:i+1].isnumeric():
            #print(f"non int detected: \"{arg[i:i+1]}\" at index {i} at {arg[i-5:i+5]}\n")
            return i
    return len(arg)

def getNextIntIndex(arg, si):
    for i in range(si,len(arg)):
        if arg[i:i+1].isnumeric():
            return i
    return len(arg)

def getNextNonLetterIndex(arg, si):
    for i in range(si,len(arg)):
        if not arg[i:i+1].isalpha():
            return i
    return len(arg)

def getNextLetterIndex(arg, si):
    for i in range(si,len(arg)):
        if arg[i:i+1].isalpha():
            return i
    return len(arg)

def hasAlphabet(input):
    return any(c.isalpha() for c in input)

def hasNumbers(input):
    return any(c.isdigit() for c in input)

def reformat_student_info(filename):
    global curI
    file = open(filename, "r")
    contents = file.read()
    
    output = "" 
    #print(f"length: {len(contents)}")

    while(curI <= len(contents)):
        prevCurI = curI
        netID = getNetID(contents, curI)
        # curI += len(netID)
        firstName = getFirstName(contents, curI)
        # curI += len(firstName)
        lastName = getLastName(contents, curI)
        # curI += len(lastName)
        major = getMajor(contents, curI)
        # curI += len(major)
        gpa = getGPA(contents, curI)
        # curI += len(gpa)
        
        #print(f"netID: \"{netID}\"")
        #print(f"firstName: \"{firstName}\"")
        #print(f"lastName: \"{lastName}\"")
        #print(f"major: \"{major}\"")
        #print(f"gpa: \"{gpa}\"")
        
        
        output += netID + ", "
        output += firstName + " " + lastName + ", "
        output += major + ", "
        
        if len(gpa) == 1:
            output += gpa + ".0\n"
        else:
            output += gpa + "\n"
        
        #print(f"\ncurrent output: \n{output}")
        restOfInfo = contents[curI:]
        #print(f"--------\nrest of info: \"{contents[curI:]}\"\n--------\n")
        
        if not (hasAlphabet(restOfInfo) or hasNumbers(restOfInfo)):
            break
        
        if(curI <= prevCurI):
            break
        
        if curI > len(contents):
            break 
           
    fileName = "studentInfoReformatted.txt"

    # Open the file in write mode and write the string
    with open(fileName, 'w') as file:
        file.write(output[0:len(output)-1])

# go until finding a number and then a non-number in a row, this is the end of the netID
# go until finding a letter, this is the first part of the first name
    # the last lowercase letter before a non-lowercase letter is the last part of the first name 
# find next capital letter, which is hte first letter of last name
print(reformat_student_info("hwFile.txt"))