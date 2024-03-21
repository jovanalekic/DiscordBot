#### "Interesting" Numbers
'''
Interesting numbers are 3-or-more digit numbers that meet one or more of the following criteria:

* Any digit followed by all zeros: `100`, `90000`
* Every digit is the same number: `1111`
* The digits are sequential, incementing: `1234`
* The digits are sequential, decrementing: `4321`<sup>1</sup>
* The digits are a palindrome: `1221` or `73837`
* The digits match one of the values in the awesome_numbers array because Bob's birthday could be contained in the mileage numbers
'''

def isPalindrome(strInput):
    left = 0
    right = len(strInput)-1

    while left < right and left != right:
        
        leftChar = strInput[left:left+1]
        rightChar = strInput[right:right+1]
        
        if leftChar != rightChar:
            return False 
        
        left += 1
        right -= 1

    return True 

def checkDecrementing(strInput):
    arr = []
    
    strLength = len(strInput)
    
    if strLength > 10:
        return False 
     
    for i in range(0, strLength):
        arr.append(int(strInput[i:i+1]))
    
    for i in range(0, strLength-1):
        if arr[i] <= arr[i+1]:
            return False 
    
    
    return True 

def checkIncrementing(strInput):
    
    strLength = len(strInput)
    
    arr = []
    
    if strLength > 10:
        return False 
     
    for i in range(0, strLength):
        arr.append(int(strInput[i:i+1]))
    
    for i in range(0, strLength-1):
        if arr[i] >= arr[i+1]:
            return False 
    
    return True 

def checkAllAreSameDigit(strInput):
    firstChar = strInput[0:1]
    return all(char == firstChar for char in strInput)

def checkAllZeroFollow(strInput):
    return all(char == "0" for char in strInput[1:])

def is_interesting(number, awesome_numbers):
    strInput = str(number)
    if len(strInput) < 3:
        return 0

    if checkAllZeroFollow(strInput):
        print("ALL ZEROES FOLLOW")
        return 2
    
    if checkAllAreSameDigit(strInput):
        print("SAME DIGIT")
        return 2
    
    if checkIncrementing(strInput):
        print("INCREMENTING")
        return 2
    
    if checkDecrementing(strInput):
        print("DECREMEINTING")
        return 2 

    if isPalindrome(strInput):
        print("PALINDROME")
        return 2

    if number in awesome_numbers:
        print("NUMARRAY")
        return 2
    
    if is_interesting(number+1, awesome_numbers) or is_interesting(number+2,awesome_numbers):
        return 1
    
    return 0

num = 60001
awesomes = [1337, 60002]

print(is_interesting(num, awesomes))