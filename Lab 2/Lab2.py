 # Siraphop Mukdaphetcharat 64011614

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
    strList = str(d).split()
    strList.reverse()
    dec = 0
    for i in range(len(strList)):
        dec += int(strList[i]) * b**i
    return dec

selectConvert = int(input("1 to convert from decimal, 2 to convert to decimal: "))
if selectConvert == 1:
    deciInput = int(input("Enter the decimal: "))
    decibase = int(input("Enter the base: "))
    print(from_decimal(deciInput, decibase))
elif selectConvert == 2:
    toDecInput = int(input("Enter the decimal: "))
    toDecBase = int(input("Enter the base: "))
    print(from_decimal(toDecInput, toDecBase))
else:
    print("error")