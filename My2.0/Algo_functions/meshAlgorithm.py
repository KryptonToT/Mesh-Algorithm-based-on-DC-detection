import numpy as np
from math import floor

class Mesh:
    def __init__(self, size, resistance) -> None:
        mesh = [[] for _ in range(size)]
        

    def Ef(self):  # Mesh resistence value
        L_AO = self.M + (self.N - self.M) / 2 - self.A
        y = lambda x: (L_AO ** 2 - (x + self.A) ** 2) ** 0.5  # Curve of resident
        y_ = lambda x: (L_AO ** 2 - x ** 2) ** 0.5 - self.A
        d = L_AO - self.A  # forward detection distance
        if d > 0:
            t_x = [i for i in np.arange(0, y_(0) + 0.001, delta_x)]  # 0.001 is aimed to get the boundary point
            t_y = [i for i in np.arange(0, y(0) + 0.001, delta_x)]  # Coordinate
            # cross_point(y, y_, t_x, t_y):
            p1 = np.array(list(map(y, t_x))) / delta_x  # cross with axis x
            p2 = np.array(list(map(y_, t_y))) / delta_x  # cross with axis y
            for column, row in enumerate(p1):  # Assignment through point1
                if row != int(row):
                    row = floor(row)
                    if column == 0:
                        mesh[row][column].append(rho)
                    elif column != 0:
                        mesh[row][column].append(rho)
                        mesh[row][column - 1].append(rho)
                elif row == int(row):  # int part
                    r_int = int(row)
                    if r_int == 0:
                        mesh[r_int][column].append(rho)
                        mesh[r_int][column - 1].append(rho)
                    else:
                        if column != 0:
                            mesh[r_int - 1][column - 1].append(rho)
                            mesh[r_int][column - 1].append(rho)
                        mesh[r_int][column].append(rho)
                        mesh[r_int - 1][column].append(rho)
                        
            for row, column in enumerate(p2):  # Assignment through point2
                if column == int(column):  # int part
                    column_int = int(column)
                    if row == 0:
                        mesh[row][column_int].append(rho)
                        mesh[row][column_int - 1].append(rho)
                    else:
                        if column_int != 0:
                            mesh[row][column_int - 1].append(rho)
                            mesh[row - 1][column_int - 1].append(rho)
                        mesh[row][column_int].append(rho)
                        mesh[row - 1][column_int].append(rho)
                        
                elif column != int(column):  # nonint part
                    column_f = floor(column)
                    mesh[row][column_f].append(rho)
                    mesh[row - 1][column_f].append(rho)
        else:
            pass