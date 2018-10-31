
'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
#It has to be even
#can't be prime

def isPrime(value,num):
    for i in range(3,num): #def: prime can't be evenly divisible from 2-10
        if value % i != 0:
            return True
    return False
factor = 0

while True:
    factor += 2
    if isPrime(factor, 10) == False: #if it is a prime
        break
        
print(factor)


