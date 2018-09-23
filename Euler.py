'''The prime factors of 13195 are 5,7,13 and 29. 
%What is the largest prime factors of the number 600851475143?
% 09/22/2018'''

import math

def isPrime(num):
    factor = 1
    factorproduct = 1
    while True:
        if factorproduct >= num:
            return factor - 2
        elif num % factor == 0:
            factorproduct *= factor
        factor += 2
        
def main():
    print(isPrime(600851475143))

main()




