from functions import beta_distribution as beta
from matplotlib import pyplot as plt
import random
def draw(a, b, name=None):
    if name is not None:
        plt.clf()
    x = [0.001*i for i in range(1001)]
    y = [beta(i, a, b) for i in x]
    plt.plot(x, y)
    if name is not None:
        plt.savefig(name)

if __name__ == '__main__':
    random.seed()
    # 計測回数の効果
    draw(1, 1, 'Be(1,1).png')
    draw(2, 1, 'Be(2,1).png')
    draw(3, 1, 'Be(3,1).png')
    draw(4, 1, 'Be(4,1).png')
    draw(5, 1, 'Be(5,1).png')
    draw(5, 2, 'Be(5,2).png')
    draw(6, 2, 'Be(6,2).png')
    draw(7, 2, 'Be(7,2).png')
    draw(7, 3, 'Be(7,3).png')
    draw(8, 3, 'Be(8,3).png')
    draw(8, 4, 'Be(8,4).png')

    a, b = 8, 4
    plt.clf()
    draw(1, 1)
    draw(a, b)
    for i in range(10, 100):
        if random.random() < 0.8:
            a += 1
        else:
            b += 1
    draw(a, b)
    for i in range(100, 1000):
        if random.random() < 0.8:
            a += 1
        else:
            b += 1
    draw(a, b)
    plt.savefig('enp4-7-(1).png')

    # 事前分布の効果
    random.seed()
    plt.clf()
    a, b = 3, 9     # 事前分布にBe(3,9)を適用
    draw(a, b)
    a += 8
    b += 4
    draw(a, b)
    for i in range(10, 100):
        if random.random() < 0.8:
            a += 1
        else:
            b += 1
    draw(a, b)
    for i in range(100, 1000):
        if random.random() < 0.8:
            a += 1
        else:
            b += 1
    draw(a, b)
    plt.savefig('enp4-7-(2-1).png')

    random.seed()
    plt.clf()
    a, b = 31, 21    # 事前分布にBe(31,21)を適用
    draw(a, b)
    a += 8
    b += 4
    draw(a, b)
    for i in range(10, 100):
        if random.random() < 0.8:
            a += 1
        else:
            b += 1
    draw(a, b)
    for i in range(100, 1000):
        if random.random() < 0.8:
            a += 1
        else:
            b += 1
    draw(a, b)
    plt.savefig('enp4-7-(2-2).png')
