#64011614 Siraphop Mukdaphetcharat
def stars(n):
    if n > 0:
        print("*" * n)
        print("*" * stars(n - 1))
    return (n + 1)

stars(int(input("enter a number: ")))

def stars2(n, a = 1):
    if n >= a:
        print('*' * a)
        stars2(n, a + 1)
        print('*' * a)

stars2(int(input("enter a number: ")))