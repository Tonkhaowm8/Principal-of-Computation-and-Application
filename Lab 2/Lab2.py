 # Siraphop Mukdaphetcharat 64011614
#hexDict = {"A": 10, "B" : 11, "C" : 12, "D" : 13, "E" : 14, "F" : 15, "G" : 16, "H" : 17, "I" : 18, "J" : 19, "K" : 20,"L" : 21,"M" : 22,"N" : 23,
#"O" : 24,"P" : 25,"Q" : 26,"R" : 27,"S" : 28,"T" : 29,"U" : 30,"V" : 31,"W" : 32,"X" : 33,"Y" : 34,"Z" : 35} #hex dictionary

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
            translated = ord(i) - 55
            if translated <= int(b):
                numLs.append(translated)
            else:
                print("error! Invalid Input")
        except:
            numLs.append(int(i))
    dec = 0
    for i in range(len(numLs)):
        dec += int(numLs[i]) * (int(b)**i)
    return dec

def start(): # Start Function for user input
    try:
        rep = True # repeating input for errors
        selectConvert = int(input("1 to convert from decimal, 2 to convert to decimal: "))
        while rep:
            if selectConvert == 1:
                try: #Input from decimal to any base
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