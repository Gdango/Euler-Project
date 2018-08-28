2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?'''
import time
start_time = time.time()

def Divfactor(lim):
    divfactor = []
    for i in range(1,lim+1):
        divfactor.append(i)
    return divfactor

ListFactor = Divfactor(20)
i = 0
while True:
    i +=210

    for j in range(1,len(ListFactor)):
        if i % ListFactor[j] != 0:
            break
    if j == len(ListFactor)-1:
        break

elapsed_time = time.time() - st
elapsed_time = time.time() - start_time


































