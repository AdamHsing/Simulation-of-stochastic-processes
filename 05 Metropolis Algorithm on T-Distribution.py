from math import *
import matplotlib.pyplot as plt

# 给定提议分布（purposal distribution）的初始常模
global sigma
sigma = eval(input('please enter the standared diviation of the purposal distribution:'))

# 给定目标分布的初始常模
global df 
df = eval(input('please enter the degree of freedom of the objection distribution:'))

# 定义提议分布 | 常用正态分布
def q(i,j):
    qij = exp(-(i-j)**2/(sigma**2))/(np.sqrt(2*np.pi)*sigma)
    return qij

# 定义目标分布 | 以t分布为例
def p(i):
    pi = gamma((df + 1)/2)/(np.sqrt(df*np.pi)*(gamma(df/2)))*(1+i**2/df)**(-(df+1)/2)
    return pi

# 定义接受概率
def a(i,j):
    alpha = p(j) * q(i,j)
    return alpha

# 主函数
## 给定迭代次数
T = 10000

## 定义储存数组
i = np.zeros(T)
i[0] = np.random.rand()

for t in range(T-1):
    # 在i[t]的条件下随机生成一个j
    j = np.random.normal(i[t],sigma)
    # 生成随机决定是否转换到j的判断条件
    u = np.random.rand()
    # 计算接受概率
    alpha = a(i[t],j)
    # 判断是否转移
    if (u <= alpha):
        i[(t+1)] = j
    else:
        i[(t+1)] = i[t]

## 作图
x = np.arange(-10,10,1);

obj = p(x)*10000

plt.plot(x,obj,'r')
plt.hist(i,bins=x)

plt.show()
