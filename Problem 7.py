"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""
i = 2
n = 0
while True:
    prime = True
    for j in range(2,int(i**0.5)+1):
        if i % j == 0:
            prime = False
            break
    if prime:
        n+=1

    if n == 10001:
        print(i)
        break
    i+=1
