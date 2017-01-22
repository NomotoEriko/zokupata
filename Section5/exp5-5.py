import random
import sys
from math import log
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def make_r(n=10000):
    random.seed()
    odd = 0
    even = 0
    for i in range(n):
        s = random.random()
        if s < 0.1:
            if random.random() < 0.8:
                odd += 1
            else:
                even += 1
        elif s < 0.5:
            if random.random() < 0.6:
                odd += 1
            else:
                even += 1
        else:
            if random.random() < 0.3:
                odd += 1
            else:
                even += 1
    return odd, even
def draw(x, y):
    plt.plot([0.01*i for i in range(101)], [(17-50*i)/30 for i in range(101)], color="k")
    plt.plot(x, y, "bo")

if __name__ == '__main__':
    # piを推定する。thetaは既知

    # アニメーション描画用
    ani_pi1 = []
    ani_pi2 = []
    fig = plt.figure()
    ani_ims = []
    name = 'LearningCource_'
    # piの初期化
    args = sys.argv
    pi = [None for _ in range(3)]
    for i, val in enumerate(args[1:]):
        pi[i] = float(val)
    for i, val in filter(lambda x: x[1] is None, enumerate(pi)):
        pi[i] = float(input('Initialize pi'+str(i+1)+'>>'))
    name += str(pi[0])+"_"+str(pi[1])+'_'+str(pi[2])+'.png'
    ani_pi1.append(pi[0])
    ani_pi2.append(pi[1])
    ani_ims.append(plt.plot(ani_pi1, ani_pi2, "bo"))

    # 試行回数10000回. 奇数目が出た回数r1, 偶数目が出た回数r2
    n = 10000
    r = make_r(n)
    # thetaの初期化ってか値の格納
    theta = [[0.8, 0.2], [0.6, 0.4], [0.3, 0.7]]
    # 初期値での対数尤度logP(x)
    pv = [0, 0]
    for k in range(2):
        for i in range(3):
            pv[k] += pi[i]*theta[i][k]
    lpx = 0
    for k in range(2):
        lpx += r[k]*log(pv[k])
    p = [[None, None] for _ in range(3)]  # p[i][k] = P(omega_i|v_k)
    while(True):
        # 教師なし学習アルゴリズム(教科書p95に沿ってpiを推定)
        # step2: P(omega_i|v_k)の計算
        for k in range(2):
            m = 0
            for i in range(3):
                m += pi[i]*theta[i][k]
            for i in range(3):
                p[i][k] = pi[i]*theta[i][k]/m

        # step3-1: piの更新(hpi)
        hpi = [0 for _ in range(3)]
        for i in range(3):
            for k in range(2):
                hpi[i] += r[k]*p[i][k]
            hpi[i] /= n

        # step4: P(v_k)の対数尤度の変化量が閾値(0.0001)以下なら終了, それ以外なら続ける
        # 新しい値での対数尤度hat_logP(x)
        pv = [0, 0]
        for k in range(2):
            for i in range(3):
                pv[k] += hpi[i] * theta[i][k]
        hlpx = 0
        for k in range(2):
            hlpx += r[k] * log(pv[k])
        ani_pi1.append(hpi[0])
        ani_pi2.append(hpi[1])
        ani_ims.append(plt.plot(ani_pi1, ani_pi2, "bo"))
        if hlpx - lpx < 0.000000001:
            break
        else:
            lpx = hlpx
            pi = hpi
    ani = animation.ArtistAnimation(fig, ani_ims, interval=50)
    plt.plot([0.01 * i for i in range(101)], [(17 - 50 * i*0.01) / 30 for i in range(101)], color="k")
    plt.plot([0.1], [0.4], "ro")
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.xlabel('pi1')
    plt.ylabel('pi2')
    plt.savefig(name)
    if 'y' in input('show as gif(y or n)>>'):
        plt.show()
    # ani.save("animation.gif")
