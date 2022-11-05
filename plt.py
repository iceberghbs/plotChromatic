from colour.plotting import *
import numpy as np


import matplotlib.pyplot as plt
import pandas as pd
xyz = pd.read_excel(io=r'xyz.xlsx')
xyz = xyz.values
xyz = xyz.reshape((-1, 7))
x_bar = xyz[:, 4]
y_bar = xyz[:, 5]
z_bar = xyz[:, 6]
# print(xyz)  # test

C1 = 3.7418e-12
C2 = 1.4388e4

def blackBody(t):  
    waveLengths = np.array(range(380, 785, 5), dtype=np.int64)
    # print(waveLengths)

    P_Lamda = np.multiply((C1/np.power(waveLengths, 5)), (1/(np.exp(C2/(waveLengths*t)))-1))

    return P_Lamda

result = np.zeros(shape=(12000, 4))
for i in range(0, 12000):

    P_Lamda = blackBody(i+1)
    # print(P_Lamda)

    X = np.dot(P_Lamda, x_bar) * 5
    Y = np.dot(P_Lamda, y_bar) * 5
    Z = np.dot(P_Lamda, z_bar) * 5

    x = X/(X+Y+Z)
    y = Y/(X+Y+Z)
    z = Z/(X+Y+Z)
    # print(x, y, z)

    result[i, :] = [i+1, x, y, z]
    # print(result[i, :])

print(result)
plot_chromaticity_diagram_CIE1960UCS(standalone=False)
plt.plot(result[:, 1], result[:, 2], '-')
plt.axis([-0.1, 0.7, -0.1, 0.7])    #改变坐标轴范围
plt.show()

plot_planckian_locus_in_chromaticity_diagram_CIE1960UCS(['A', 'B', 'C'])  # one step
