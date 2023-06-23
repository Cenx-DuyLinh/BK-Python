from PID_Kalman_Module import Kalman
import matplotlib.pyplot as plt
import numpy as np

kalmanfilter = Kalman()
samples = 2000
t = np.linspace(0,100,samples)
x = 0.8*np.sin(t/(16*np.pi))
noise = np.random.normal(0,0.1,samples)
X = x + noise
X_kalman = []
for i in range(samples):
    x_kalman = kalmanfilter.Filter(X[i])
    X_kalman.append(x_kalman[0])

plt.plot(t,X, c='r')
plt.plot(t,x, c='b')
plt.plot(t,X_kalman,c='g')
plt.show()