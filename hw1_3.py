def decreasing_digits(n):
	""" 
 	Returns the number of integers from 1 to $n$ (inclusive) 
	that have all digits in decreasing order, where $n$ is
	given as a parameter. 
	"""
	# YOUR CODE HERE
	# number output = 0
	# number x copies input 
	# for x iterations 
	#  get num of digits 
	#  run number of digits iterations check each one less than the next
	#  continue if false 
	#  output++ at end
	output = 0
	
	for i in range(1, n+1):
		intVersion = i
		stringVersion = str(intVersion)
		isYes = 1
		while len(stringVersion) >= 2:
			dig1 = stringVersion[0:1]
			dig2 = stringVersion[1:2]
			int1 = int(dig1)
			int2 = int(dig2)
			print(f"comparing int1: {int1} with int2: {int2}")
			if int2 >= int1:
				print(f"this is not a number that is decreasing digits")
				isYes = 0
				break
			intVersion = int(intVersion / 10)
			stringVersion = str(intVersion)
		if isYes == 1:
			print(f"all decreasing number found!")
			output += 1

	return output

n = 30
print(f"decreasing digits of ints under {n}")
output = decreasing_digits(n)
print(f"output: {output}")