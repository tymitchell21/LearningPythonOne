from __future__ import print_function
import sys
from math import e
from decimal import *
getcontext().rounding=ROUND_FLOOR
sys.setrecursionlimit(1000)

python2 = sys.version_info[0] == 2
if python2:
	input = raw_input

def calculateE (n):
    return '%.*f' % (n, e)

def shell():
    print ("Welcome to the e calculator.  Please enter the number of digits (1 to 100) you would like e to be calculated to or enter quit to exit")

    while True:
        print (">>> ", end='')
        entry = input()
        if entry == "quit":
            break
        if not entry.isdigit():
            print("I am sorry but you did not enter a number.  Please try again.")
        else:
            print (calculateE(int(entry)))
    print ("Thank you for using the e calculator!")

if __name__ == '__main__':
    shell()