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
        entry = round(0.5 * self.length)
        for i in self.inputArr:
            wordNode = node(i)
            key = self.hash(i)
            index = self.convertToIndex(key)
            if self.hash_table[index] == " ":
                self.hash_table[index] = wordNode
            else:
                try:
                    check = self.hash_table[index].next
                    while check.next != None:
                        check = check.next
                    check.next = wordNode
                except:
                    self.hash_table[index].next = wordNode

    def rehash(self):
        self.clear_table()
        for i in range(getNextPrime(self.length * 2)):
            self.hash_table.append(" ")
        self.separate()


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
            if current.nodeData == str:
                return (f'"{str}" is correctly spelled')
            else:
                current = current.next
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
    hash_table.separate()
    #hash_table.showTableSeparate()
    print(hash_table.find(userInput))


file = open(r"/Users/tonkhaow/Desktop/Principal-of-Computation-and-Application/Lab 10/small.txt", "r")
data = file.read()
file.close()
data = data.split(" ")

start()
