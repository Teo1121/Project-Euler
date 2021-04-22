"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
i = 2
while True:
    if 600851475143 % i == 0:
        t = 600851475143/i
        for j in range(2,int(t**0.5)+1):
            if t/j == int(t/j):
                break
        if j == int(t**0.5):
            print(t)
            break
    i += 1
