# Siraphop Mukdaphetcharat 6401614

from itsdangerous import NoneAlgorithm


class Node: # Node Class
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

class UnorderedList:

    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def deleteAfter(self, node):
        current = node.head
        current

    def print(self):
        try:
            current = self.head
            while True:
                if current.getData() == "end":
                    break
                else:
                    print(current.getData())
                    current = current.getNext()
        except:
            return 0

    def squish(self):
        current = self.head
        duplicates = None
        exitt = False
        while True:
            if current == None:
                break
            while duplicates == current.getData():
                if current.getNext() == None:
                    current.setData("end")
                    current.setNext(None)
                    exitt = True
                    break
                else:
                    current.setData(current.getNext().getData())
                    current.setNext(current.getNext().getNext())
            if exitt:
                break
            duplicates = current.getData()
            try:
                current = current.getNext()
            except:
                break
                
    def dble(self):
        current = self.head
        while current != None:
            dupNode = Node(current.getData())
            try:
                dupNode.setNext(current.getNext())
            except:
                dupNode.setNext(None)
                break
            current.setNext(dupNode)
            current = dupNode.getNext()
    
def start():
    ul = UnorderedList()
    numInput = int(input("num of input: "))
    for i in range(numInput):
        ul.add(input("enter num: "))
    modeInput = int(input("(1) Squish, (2) Dble: "))
    if modeInput == 1:
        ul.squish()
        ul.print()
    elif modeInput == 2:
        ul.dble()
        ul.print()

start()