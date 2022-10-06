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
        for i in range(size):
            current = self.head
            previous = current.getPrevious()
            for j in range(size):
                prevSwitch = False
                nextSwitch = False
                if current == None:
                    break
                if current.getData()[1] > previous.getData()[1]:
                    if previous == None:
                        prevSwitch = True
                    if current.next() == None:
                        nextSwitch = True
                    # Previous
                    if prevSwitch:
                        previous.setPrevious(current)
                        current.setPrevious(None)

                        currNext = current.getNext()
                        prev.setNext(current)
                        current.setNext(previous)
                        previous.setNext(currNext)

                    elif nextSwitch:
                        prev = previous.getPrevious()
                        previous.setPrevious(current)
                        current.setPrevious(prev)

                        prev.setNext(current)
                        current.setNext(previous)
                        previous.setNext(None)
                    
                    else:
                        #Previous
                        prev = previous.getPrevious()
                        current.getNext().setPrevious(current)
                        previous.setPrevious(current)
                        current.setPrevious(prev)
                        # Next
                        currNext = current.getNext()
                        prev.setNext(current)
                        current.setNext(previous)
                        previous.setNext(currNext)
                        # sortout pointers

                    #print(current.getPrevious().getPrevious().getData())
                    #print(current.getPrevious().getPrevious().getData())
                    if i == 0:
                        previous.setNext(None)
                        self.head = previous
                        previous = current.getPrevious()
                else:
                    current = previous
                    previous = current.getPrevious()

            #print(self.head.getData())
        #print(self.head.getData())
        #print(self.head.getPrevious().getData())
        #print(self.head.getPrevious().getPrevious().getData())


def start():
    numPlayer = int(input("Enter the amount of players: "))
    dbll = doubleLinkedList()
    for i in range(numPlayer):
        dataArr = [input("Enter Name: "), int(input("Enter score: "))]
        dbll.add(dataArr)
    #print(dbll.size())
    #dbll.print()
    #print(" ")
    dbll.sort(dbll.size())
    #print(dbll.size())
    dbll.print()

start()