import matplotlib.pyplot as plt
import numpy as np
import math as m

x = np.linspace(m.log(9934.2,10) - m.log(144613.45,10), 4, 400)
x2 = np.linspace(-2, m.log(9934.2,10) - m.log(144613.45,10), 400)
x3 = np.linspace(-2,m.log(9934.2,10) - m.log(104070.97,10), 400)
x4 = np.linspace(-2,m.log(9934.2,10) - m.log(52445.81,10), 400)
x5 = np.linspace(-2,m.log(9934.2,10) - m.log(9032.46,10), 400)

y = m.log(9934.2,10) + 0*x
y2 = m.log(144613.45,10) + x2
y3 = m.log(104070.97,10) +x3
y4 = m.log(52445.81,10) +x4
y5 = m.log(9032.46,10) +x5
plt.plot(x,y,label="Peak MFlops/s")
plt.plot(x2,y2,label="L1 Cache")
plt.plot(x3,y3,label="L2 Cache")
plt.plot(x4,y4,label="L3 Cache")
plt.plot(x5,y5,label="DRAM")


x = [-0.25806092,1.76774937,0.50201721,2.40402936]
y = [2.55552369,2.72560948,2.63110879,2.9386548]
matrix1 = np.array([-0.25806092,2.55552369])
matrix2 = np.array([1.76774937,2.72560948])
matrix3 = np.array([0.50201721,2.63110879])
matrix4 = np.array([2.40402936,2.9386548])
plt.plot(x,y,'o')
plt.text(x[0]+0.1,y[0],"A",va="center")
plt.text(x[1]+0.1,y[1],"B",va="center")
plt.text(x[2]+0.1,y[2],"C",va="center")
plt.text(x[3]+0.1,y[3],"D",va="center")
#plt.plot(matrix1)
#plt.scatter(matrix2,'o')
#plt.plot(matrix3,'o')
#plt.plot(matrix4,'o')
plt.grid(True)
plt.title("Matrix Multiplication Roof-Line Model (Log-Log Scale)")
plt.xlabel("MFlops/Mbyte")
plt.ylabel("MFlops/s")
plt.legend()
plt.savefig('matrix_ mult_plot.png')
