import colour
from colour.plotting import *
colour_style()
import numpy as np

plot_chromaticity_diagram_CIE1976UCS(standalone=False)

import matplotlib.pyplot as plt

ax = plt.gca()       # 获取CIE1976UCS的坐标系

# 坐标转换函数
# colour.xy_to_Luv_uv        convert  CIE 1931 xy to CIE 1976UCS u'v'
# colour.xy_to_UCS_uv       convert CIE 1931 xy to CIE 1960UCS uv            
#  xy: CIE 1931 xy;    UCS_uv: CIE 1960UCS uv;  Luv_uv: CIE 1976 u'v'
ITUR_709=([[.64, .33], [.3, .6], [.15, .06]])
ITUR_709_uv=colour.xy_to_Luv_uv(ITUR_709)
ITUR_2020=([[.708, .292], [.170, .797], [.131, .046]])
ITUR_2020_uv=colour.xy_to_Luv_uv(ITUR_2020)
DCI_P3=([[.68, .32], [.265, .69], [.15, .06]])
DCI_P3_uv=colour.xy_to_Luv_uv(DCI_P3)
pointer_bound= ([[ 0.508, 0.226], [ 0.538, 0.258], [ 0.588, 0.280], [ 0.637, 0.298], [ 0.659, 0.316], 
                                      [ 0.634, 0.351], [ 0.594, 0.391], [ 0.557, 0.427], [ 0.523, 0.462], [ 0.482, 0.491], 
                                      [ 0.444, 0.515], [ 0.409, 0.546], [ 0.371, 0.558], [ 0.332, 0.573], [ 0.288, 0.584], 
                                      [ 0.242, 0.576], [ 0.202, 0.530 ], [ 0.177, 0.454], [ 0.151, 0.389],[ 0.151, 0.330 ],
                                      [ 0.162, 0.295], [ 0.157, 0.266], [ 0.159, 0.245], [ 0.142, 0.214], [ 0.141, 0.195], 
                                      [ 0.129, 0.168], [ 0.138, 0.141], [ 0.145, 0.129], [ 0.145, 0.106], [ 0.161, 0.094], 
                                      [ 0.188, 0.084], [ 0.252, 0.104], [ 0.324, 0.127], [ 0.393, 0.165], [ 0.451, 0.199], [ 0.508, 0.226]])
pointer_bound_uv=colour.xy_to_Luv_uv(pointer_bound)


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
plt.plot(result[:, 1], result[:, 3], 'r*')


plt.axis([-0.1, 0.7, -0.1, 0.7])    #改变坐标轴范围
plt.show()