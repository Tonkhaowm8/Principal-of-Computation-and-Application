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


deciInput = int(input("Enter the decimal: "))
decibase = int(input("Enter the base: "))
print(from_decimal(deciInput, decibase))
