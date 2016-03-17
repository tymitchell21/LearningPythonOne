import math, sys

def isPrime(x):
    if x==2:
        return True
    for n in range(2,x):
        if x%n==0:
            return False
    return True

def nextPrime(currentPrime):

    newPrime= currentPrime+1

    while True:
        if not isPrime(newPrime):
            newPrime+=1
        else:
            break

    return newPrime

def shell():
    ans=raw_input("Hi, I am going to show you the next prime number in order each time you ask me to.  Would you like to begin? Yes(y) or No(no) ")
    if ans=="y":
        print("The first prime number is: 1")
        currentPrime=1
        while True:
            entry=raw_input("Would you like to see the next one? Yes(y) or No(no): ")
            if entry=="quit":
                break
            elif entry=="y":
                print(nextPrime(currentPrime))
                currentPrime=nextPrime(currentPrime)
            else:
                print("I am sorry but I cannot recognize that command.  Please try again.")

if __name__=='__main__':
    shell()