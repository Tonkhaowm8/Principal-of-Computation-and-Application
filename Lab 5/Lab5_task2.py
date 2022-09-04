def stars(n):
    if n > 0:
        print("*" * n)
        print("*" * stars(n-1))
    return (n + 1)

stars(int(input("enter a number: ")))