def recF(num,sum):
    if(num<10):
        return sum+num
    else:
        return recF(num//10,sum+num%10)
n =int(input())
for i in range(n):
    print(recF(int(input()),0))
