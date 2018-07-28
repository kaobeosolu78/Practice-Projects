#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

number = 600851475143
factors = []

def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
        return True

for k in range(number-1):
    for i in range(number-1):
        if k*i == 600851475143 and is_prime(k) == True:
            factors.append(i)
            factors.append(k)
print (max(factors))
