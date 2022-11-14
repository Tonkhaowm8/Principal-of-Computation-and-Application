import os

file = open(r"C:\Users\Tonkhaow\Desktop\PCA\Principal-of-Computation-and-Application\Lab 10\small.txt", "r")
data = file.read()
file.close()
data = data.split(" ")
print(data)

def hash(str):
    h = 0
    for ch in str:
        h *= 37
        h += ord(ch)
    return h