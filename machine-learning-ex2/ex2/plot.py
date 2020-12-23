import matplotlib.pyplot as plt
import csv

x=[]
y=[]

with open('ex2data1.txt','r') as csvfile:
    plots=csv.reader(csvfile,delimiter=' ')
    for row in plots:
        x.append(float(row[0]))
        y.append(float(row[1]))

plt.plot(x,y,label='loaded from file1')
plt.xlabel('x')
plt.ylabel('y')
plt.title('intersting graph')
plt.legend()
plt.show()
