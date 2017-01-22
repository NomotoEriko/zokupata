from functions import dhirichlet as dhir
from mpl_toolkits.mplot3d import Axes3D
from pylab import *
import numpy as np

def draw(alpha1, alpha2, alpha3, name):
    x = []
    y = []
    z = []
    for t in range(101):
        for i in range(101-t):
            xi = 0.01*t
            yi = 0.01*i
            zi = 1-xi-yi
            x.append(xi)
            y.append(yi)
            z.append(dhir([xi, yi, zi], [alpha1, alpha2, alpha3]))
    clf()
    npx = np.arange(101)*0.01
    npy = np.arange(101)*0.01
    npX, npY = meshgrid(npx, npy)
    npz = np.zeros((101, 101))-1
    for i in range(len(x)):
        npz[round(x[i]*100), round(y[i]*100)] = z[i]
    pcolor(npX, npY, npz, cmap='Blues', vmin=-1, vmax=20)
    colorbar()
    xlim(0, 1)
    ylim(0, 1)
    savefig(name)

if __name__ == '__main__':
    x = []
    y = []
    z = []
    for t in range(101):
        for i in range(101-t):
            xi = 0.01*t
            yi = 0.01*i
            zi = 1-xi-yi
            x.append(xi)
            y.append(yi)
            z.append(dhir([xi, yi, zi], [4, 4, 4]))
    # Dir(4,4,4)をθ1, θ2を説明変数(Θ3=1-Θ1-Θ2)として3次元に可視化
    ax = Axes3D(plt.figure())
    ax.plot_wireframe(x, y, z)
    savefig('Dir(4,4,4)3D.png')

    # Dir(α1,α2,α3)をθ1, θ2を説明変数(Θ3=1-Θ1-Θ2)として2次元に濃淡で可視化
    draw(1, 1, 1, 'Dir(1,1,1)2D.png')
    draw(8, 8, 8, 'Dir(8,8,8)2D.png')
    draw(4, 4, 4, 'Dir(4,4,4)2D.png')
    draw(8, 2, 2, 'Dir(8,2,2)2D.png')
    draw(2, 8, 2, 'Dir(2,8,2)2D.png')
    draw(2, 4, 6, 'Dir(2,4,6)2D.png')
