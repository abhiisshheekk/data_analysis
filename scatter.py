import numpy as np
import matplotlib.pyplot as la
from scipy import stats

x1 = np.random.randint(0,31,20)
y1 = np.random.randint(0,31,20)
x2 = np.random.randint(0,21,20)
y2 = 3*x2 + 5
x3 = [10,50,11,25,8,21,13,15,10,55,5,17,8,21,13,15,10]
y3 = [5,7,3,6,7.5,4,8,4,6.3,4.5,7.1,5.3,8,4.1,6.8,3.8,7]

fig1 = la.figure()
la.scatter(x1,y1,marker="D",color="red")
la.xlabel('X1')
la.ylabel('Y1')
la.title('Random Scatter Plot')
fig1.savefig('random.png')

fig1 = la.figure()
la.scatter(x2,y2)
la.xlabel('X2')
la.ylabel('Y2')
la.title('Linear Scatter Plot')
fig1.savefig('linear.png')

fig1 = la.figure()
la.scatter(x3,y3)
la.xlabel('X3')
la.ylabel('Y3')
la.title('Scatter Plot with outliers')
fig1.savefig('outlier.png')