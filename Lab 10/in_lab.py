import os
import math

class node:
    def __init__():
        next = None
        data = None

class hashtable:
    def __init__(arr):
        hash_table = []
        length = len(arr) * 0.2

def getNextPrime(num):
    prime = False
    while not prime:
        if '.' in str(math.sqrt(num)):
            for i in range(1, 9):
                if num % i != 0:
                    num += 1
                    prime = False
                    break
                else:
                    prime = True
                    continue
            
        else:
            num += 1
    return num

def hash(str):
    h = 0
    for ch in str:
        h *= 37
        h += ord(ch)
    return h

file = open(r"C:\Users\Tonkhaow\Desktop\PCA\Principal-of-Computation-and-Application\Lab 10\small.txt", "r")
data = file.read()
file.close()
data = data.split(" ")

print(getNextPrime(25))
