import math
def gamma(a):
    # ガンマ関数(引数は整数のみ対応)(ただの階乗)
    t = 1
    for i in range(1, a):
        t *= i
    return t

def beta_function(a, b):
    # ベータ関数
    return gamma(a)*gamma(b)/gamma(a+b)

def beta_distribution(theta, a, b):
    # ベータ分布
    return math.pow(theta, a-1)*math.pow(1-theta, b-1)/beta_function(a, b)

def dhirichlet(thetas, alphas):
    # ディリクレ分布
    alp = 0
    for al in alphas:
        alp += int(al)
    z = gamma(alp)
    for al in alphas:
        z /= gamma(int(al))
    for th, al in zip(thetas, alphas):
        z *= math.pow(float(th), int(al-1))
    return z

if __name__ == '__main__':
    # ディリクレ分布の関数がちゃんと動くか試し書き(あまり意味がない)
    ts = [float(t) for t in input('thetas >').rstrip().split()]
    l = 1.0
    thetas = []
    for t in ts:
        if 0 > l-t:
            thetas.append(l)
            l -= t
            break
        else:
            thetas.append(t)
            l -= t
    if l > 0:
        thetas.append(l)

    als = [int(t) for t in input('alphas >').rstrip().split()]
    while len(thetas) > len(als):
        als += [int(t) for t in (input('more alphas >').rstrip().split())]
    print(dhirichlet(thetas, als))
