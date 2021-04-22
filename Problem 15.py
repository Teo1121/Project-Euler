"""Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?"""

def factorial(n):
    ret = 1
    if n > 0:
        while n > 0:
            ret *=n
            n -=1
    return ret

def binomial_coefficient(n,k):
    return (factorial(n)/(factorial(k)*factorial(n-k)))

x = 20
y = 20

print(binomial_coefficient(x+y,y))

