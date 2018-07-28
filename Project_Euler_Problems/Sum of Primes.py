def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
        return True

primes = []
count = 0
while len(primes) <= 2000000:
    count += 1
    if is_prime(count) == True:
         primes.append(count)
    else:
        continue

print (sum(primes[2000000]))