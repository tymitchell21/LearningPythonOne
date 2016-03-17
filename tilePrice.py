from __future__ import print_function
import math, sys

def floorArea(width,length):
    area= width*length

    return area

def floorCost(cost,width,length):
    price=cost*floorArea(width,length)

    return price

def main():
    print("Hi, welcome to the tile floor price calculator.")

    while True:
        cost=input("What is the cost of the tile per square foot: $")
        width=input("What is the width of the room in feet: ")
        length=input("What is the length of the room in feet: ")

        print("The total cost would be: $%.2f" % floorCost(cost,width,length))

        ans=raw_input("Would you like to calculate another price? Yes(y) or No(n)")
        if ans=="n":
            break
    print("\nThanks for using the tile floor price calculator!")


if __name__=='__main__':
    main()