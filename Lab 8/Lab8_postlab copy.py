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
        self.tail = None

    def add(self, item):
        addItem = Node(item)
        if self.head == None:
            addItem.setPrevious(None)
            addItem.setNext(None)
            self.head = addItem
            self.tail = addItem
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

    def print(self, mode):
        if mode == 1:
            current = self.head
            while current != None:
                if current.getData() != None:
                    print(current.getData())
                current = current.getPrevious()
        else:
            current = self.tail
            while current != None:
                if current.getData() != None:
                    print(current.getData())
                current = current.getNext()
        

    def sort(self):
        if self.head == None:
            return 0
        else:
            current = self.head
            while current.getPrevious() != None:
                previousNode = current.getPrevious()
                while previousNode != None:
                    if current.getData()[1] > previousNode.getData()[1]:
                        temp = current.getData()
                        current.setData(previousNode.getData())
                        previousNode.setData(temp)
                    previousNode = previousNode.getPrevious()
                current = current.getPrevious()

    def retrieveScore(self, name):
        current = self.head
        found = True
        while current.getData()[0] != name:
            current = current.getPrevious()
            if current == None:
                found = False
                break
        if found:
            return current.getData()

    def editScore(self, name, score):
        current = self.head
        found = True
        while current.getData()[0] != name:
            current = current.getPrevious()
            if current == None:
                found = False
                break
        if found:
            oldData = current.getData()
            oldData[1] = score
            current.setData(oldData)

    def deleteScore(self, name):
        current = self.head
        found = True
        while current.getData()[0] != name:
            current = current.getPrevious()
            if current == None:
                found = False
                break
        if found:
            while current.getNext() != None:
                current.setData(current.getNext().getData())
                current = current.getNext()
            current.setData(None)

def start():
    numPlayer = int(input("Enter the amount of players: "))
    dbll = doubleLinkedList()
    for i in range(numPlayer):
        dataArr = [input("Enter Name: "), int(input("Enter score: "))]
        dbll.add(dataArr)
    dbll.print(1)
    mode = int(input("[1] Sort, [2] Edit, [3] Add, [4] Delete, [5] Retrieve: "))
    if mode == 1:
        dbll.sort()
        userMode = int(input("[1] ascending, [2] decending: "))
        dbll.print(userMode)
    elif mode == 2:
        name = input("Enter name of player: ")
        score = int(input("Enter score: "))
        dbll.editScore(name, score)
        dbll.print(1)
    elif mode == 3:
        name = input("Enter name of player: ")
        score = int(input("Enter score: "))
        dbll.add([name, score])
        dbll.print(1)
    elif mode == 4:
        name = input("Enter name of player: ")
        dbll.deleteScore(name)
        dbll.print(1)
    elif mode == 5:
        name = input("Enter name of player: ")
        print(dbll.retrieveScore(name))

start()