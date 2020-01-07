import numpy as np
import random
import matplotlib.pyplot as plt
# 定义激活函数

class net(object):
    """三层BP神经网络"""
    def __init__(self, ni=28*28, nh=30, no=2, learning_rate=0.5,momentum=0.1, convergence=1e-4):
        self.ni = ni
        self.nh = nh
        self.no = no
        self.learning_rate = learning_rate
        self.momentum_factor = momentum

        #激活所有节点
        self.ele_i = self.ni * [1]
        self.ele_hid = self.nh * [1]
        self.ele_o = self.no * [1]
        random.seed=1
        #权重初始化,生成随机数
        self.wij = np.empty([self.ni, self.nh])
        self.wjk = np.empty([self.nh, self.no])
        for j in range(self.nh):
            for k in range(self.no):
                self.wjk[j,k] = -0.1+0.2*random.random()
            for i in range(self.ni):
                self.wij[i,j] = -0.3+0.6*random.random()
        self.wij_last = self.wij
        self.wjk_last = self.wjk
        self.wij_last_last = self.wij_last
        self.wjk_last_last = self.wjk_last
        # 阈值初始化
        # self.theta = [-1]*self.no
        # self.gamma = [-1]*self.nh
        ## 动量因子

    # 正向传播
    @staticmethod
    def __sigmoid_activation(x):
        return 1 / (1 + np.exp(-x))


    def feedForward(self,input):
        for i in range(self.ni):
            self.ele_i[i] = input[i]
        for j in range(self.nh):
            sum = 0
            for i in range(self.ni):
                sum = sum + self.ele_i[i] * self.wij[i, j]
            self.ele_hid[j] = self.__sigmoid_activation(sum) # - self.gamma[j])

        for k in range(self.no):
            sum = 0
            for j in range(self.nh):
                sum = sum + self.ele_hid[j] * self.wjk[j, k]
            self.ele_o[k] = self.__sigmoid_activation(sum)#- self.theta[k])


    #反向传播
    def backPropagate(self,target):

        err = [0] * self.no
        gk = [0] * self.no
        h_yj = [0] * self.nh
        ej = [0] * self.nh

        for k in range(self.no):
            # 网络第k个输出与理想输出的差
            err[k] =  target[k] - self.ele_o[k]
            gk[k] = self.ele_o[k] * (1 - self.ele_o[k]) * err[k]
        # 梯度下降法调整各层间的权值
        for j in range(self.nh):
            for k in range(self.no):
                h_yj[j] = h_yj[j]+self.wjk[j,k] * gk[k]
            ej[j] = self.ele_hid[j] * (1 - self.ele_hid[j]) * h_yj[j]

        self.wij_last = self.wij
        self.wjk_last = self.wjk
        self.wij_last_last = self.wij_last
        self.wjk_last_last = self.wjk_last

        # 误差传播更新wjk
        for k in range(self.no):
            for j in range(self.nh):
                self.wjk[j,k] = self.wjk[j,k] + self.learning_rate * gk[k]* self.ele_hid[j]\
                                +self.momentum_factor*(self.wjk_last[j,k]-self.wjk_last_last[j,k])
           # self.theta[k] = self.theta[k] - self.learning_rate*gk[k]
        # 误差传播更新wij
        for j in range(self.nh):
            for i in range(self.ni):
                self.wij[i,j] = self.wij[i,j] + self.learning_rate * ej[j]* self.ele_i[i]\
                                +self.momentum_factor*(self.wij_last[i,j]-self.wij_last_last[i,j])
           # self.gamma[j] = -self.learning_rate*h_yj[j] + self.gamma[j]


    # def err_targets(self,times,Inputs,Outputs):
    #     error_target = 0
    #     for time in range(times):
    #         self.feedForward(Inputs[time])
    #         for k in range(self.no):
    #             error_target = error_target + (self.ele_o[k] - Outputs[times][k]) ^ 2 / 2
    #    return error_target/times


    # 根据一组输入和实际输出，训练网络
    def training(self, Inputs,Outputs,times):
        for t in range(times):
            input = Inputs[t,:]
            target = Outputs[t,:]
            # err = [0] * times
            self.feedForward(input)
            self.backPropagate(target)
            print("训练第%d个样本，训练完成 %.2f " % (t, t/times))
            print ("权值wij:" )
            print(self.wij)
            print("权值wjk:\n")
            print(self.wjk)


    # 训练好的权值用于判断输入矩阵的输出
    def test(self,input):
        self.feedForward(input)
        return self.ele_o






