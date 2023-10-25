0# _*_ coding : UTF-8 _*_
# 开发人员： MY
# 开发时间： 2022/2/28  16:58
# 文件名称： 1.py
# 开发工具： PyCharm

import PySide6.QtGui
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame
from math import floor, ceil, pi
import fancyimpute
import re
import sys
import xlrd
import xlwt
import matplotlib.pyplot as plt
import pyqtgraph as pg

from math import sqrt
from pandas import DataFrame, Series


plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['xtick.direction'] = 'in'  # 将x周的刻度线方向设置向内
plt.rcParams['ytick.direction'] = 'in'  # 将y轴的刻度方向设置向内


# Algorithm
def destroy_depth(self, phi, m, gama, h):
    K1 = (1+np.sin(phi))/(1-np.sin(phi))
    F = (K1 - 1)/sqrt(K1) + ((K1 - 1)/sqrt(K1))**2 * np.arctan(sqrt(K1))
    x_alpha = m/F*np.log(10*gama*h)  # A.H.Wilson 曲屈服区长度计算
    e1 = x_alpha*np.cos(phi)/(2*np.cos(np.pi/4+phi/2))
    e2 = e2 = np.e**((np.pi/4 + phi/2)* np.tan(phi))
    return e1 * e2

def uneven(series, n):
        Ue = 0
        count = 0
        series = series.apply(lambda x: (x-series.min())/(series.max()-series.min())) 
        for i in range(len(series)):
            s = []
            for j in range(len(series)):
                if i != j and abs(i-j)<n:
                    a = abs(series.iloc[i] - series.iloc[j])/(abs(i-j))
                    Ue += a
                    count += 1
        return 10*Ue/count  # 根据结果去求结果 doesn't make any sense

def mul(df1, df2):
    l1 = df1.values.tolist()
    l2 = df2.values.tolist()
    l3 = np.multiply(l1, l2)
    return DataFrame(l3)

def rho_3(n, filename, a, reverse=False):  # 原始数据处理
    # 处理原始数据得出
    dataset = pd.read_csv(filename, encoding='gb2312')
    dataset.dropna(axis=1, inplace=True)
    col = []
    for i in dataset.columns:
        col.append(i[:-3])
    dataset.columns = col
    if not reverse:
        dataset = dataset[0:n]  # Take the first three rows
        ampere = dataset.电流[:n]
        dataset.drop(columns=['电流'], inplace=True)
    elif reverse:
        dataset = dataset[-n:][::-1]  # Take the last three rows
        ampere = dataset.电流
        dataset.drop(columns=['电流'], inplace=True)
        for i in range(len(dataset.index)):
            dataset.iloc[i] = dataset.iloc[i][::-1]

    # rho_s  ------------------------
    data_r = DataFrame(np.zeros((n, 46)))
    for row in range(len(dataset.index)):
        for col in range(row + 1, len(dataset.columns)):
            cat = []
            m = col
            n = col + 1
            while (n - m) <= (m - row) and n <= 47:
                cat.append((row, m, n))
                m -= 1
                n += 1
            if cat != []:
                dog = 0  # Apprent resistivity
                f = 0  # Weight factor: f
                for i in cat:
                    fi = 3 / (4 * pi * (((i[2] - i[0]) * a) ** 3 - (
                                (i[1] - i[0]) * a) ** 3))  # Weight factor f = 3/(4*pi*(AN ** 3 - AM ** 3))
                    ki = 2 * pi * (i[1] - i[0]) * (i[2] - i[0]) * a / (
                                i[2] - i[1])  # Coefficient k = 2*pi*|AM|*|AN|/|MN|
                    dog += fi * ki * (dataset.iloc[i[0]][i[1]] - dataset.iloc[i[0]][i[2]]) / ampere.iloc[
                        i[0]]  # ∑(ai * ki * delta_Ui/I) / ∑ai
                    f += fi
                data_r.iloc [row][col - 1] = dog / f
                # ------------------------------
    #data_r.to_csv('d:/kong/aaa_/3ar.csv', encoding='gb2312')
    return data_r

def f(p1):   # delta_x 网格划分间距
    list1 = []
    for x_pos in range(len(p1)-1):
        # 必须满足单一网格内 曲线单调
        p_start = p1[x_pos]
        p_end = p1[x_pos+1]
        if p_start > p_end:
            top_boundary = ceil(p_start)           
            bot_boundary = floor(p_end)
            list1.append([[x_pos, x_pos+1], [bot_boundary,bot_boundary], [top_boundary, top_boundary]])
        elif p_start < p_end:
            top_boundary = ceil(p_end)
            bot_boundary = floor(p_start)
            list1.append([[x_pos, x_pos+1], [bot_boundary,bot_boundary], [top_boundary, top_boundary]])
            
            
            # 1添加 两相邻坐标轴 值相等的情况 
    return list1
rho_s = pd.read_csv('d:/kong/aaa_/4ar.csv', index_col=None)
rho_s.drop(columns='Unnamed: 0', inplace=True)
delta_x = 0.25
# func = lambda x :np.sqrt((1.5/delta_x)**2-x**2)

switch = True

def func(x, A, d):
    return np.sqrt((d/delta_x)**2-(x-A)**2)
if switch:
    for A in rho_s.index:
        for M in range(A, len(rho_s.columns)-1):
            d= M + 0.5 - A
            y = func
            t_x = [i for i in np.arange(0, 20 + 0.001)]  # 0.001 is aimed to get the boundary point
            p1 = np.array(list(map(y, t_x, [A]*len(t_x), [d]*len(t_x))))   # cross with axis x
            list1 = f(p1)
            x = np.linspace(-50, 50, 10000)
            y1 = func(x, A, d)
            line = plt.plot(x, y1, label='发射电极位置:{}，AO:{}'.format(A, d))
            for l in list1:
                plt.fill_between(l[0], l[1], l[2], color = line[0].get_color(), alpha=0.3)
                # plt.scatter([i[0] for i in p2], [i[1]for i in p2], c='g')

# ---------测试单条曲线----------------
if not switch:
    def func(x):
        return 1/x+0.5
    x = np.linspace(-50, 50, 10000)
    t_x = [i for i in np.arange(0.001, 20 + 0.001)] 
    p1 = np.array(list(map(func, t_x))) 
    list1 = f(p1)
    y = func(x)
    plt.plot(x, y)
    for l in list1:
        plt.fill_between(l[0], l[1], l[2], color = 'green', alpha=0.3)
# -------------------------------------


mesh  = np.full((20, 20), int(10), dtype=np.int8)
delta_x = 0.25
plt.xlim(-2, 20)  # 设置x轴范围
plt.ylim(-0.1, 10)  # 设置y轴范围
my_x_ticks = np.arange(-2, 20, 1)
my_y_ticks = np.arange(0, 10, 1)
plt.xticks(my_x_ticks)
plt.yticks(my_y_ticks)
plt.imshow(mesh, cmap=plt.cm.hot, interpolation='nearest', vmin=0, vmax=10)
plt.grid(True)
plt.legend()
plt.show()

 