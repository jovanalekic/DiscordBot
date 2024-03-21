def stats(ints):
    """ 
    Returns the mean, median, and standard deviation (in that order) of a 
    list of integers given as a parameter. 
    """
    output = []
    if len(ints) == 0:
        #print("input has 0 elements!")
        output = ["mean: 0", "median: 0"]
        return output
    
    totalSum = 0
    for x in ints:
        totalSum += x
    mean = totalSum / len(ints)
    
    median = -23123
    ints.sort()
    even = 0
    arrayLength = len(ints)
    
    if arrayLength%2 == 0:
        even = 1
    
    if even == 0:
        median = ints[int(arrayLength/2)]
    else:
        med1 = ints[int((arrayLength-1)/2)]
        med2 = ints[int((arrayLength-1)/2)+1]
        #print(f"med1: {med1}, med2: {med2}")
        median = (med1+med2)/2
    
    output = {"mean": mean, "median": median}
    return output

input = [15, 4, 10, 2]
output = stats(input)
# print(f"output: {output[0]}, {output[1]}")
print(output)
assert stats([15, 4, 10, 2]) == {"mean": 7.75, "median": 7.0} 
