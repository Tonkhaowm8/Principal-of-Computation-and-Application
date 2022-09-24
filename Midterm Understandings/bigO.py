import matplotlib.pyplot as plt


n = int(input("Enter n: "))
i = 1
j = 0
x_axis = []
y_axis = []
length1 = []
while i <= n: #Algo of log2n
    #print(i)
    x_axis.append(i)
    y_axis.append(j)
    length1.append(len(x_axis))
    j += 1
    i = i * 2

print(f"The points of algo 1 is: {y_axis}")
#print(f"The amount of points of algo 2 is: {len(x2_axis)}")
plt.plot(x_axis, y_axis)
plt.ylabel("No. of iterations run")
plt.xlabel("No. of points")
#plt.plot(x2_axis, y2_axis)
plt.show()