'''
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''

def isFib(fib1, fib2, sumnum): #solving recursively
    fib = fib1 + fib2
    if (fib % 2) == 0: #only summing even value
        sumnum += fib
        
    return [fib, fib2, sumnum]


def compute(value):
    num = isFib(1, 2, 2)
    i = 3
    while num[0] <= value:
        i += 1
        num = isFib(num[1], num[0], num[2])

    return num[2]


print(compute(4000000))

