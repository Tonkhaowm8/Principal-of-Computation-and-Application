def stars(n):
    if n > 0:
        print("*" * n)
        print("*" * stars(n - 1))
    return (n + 1)

#stars(int(input("enter a number: ")))

def stars2(n):
    def stars3(n): # print 1 - 5
        if n > 0:
            print("*" * stars(n - 1))
        return (n + 1)
    if n > 0:
        stars2(n - 1)
        print(n)
    else:
        print("*" * stars3(n))

    return (n + 1)
    

stars2(int(input("enter a number: ")))