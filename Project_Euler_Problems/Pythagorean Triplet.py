def pyth_triplet(a,b,c):
    if a**2+b**2==c**2 and a<b<c:#or a**2+c**2==b**2 or b**2+c**2==a**2:
        return True
    else:
        return False

to_1000 = range(0,1001)
pytha = 0
pythb = 0
pythc = 0

for a in to_1000:
    for b in to_1000:
        for c in to_1000:
            if a + b + c == 1000 and pyth_triplet(a,b,c) == True:
                pytha = a#append(a)
                pythb = b#append(b)
                pythc = c#append(c)

answer = a*b*c
