#! /usr/bin/env python3

def ifelse(n):
    if n % 2 == 1:
        print("Weird")

    if n % 2 == 0:
        if n % 2 == 0 and n in range(2,6):
            print("Not Weird")
        elif n % 2 == 0 and n in range(6,21):
            print("Weird")
        elif n % 2 == 0 and n > 20:
            print("Not Weird")
        else: 
            print("Not Weird")
ifelse(int(input().strip()))

