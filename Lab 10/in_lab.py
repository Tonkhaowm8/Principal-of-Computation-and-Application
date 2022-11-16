# Siraphop Mukdaphetcharat 64011614

import os
import math

class node:
    def __init__(self, data):
        self.next = None
        self.nodeData = data

class hashtable:
    def __init__(self, arr):
        self.hash_table = []
        self.inputArr = arr
        self.length = getNextPrime(round(len(arr) * 0.2))
        for i in range(self.length):
            self.hash_table.append(" ")  
        self.expansion = 0
        self.load_factor = 0
        self.collisions = 0
        self.longest = 0

    def hash(self, str):
        h = 0
        for ch in str:
            h *= 37
            h += ord(ch)
        return h

    def clear_table(self):
        for i in range(self.length):
            self.hash_table.pop()

    def convertToIndex(self, key):
        return key % self.length

    def separate(self):
        chain_length = 1
        entry = round(0.5 * self.length)
        rehash = False
        for i in range(len(self.inputArr)):
            wordNode = node(self.inputArr[i])
            key = self.hash(self.inputArr[i])
            index = self.convertToIndex(key)
            if i >= entry:
                self.expansion += 1
                rehash = True
                self.longest = 0
                break
            if self.hash_table[index] == " ":
                self.hash_table[index] = wordNode
            else:
                try:
                    check = self.hash_table[index].next
                    while check.next != None:
                        check = check.next
                        chain_length += 1
                    check.next = wordNode
                    if chain_length > self.longest:
                        self.longest = chain_length
                except:
                    self.hash_table[index].next = wordNode
            self.load_factor = i / len(self.hash_table)
        if rehash:
            self.rehash(1)
            
    def rehash(self, mode):
        self.clear_table()
        self.length = getNextPrime(self.length * 2)
        for i in range(self.length):
            self.hash_table.append(" ")
        if mode == 1:
            self.separate()
        else:
            self.linear()

    def showTableSeparate(self):
        for i in self.hash_table:
            arr = []
            if type(i) != str:
                while i != None:
                    arr.append(i.nodeData)
                    i = i.next
                print(arr)
            else:
                arr.append(i)
                print(arr)

    def find(self, str):
        key = self.hash(str)
        index = self.convertToIndex(key)
        current = self.hash_table[index]
        while current != None:
            if current == " ":
                break
            if current.nodeData == str:
                return (f'"{str}" is correctly spelled')
            else:
                current = current.next
        return (f'"{str}" is not in the dictionary')

    def linear(self):
        collisions = 0
        entry = round(0.5 * self.length)
        rehash = False
        for i in range(len(self.inputArr)):
            key = self.hash(self.inputArr[i])
            index = self.convertToIndex(key)
            if i >= entry:
                self.expansion += 1
                rehash = True
                self.collisions = 0
                break
            if self.hash_table[index] == " ":
                self.hash_table[index] = self.inputArr[i]
            else:
                j = 1
                while True:
                    index = self.convertToIndex(key + j)
                    if self.hash_table[index] == " ":
                        break
                    else:
                        j += 1
                        collisions += 1
                        continue
                if collisions > self.collisions:
                    self.collisions = collisions
            self.load_factor = i / len(self.hash_table) 
        if rehash:
            self.rehash(2)

    def showTableLinear(self):
        j = 0
        for i in self.hash_table:
            if i == " ":
                continue
            else:
                j += 1
        return self.hash_table

    def search(self, str):
        key = self.hash(str)
        index = self.convertToIndex(key)
        initialIndex = index
        found = False
        if self.hash_table[index] == str:
            found = True
        else:
            j = 1
            index = self.convertToIndex(key + j)
            while index != initialIndex:
                index = self.convertToIndex(key + j)
                if self.hash_table[index] == str:
                    found = True
                    break
                j += 1
        if found:
            return (f'"{str}" is correctly spelled')
        else:
            return (f'"{str}" is not in the dictionary')
                
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

def start():
    userInput = input("Enter a word to search: ")
    hash_table = hashtable(data)
    userMode = int(input("1. Separate Chaining, 2. Linear Probing: "))
    if userMode == 1:
        hash_table.separate()
        #hash_table.showTableSeparate()
        print(hash_table.find(userInput))
        print(f"Total Words: len(data)")
        print(f"{hash_table.expansion} expansions")
        print(f"load factor {hash_table.load_factor}")
        print(f"longest chain {hash_table.longest}")
    else:
        hash_table.linear()
        #print(hash_table.showTableLinear())
        print(hash_table.search(userInput))
        print(hash_table.find(userInput))
        print(f"Total Words: len(data)")
        print(f"{hash_table.expansion} expansions")
        print(f"load factor {hash_table.load_factor}")
        print(f"{hash_table.longest} collisions")

file = open(r"C:\Users\Tonkhaow\Desktop\PCA\Principal-of-Computation-and-Application\Lab 10\small.txt", "r")
data = file.read()
file.close()
data = data.split(" ")

start()
