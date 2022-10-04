# Siraphop Mukdaphetcharat 64011614

from symbol import except_clause


class Node: # Node Class
    def __init__(self,initdata):
        self.data = initdata
        self.next = None
        self.previous = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def getPrevious(self):
        return self.previous

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

    def setPrevious(self, newPrevious):
        self.previous = newPrevious

class doubleLinkedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        addItem = Node(item)
        if self.head == None:
            addItem.setPrevious(None)
            addItem.setNext(None)
            self.head = addItem
        else:
            self.head.setNext(addItem)
            addItem.setPrevious(self.head)
            addItem.setNext(None)
            self.head = addItem

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getPrevious()
        return count

    def print(self):
        current = self.head
        while current != None:
            print(current.getData())
            current = current.getPrevious()

    def sort(self):
        current = self.head
        previous = current.getPrevious()
        noSwap = True
        while noSwap:
            while current != None:
                if current.getData() <= previous.getData():
                    current = previous
                    previous = previous.getPrevious()
                else:
                    high = previous
                    try:
                        previous.setNext(current.getNext())
                    except:
                        previous.setnext(None)
                    previous.setPrevious(current.getPrevious())

                    current.setNext(high.getNext())
                    try:
                        current.setPrevious(high.getPrevious())
                    except:
                        current.setPrevious(None)
                    previous = current.getPrevious()
                

    
def start():
    numPlayer = int(input("Enter the amount of players: "))
    dbll = doubleLinkedList()
    for i in range(numPlayer):
        dataArr = [input("Enter Name: "), int(input("Enter score: "))]
        dbll.add(dataArr)
    print(dbll.size())
    dbll.sort()
    dbll.print()

start()