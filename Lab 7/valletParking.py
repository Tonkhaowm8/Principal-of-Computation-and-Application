# Siraphop Mukdaphetcharat 64011614
import random

class stack:
    def __init__(self):
        self.stack = []
    
    def push(self, element):
        self.stack.append(element)

    def pop(self):
        popElement = self.stack[-1]
        self.stack.pop[-1]
        return popElement

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        if len(self.stack.append) == 0:
            return True
        else:
            return False
            
    def size(self):
        return len(self.stack)

    def contain(self, element):
        if element in self.stack:
            return True
        else:
            return False

    def returnLs(self):
        return self.stack

class parking:
    def __init__(self):
        self.parkingLot = stack()

    def returnStack(self):
        return self.parkingLot
    
    def park(self, car):
        self.parkingLot.push(car)

    def backOut(self, car):
        if self.parkingLot.contain(car):
            carList = stack()
            for i in range(self.parkingLot.size()):
                if car == self.parkingLot.peek():
                    self.parkingLot.pop()
                    break
                else:
                    carList.push(self.parkingLot.pop())
                for j in range(carList.size()):
                    self.parkingLot.push(carList.pop())


def initialize():
    soiInput = int(input("How many soi are there to park: "))
    soiArr = []
    for i in range(soiInput):  
        soiArr.append(parking())
    for i in soiArr:
        carNum = random.randint(0, 4)
        for j in range(carNum):
            carPlate = random.randint(1, 1000)
            while i.returnStack().contain(carPlate):
                carPlate = random.randint(1, 1000)
            i.park(carPlate)
        print(i.returnStack().returnLs())
    return soiArr

def inputMode(soiArr):
    modeInput = int(input("1. parking, 2. backout: "))
    if modeInput == 1:
        carInput = int(input("How many cars you want to park: "))
        for i in range(carInput):
            carNumber = int(input("Enter car licence plate number: "))
            soiNum = int(input("Enter the number of soi you want to park: ")) - 1
            soiArr[soiNum].park(carNumber)
            print(f"Your car with the number {carNumber} has been parked!")
            for j in soiArr:
                print(j.returnStack().returnLs())

def start():
    soiArr = initialize()
    

start()
