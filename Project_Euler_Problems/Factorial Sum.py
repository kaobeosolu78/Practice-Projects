def factorial(n):
    fact = 1
    for k in range(0,n+1):
        if n == 0:
            return 1
        elif k != n:
            fact *= (n-k)
    return (fact)

fact_100 = str(factorial(100))
answer = 0
hold = []
for k in fact_100:
    hold.append(int(k))
for k in hold:
    answer += k
print (answer)
