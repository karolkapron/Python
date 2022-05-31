import matplotlib.pyplot as plt
import numpy as np


def x2():
    x = np.linspace(-10, 10, 100)
    y = x**2

    plt.plot(x, y)

    plt.title('x^2')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid()
    plt.show()

x2()

def sinus():


    x = np.linspace(0, 2*np.pi, 200)
    y = np.sin(x)

    p = plt.subplot()
    p.plot(x, y)
    plt.title('sinus')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid()
    plt.show()


sinus()


def circle():

    circle=plt.Circle((0.5, 0.5), 0.2, facecolor='blue')

    plt.gca().add_patch(circle)

    plt.plot()
    plt.title('Circle')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid()
    plt.show()

circle()