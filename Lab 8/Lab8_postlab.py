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
        #origiHead = self.head
        highLs = []
        for i in range(size):
            current = self.head
            highNum = 0
            #print(i)
            while current != None:
                if current.getData()[1] > highNum and current.getData()[1] not in highLs:
                    high = current
                    highNum = current.getData()[1]
                else:
                    current = current.getPrevious()
            #print(high.getData())
            current = self.head
            while current.getData()[1] != high.getData()[1]:
                current = current.getPrevious()
            #print(current.getData())
            if current.getPrevious() == None:
                try:
                    current.getNext().setPrevious(None)
                except:
                    continue
            elif current.getNext() == None:
                current.getPrevious().setNext(None)
            else:
                current.getPrevious().setNext(current.getNext())
                current.getNext().setPrevious(current.getPrevious())
            
            current.setPrevious(self.head)  
            current.setNext(None)
            highLs.append(current.getData()[1])
            self.head = current
            print(self.head.getPrevious().getData())


            
    
def start():
    numPlayer = int(input("Enter the amount of players: "))
    dbll = doubleLinkedList()
    for i in range(numPlayer):
        dataArr = [input("Enter Name: "), int(input("Enter score: "))]
        dbll.add(dataArr)
    #print(dbll.size())
    dbll.print()
    print(" ")
    dbll.sort(dbll.size())
    #print(dbll.size())
    #dbll.print()

start()