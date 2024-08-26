import numpy as np
import matplotlib.pyplot as plt
from labellines import labelLine, labelLines

c = 1
m = 1

def f(x):
    return 0 * x

def f1(px):
    return np.sqrt((m*c)*(m*c) + px*px)    

def f2(px, py):
    return np.sqrt((m*c)*(m*c) + px*px + py*py)

def plot1():
    fig, ax = plt.subplots()

    x = np.linspace(-5, 5, 1000)
    x1 = np.concatenate((x,x), axis=None)
    y = np.concatenate((f1(x), -f1(x)), axis=None)
    plt.scatter(x1, y, c=y, cmap="viridis")
    plt.plot(x, f(x), color='grey')
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.savefig("2DMassShell.png", dpi=500)

def plot2():
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

    x = np.arange(-5, 5, 0.25)
    y = np.arange(-5, 5, 0.25)
    X, Y = np.meshgrid(x, y)
    
    surf = ax.plot_surface(X, Y, f2(0.75*X, 0.75*Y), cmap="coolwarm")

    plt.show()

plot1()
plot2()
