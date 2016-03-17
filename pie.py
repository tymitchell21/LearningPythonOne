from __future__ import print_function
import math, sys
from decimal import *
getcontext().rounding = ROUND_FLOOR
sys.setrecursionlimit(100000)

python2 = sys.version_info[0] == 2
if python2:
	input = raw_input

def factorial(n):
    product = 1
    for i in range(n):
        product = product * (i + 1)
    return product

def getIteratedValue(k):
    k = k+1
    getcontext().prec=k
    sum=0
    for k in range(k):
        num=factorial(6*k)*(13591409+545140134*k)
        den=factorial(3*k)*(factorial(k))**3*(640320**(3*k))
        sum += num/den
    return Decimal(sum)

def getValueOfPi(k):
    iter=getIteratedValue(k)
    den=426880*math.sqrt(10005)
    pi=Decimal(den)/iter

    return pi

def shell():
    print ("Welcome to Pi Calculator. In the shell below Enter the number of digits upto which the value of Pi should be calculated or enter quit to exit")

    while True:
        print (">>> ", end='')
        entry = input()
        if entry == "quit":
            break
        if not entry.isdigit():
            print("I am sorry but you did not enter a number.  Please try again.")
        else:
            print(getValueOfPi(int(entry)))

if __name__=='__main__':
    shell()