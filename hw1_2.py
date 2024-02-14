def primes(n):
	# """Returns all prime numbers from 2 to n (excluding n) """
	# YOUR CODE HERE
	# new number array
	# for loop % every number below half of every number below n
		# if any % == 0, continue
		# add to array if for loop ends 
	  # fuck time efficiency
	primes = []
	for i in range (2, n):
		isPrime = 1
		for k in range (2, i):
			if i%k == 0:
				isPrime = 0
				continue
		if(isPrime == 1):
			primes.append(i)
	return primes

def factor(n):
	"""Return all the prime factors of n."""
	# YOUR CODE HERE
	# find factor f of n
		# if prime, add to array
		# if not prime, find factors of f
		# recursively add factors of f to array
	factors = []
	possibleFactors = primes(n)

	print(f"possible primes of :{n}")
	for x in possibleFactors:
		print(x)
 
	curLeft = n
	while (curLeft not in possibleFactors) and (curLeft > 1):
		isPrime = 1
		print(f"{curLeft} is not in possibleFactors, running iteration")
		for x in possibleFactors:
			if curLeft%x == 0:
				isPrime = 0
				print(f"{x} is a factor of {curLeft}")
				factors.append(x)
				curLeft = int(curLeft/x)
				continue
		if(isPrime == 1):
			break
	if(curLeft != 1):	
		factors.append(curLeft)
	return factors

n = 41
result = factor(n)
print(f"factors of {n}:")
for x in result:
	print(x)
print("done")