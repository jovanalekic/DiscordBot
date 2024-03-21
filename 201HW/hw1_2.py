def primes(n):
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

n = 42
result = factor(n)
print(f"factors of {n}:")
for x in result:
	print(x)
print("done")