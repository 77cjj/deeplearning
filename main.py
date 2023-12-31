import numpy as np
import matplotlib.pylab as plt
#测试变更是否有效
def sigmoid(x):
    return 1/(1+np.exp(-x))

def softmax1(a):#分类问题激活函数
    exp_a=np.exp(a)
    sum_exp_a=np.sum(exp_a)
    y=exp_a/sum_exp_a
    return  y

def softmax2(a):#分类问题激活函数
    c=np.max(a)#溢出对策
    exp_a=np.exp(a-c)
    sum_exp_a=np.sum(exp_a)
    y=exp_a/sum_exp_a
    return  y

def mean_squared_error(y,t):#均方误差
    return 0.5*np.sum((y-t)**2)

def cross_entropy_error(y,t):#交叉熵误差
    if y.ndim==1:#求单个数据的交叉熵误差
        t=t.reshape(1,t.size)
        y=y.reshape(1,y.size)
    batch_size=y.shape[0]
    return -np.sum(t*np.log(y+1e-7))/batch_size

import sys, os
sys.path.append(os.pardir)  # 为了导入父目录的文件而进行的设定
from dataset.mnist import load_mnist

(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)

train_size=x_train.shape[0]
batch_size=10
batch_mask=np.random.choice(train_size,batch_size)
x_batch=x_train[batch_mask]
t_batch=t_train[batch_mask]

print(x_train.shape)
print(t_train.shape)
print(x_test.shape)
print(t_test.shape)
t=np.array([0,0,1,0,0,0,0,0,0,0])
y2=np.array([0.1,0.05,0.6,0,0.05,0.1,0,0.1,0,0])
y7=np.array([0.1,0.05,0.1,0,0.05,0.1,0,0.6,0,0])
print(mean_squared_error(y2,t))
print(mean_squared_error(y7,t))
