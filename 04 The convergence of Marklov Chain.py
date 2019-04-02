import numpy as np

P = np.array([[.65,.18,.17],
              [.15,.67,.18],
              [.12,.36,.52]])

a = np.random.rand(1)[0]
b = np.random.rand(1)[0]
c = np.random.rand(1)[0]

sumarize = a + b + c

a = a / sumarize
b = b / sumarize
c = c / sumarize

Pi0 = np.array([a, b, c])
Pi = np.dot(Pi0,P)
print(Pi0)

while (abs((Pi - Pi0))[0] >= .00001):
    Pi0 = Pi
    Pi = np.dot(Pi,P)
    print(Pi0)
