#A palindromic number reads the same both ways. The largest palindrome made
#from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

def palindrome(num):
    placehold = []
    mum = str(num)

    for k in range(len(mum)):
        if k == 0 and mum[0] == mum[len(mum) - 1]:
            placehold.append(mum[k])
        elif mum[k - 1] == mum[-k]:
            placehold.append(mum[k])
        else:
            return False
    palin = int(''.join(map(str, placehold)))
    if int(palin) == num:
        return True

to_1000 = range(1000)
answer = []

for k in to_1000:
    for i in to_1000:
        if len(str(k)) == 3 and len(str(i)) == 3 and palindrome(k*i) == True:
            answer.append(k*i)

print (max(answer))
