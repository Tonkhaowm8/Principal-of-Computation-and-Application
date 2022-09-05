def stars(n):
    if n > 0:
        print("*" * stars(n))
    return (n - 1)

stars(int(input("enter a number: ")))

def stars2(n):
    if n > 0:
        stars2(n-1)
        print("*" * n)
    return (n + 1)
    

#stars2(int(input("enter a number: ")))