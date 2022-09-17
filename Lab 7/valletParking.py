# Siraphop Mukdaphetcharat 64011614

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

class parking:
    def __init__(self):
        self.parkingLot = stack()
    
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

    
