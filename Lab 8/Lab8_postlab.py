# Siraphop Mukdaphetcharat 64011614

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

    def sort(self, size):
        current = self.head
        origiHead = self.head
        high = current
        for i in range(size):
            for j in range(size):
                if current == None:
                    break
                elif current.getData()[1] > high.getData()[1]:
                    high = current
                else:
                    current = current.getPrevious()
            if high != None:
                try:
                    high.getNext().setPrevious(high.getPrevious())
                except:
                    continue
                try:
                    high.getPrevious().setNext(high.getNext())
                except:
                    continue

            high.setPrevious(self.head)
            high.setNext(None)
            self.head = high
            origiHead = origiHead.getNext()

            

    
def start():
    numPlayer = int(input("Enter the amount of players: "))
    dbll = doubleLinkedList()
    for i in range(numPlayer):
        dataArr = [input("Enter Name: "), int(input("Enter score: "))]
        dbll.add(dataArr)
    #print(dbll.size())
    dbll.sort(dbll.size())
    dbll.print()

start()