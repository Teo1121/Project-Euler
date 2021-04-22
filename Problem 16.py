"""215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?"""

digits = str(2**1000)

Sum = 0

for i in digits:
    Sum += int(i)

print(Sum)
