import math,sys

python2 = sys.version_info[0] == 2
if python2:
	input = raw_input

def calculateFibSeq(n):
    n=n-2
    x=0
    y=1
    seq = [0,1]
    for k in range(n):
        sum = x+y
        seq.append(sum)
        x=y
        y=sum
    return seq


def shell():
    print ("Welcome to the Fibonacci Sequence Calculator.  Please enter the number you would like to be the nth digit that it is calculated to.")

    while True:
        entry = input(">>> ")
        if entry == "quit":
            break
        if not entry.isdigit():
            print ("I'm sorry you did not enter a digit.  Please try again.")
        else:
            print (calculateFibSeq(int(entry)))

if __name__=='__main__':
    shell()