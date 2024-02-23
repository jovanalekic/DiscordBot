def one_triples(ints):
    """ 
    Returns all triples in a list of integers that sum to zero. 
    The list of integers is given as a parameter. 
    Assumes the list will not contain any duplicates, and a triple 
    should not use the same number more than once.
    """
    # YOUR CODE HERE
    # fuck time efficiency just manually check every permutation of 3 elements 
    # if it adds to one, sort the 3 and add that array to output array 
    output = []
    
    # literally impossible to find a triple
    if(len(ints) < 3):
        return output
    
    ints.sort() 
     
    for i in range(0, len(ints) - 2):
        for k in range (i+1, len(ints)-1):
            for m in range (k+1, len(ints)):
                int1 = ints[i]
                int2 = ints[k]
                int3 = ints[m]
                sum = int1 + int2 + int3
                #print(f"checking {int1} + {int2} + {int3} = {sum}")
                if sum == 1:
                    #print(f"triple found! {int1},{int2},{int3},")
                    newTriple = [int1,int2,int3]
                    newTriple.sort()
                    newTuple = (newTriple[0],newTriple[1],newTriple[2])
                    output.append(newTuple)
    
    return output
    
input1 = [1, 2, 3, 0, -2, 8, -7]
input2 = [-3, 1, 4, 3]
output = one_triples(input2)

print(f"triples found: {len(output)}")
for x in output:
    print(output)
print("end of triples found")


inputTest = [-3, 1, 4, 3]
if one_triples(inputTest) == [(-3, 1, 3)]:
    print("shit is working")
else:
    print("shit isnt formatted right or something")

assert one_triples(inputTest) == [(-3, 1, 3)]
