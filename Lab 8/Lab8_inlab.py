# Siraphop Mukdaphetcharat 6401614

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
            while True:
                print(self.head.getData())
                self.head.setData(self.head.getNext().getData())
                self.head.setNext(self.head.getNext().getNext())
        except:
            return 0

def start():
    ul = UnorderedList()
    ul.add(1)
    ul.add(1)
    ul.add(2)
    ul.add(3)
    ul.add(3)
    ul.add(4)
    ul.print()
    ul.squish()
    ul.print()

start()