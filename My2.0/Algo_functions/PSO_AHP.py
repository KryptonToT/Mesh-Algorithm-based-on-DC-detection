import numpy as np
import random
import matplotlib.pyplot as plt

class PSO_AHP():
    def __init__(self, arr):
        self.arr = arr
        self.n = self.arr.shape[0]
        self.step = 3000
        self.PosNum = 70
        self.c1 = 2
        self.c2 = 2
        self.errors = []  # 添加一个用于存储每次迭代误差的列表
        self.g_best = None
        self.p_best = np.zeros(self.n)
        self.p_v = np.zeros((self.PosNum, self.n))
        self.p_pos = np.zeros((self.PosNum, self.n))
        self.initialize()

    def initialize(self):
        r = random.randint(0, self.n-1)
        for i in range(self.PosNum):
            self.p_pos[i] = np.random.rand(self.n)
            self.p_pos[i] = self.nor(self.p_pos[i])
            self.p_v[i][:r] = np.random.rand(r)/10 - 0.1
            self.p_v[i][r:] = np.random.rand(self.n-r)/10
        self.p_best = np.copy(self.p_pos[0])
        for i in range(1, self.PosNum):
            if self.function(self.p_best) > self.function(self.p_pos[i]):
                self.p_best = np.copy(self.p_pos[i])
        self.g_best = np.copy(self.p_best)

    def search(self):
        for j in range(self.step):
            w = 0.9 - (j/self.step) * 0.5
            current_error = self.function(self.g_best)
            self.errors.append(current_error)
            for i in range(self.PosNum):
                for k in range(self.n):
                    rand1 = np.random.rand()
                    rand2 = np.random.rand()
                    self.p_v[i][k] = w*self.p_v[i][k] + self.c1*rand1*(self.p_best[k]-self.p_pos[i][k]) + self.c2*rand2*(self.g_best[k]-self.p_pos[i][k])
                    self.p_pos[i][k] += self.p_v[i][k]
            self.p_best = np.copy(self.p_pos[0])
            for i in range(self.PosNum):
                if self.function(self.p_best) > self.function(self.p_pos[i]):
                    self.p_best = np.copy(self.p_pos[i])
            if self.function(self.g_best) > self.function(self.p_best):
                self.g_best = np.copy(self.p_best)
        self.g_best = self.nor(self.g_best)
        self.g_best = np.round(self.g_best, 3)
        self.plot_errors()
        return self.g_best

    def function(self, x):
        y = 0
        for i in range(1, self.n):
            tmp = np.sum(self.arr[i] * x)
            y += np.abs(tmp - self.n * x[i])
        return y / self.n

    def nor(self, x):
        sum_x = np.sum(np.abs(x))
        return np.abs(x) / sum_x
    
    def plot_errors(self):
        plt.plot(self.errors)
        plt.xlabel('迭代次数')
        plt.ylabel('一致性指标值')
        plt.title('一致性指标优化曲线图')
        plt.show()


if __name__ == "__main__":
    a = np.array([
            [1, 5, 5, 2],
            [1/5, 1, 3, 1],
            [1/5, 1/3, 1, 1/2],
            [1/2, 1, 2, 1]
            ])
    pos_ahp = PSO_AHP(a)
    print(type(pos_ahp.search()))
