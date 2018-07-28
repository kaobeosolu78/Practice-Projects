#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


sum_squares = sum([x**2 for x in range(0,101)])

squares_summed = (sum(range(0,101)))**2

answer = (-sum_squares+squares_summed)
print(answer)
