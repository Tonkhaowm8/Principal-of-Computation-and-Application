 # Siraphop Mukdaphetcharat 64011614
hexDict = {"A": 10, "B" : 11, "C" : 12, "D" : 13, "E" : 14, "F" : 15} #hex dictionary

def from_decimal(d, b):
    i = d
    remLs = []
    while i != 0:
        rem = i % b
        print(rem)
        remLs.append(rem)
        i = i//b
    remLs.reverse()
    return remLs

def to_decimal(d, b):
    numLs = []
    strList = [*str(d)]
    strList.reverse()
    for i in strList:
        try:
            i.capitalize()
            numLs.append(int(hexDict[i]))
        except:
            numLs.append(int(i))
    dec = 0
    for i in range(len(numLs)):
        dec += int(numLs[i]) * (int(b)**i)
    return dec

def start():
    try:
        rep = True
        selectConvert = int(input("1 to convert from decimal, 2 to convert to decimal: "))
        while rep:
            if selectConvert == 1:
                try:
                    deciInput = int(input("Enter the decimal: "))
                    decibase = int(input("Enter the base: "))
                    print(from_decimal(deciInput, decibase))
                    rep = False
                except:
                    print("please input a correct input type")
            elif selectConvert == 2:
                try:
                    toDecInput = input("Enter the power: ")
                    toDecBase = input("Enter the base: ")
                    print(to_decimal(toDecInput, toDecBase))
                    rep = False
                except:
                    print("please input a correct input type")
            else:
                print("Please select 1 or 2")
                start()
    except:
        print("Please select 1 or 2")
        start()

start()