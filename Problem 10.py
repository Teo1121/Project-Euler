"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""
i = 2
s = 0
while i < 2_000_000:
    prime = True
    for j in range(2,int(i**0.5)+1):
        if i % j == 0:
            prime = False
            break
    if prime:
        s+=i

    i+=1

print(s)
