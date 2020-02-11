import numpy as np
import matplotlib.pyplot as plt
from math import factorial as f
  
def dxdy(x,y,order): 
    dy = y
    for k  in range(order+1):
        print(k)
        dx = (x[-1]-x[0])/len(x)
        if k == 1:
            dy = y
        elif k % 2 == 0:
            dy = (dy[1:]-dy[:-1])/dx
            x = x[:-1]       
        elif k % 2 != 0:
            dy = (dy[1:]-dy[:-1])/dx
            x = x[1:]
    return dy

def taylor(x,y,n):
    a = x[int(len(x)/2)+1]
    center = int(len(x)/2)+1o
    #plt.plot(y)
    #plt.ylim(min(y),max(y))
    for k in range(n+1):
        print(k)
        if k == 0:
            y_hat = (y[center]*((x-a)**k))/f(k)
            #plt.plot(y_hat)
        else:
            y_hat += (dxdy(x,y,k+1)[center]*((x-a)**k))/f(k)
            #plt.plot(y_hat)
        #plt.plot(y)
    return y_hat

points = 101
x = np.linspace(-3*np.pi,3*np.pi,points)
y = 1/(1+np.exp(-x))
y = np.cos(x)#*x#(x**4)
center = int(points/2)
for k in range(21):
    y_hat = taylor(x,y,k)
    plt.figure(figsize=(8,4))
    plt.ylim(min(y)*1.1,max(y)*1.1)
    plt.xlim(min(x),max(x))
    plt.plot(x,y)
    plt.plot(x,y_hat,c='red')
    plt.legend(['cs(x)','taylor, k= '+str(k)],loc='upper right')
    plt.title('cos(x)') 
    plt.savefig('cos'+str(k)+'.png')