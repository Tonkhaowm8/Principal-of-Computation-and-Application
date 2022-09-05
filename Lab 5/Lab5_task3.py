import timeit
from matplotlib import pyplot as plt


def normal_fibo(n):
    a = 0
    b = 1
    ans = 0
    for i in range(n):
        if i % 2 == 0:
            b += a
            ans = b
        else:
            a += b
            ans = a
    return ans

def fibo_rec(n):
    if n <= 1:
        return n
    return fibo_rec(n-1) + fibo_rec(n-2)


#n = int(input("Input n : "))
xNormal = []
yNormal = []
xRec = []
yRec = []
for i in range(0,1000,100):
    #StartTime = timeit.default_timer()
    #normal = normal_fibo(i)
    #StopTime = timeit.default_timer()
    #xNormal.append(i)
    #yNormal.append(StopTime - StartTime)


    StartTime = timeit.default_timer()
    recursive = fibo_rec(i)
    StopTime = timeit.default_timer()
    xRec.append(i)
    yRec.append(StopTime - StartTime)

#plt.plot(xNormal, yNormal)
plt.plot(xRec, yRec)
plt.xlabel("n")
plt.ylabel("time")
plt.title("Iterative Algorithm")
plt.show()
#print(f"Iterative fibo result is {normal_fibo(n)} with runtime of {round(StopTime - StartTime, 10)}")
#StartTime = timeit.default_timer()
#normal = fibo_rec(n)
#StopTime = timeit.default_timer()
#print(f"recursive  fibo result is {fibo_rec(n)} with runtime of {round(StopTime - StartTime, 10)}")
