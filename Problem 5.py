"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

num = 20
while True:
    for i in range(2,21):
        if num % i != 0:
            break
    if i == 20:
        print(num)
        break
    num += 20
    
