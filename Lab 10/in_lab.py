import os
import math

class node:
    def __init__(data):
        next = None
        nodeData = data


class hashtable:
    def __init__(arr):
        hash_table = []
        inputArr = arr
        length = getNextPrime(len(arr) * 0.2)
        for i in range(length):
            hash_table.append(" ")

    def hash(self, str):
        h = 0
        for ch in str:
            h *= 37
            h += ord(ch)
        return h

    def clear_table(self):
        for i in range(self.length):
            self.hash_table.pop()
        for i in range(self.length):
            self.hash_table.append(" ")

    def convertToIndex(self, key):
        return key % self.length

    def separate(self):
        for i in self.inputArr:
            wordNode = node(i)
            key = self.hash(i)
            index = self.convertToIndex(key)
            if self.hash_table == " ":
                self.hash_table[index] = wordNode
            else:
                try:
                    check = self.hash_table[index].next
                    while check != None:
                        check = check.next
                except:
                    self.hash_table[index].next = wordNode
                
                
                
            


def getNextPrime(num):
    prime = False
    while not prime:
        if '.' in str(math.sqrt(num)):
            for i in range(2, num - 1):
                if num % i != 0:
                    prime = True
                    continue
                else:
                    num += 1
                    prime = False
                    break
        else:
            num += 1
    return num



file = open(r"/Users/tonkhaow/Desktop/Principal-of-Computation-and-Application/Lab 10/small.txt", "r")
data = file.read()
file.close()
data = data.split(" ")

print(getNextPrime(29))
