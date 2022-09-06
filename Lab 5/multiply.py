a = 3
b = 5
c = 0

def multiply(a, b):
    if b > 0:
        return (a + multiply(a, b - 1))
    else:
        return 0

print(multiply(a, b))