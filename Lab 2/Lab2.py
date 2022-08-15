# Siraphop Mukdaphetcharat 64011614
def from_decimal(d, b):  # Convert decimal to any base function
    ansLs = []
    if b == 1:
        print("ERROR! Base cannot be 1!!")
        exit()
    elif b > 36:
        print("ERROR! Base cannot exceed 36!")
        exit()
    elif b <= 0 or d <= 0:
        print("ERROR! Base cannot be less than or equal to zero!")
        exit()
    i = d
    remLs = []
    finalLs = []
    while i != 0:  # Change decimal to base given
        rem = i % b
        remLs.append(rem)
        i = i // b
    remLs.reverse()
    for i in remLs:  # Convert the number to hex alphabet if the number exceed 9
        if i <= 9:
            finalLs.append(i)
        else:
            finalLs.append(chr(i + 55))  # chr is ascii function that converts number to characters
    for i in finalLs:
        ansLs.append(str(i))
        ans = "".join(ansLs)
    return ans


def to_decimal(d, b):  # Convert any base to decimal
    if b == "1":
        print("ERROR! Base cannot be 1!!")
        exit()
    elif "-" in b or "-" in d:
        print("ERROR! Cannot be less than or equal to zero!")
        exit()
    numLs = []
    strList = [*str(d)]  # convert string without space into arrays
    strList.reverse()
    for i in strList:
        try:  # Capitalize everything so that the text would have similar ASCII code
            i = int(i)
            numLs.append(int(i))
        except AttributeError:
            i.capitalize()
            translated = ord(i) - 55  # ord change ASCII code of text into number
            if translated <= int(b):
                numLs.append(translated)
            else:
                print("error! Invalid Input")
    dec = 0
    for i in range(len(numLs)):  # calculate base number into decimals
        dec += int(numLs[i]) * (int(b) ** i)
    return dec


def start():  # Start Function for user input
    try:
        rep = True  # repeating input for errors
        selectConvert = int(input("1 to convert from decimal, 2 to convert to decimal: "))
        while rep:
            if selectConvert == 1:
                try:  # Input from decimal to any base
                    deciInput = int(input("Enter the decimal: "))
                    decibase = int(input("Enter the base: "))
                    print(from_decimal(deciInput, decibase))
                    rep = False
                except ValueError:
                    print("please input a correct input type")
            elif selectConvert == 2:  # Input from decimal to any base
                toDecInput = input("Enter the power: ")
                toDecBase = input("Enter the base: ")
                print(to_decimal(toDecInput, toDecBase))
                rep = False
            else:
                print("Please select 1 or 2")
                start()
    except ValueError:
        print("Please select 1 or 2")
        start()


start()
