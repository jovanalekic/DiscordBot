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

print("primes of 3:")
for x in primes(3):
  print(x)
assert primes(3) == [2]

print("primes of 11:")
for x in primes(11):
  print(x)
assert primes(11) == [2, 3, 5, 7]

print("primes of 20:")
for x in primes(20):
  print(x)
assert primes(20) == [2, 3, 5, 7, 11, 13, 17, 19]
