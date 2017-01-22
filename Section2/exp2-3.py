import random
from matplotlib import pyplot as plt


class Coin:
    def __init__(self, N=None):
        if N is None:
            self.N = random.randint(1, 3)
        else:
            self.N = N if N in (1, 2, 3) else random.randint(1, 3)

        self.ps = {1: 0.1, 2: 0.4, 3: 0.5}
        self.pis = {1: 0.1, 2: 0.4, 3: 0.5}
        self.sitas = {1: 0.8, 2: 0.6, 3: 0.3}
        self.orbit = [[0.1], [0.4], [0.5]]
        self.history = []

    def throw(self):
        if random.random() < self.sitas[self.N]:
            return 'H'
        else:
            return 'T'

    def predict(self):
        ht = self.throw()
        self.history.append(ht)
        mother = 0
        if ht == 'H':
            for j in range(1, 4):
                mother += self.ps[j]*self.sitas[j]
            for ii in range(1, 4):
                self.ps[ii] *= self.sitas[ii] / mother
                self.orbit[ii - 1].append(self.ps[ii])
            return self.ps
        else:
            for j in range(1, 4):
                mother += self.ps[j]*(1-self.sitas[j])
            for ii in range(1, 4):
                self.ps[ii] *= (1 - self.sitas[ii]) / mother
                self.orbit[ii - 1].append(self.ps[ii])
            return self.ps

    def draw(self, name):
        x = range(max([len(el) for el in self.orbit]))
        plt.plot(x, self.orbit[0], label='p1')
        plt.plot(x, self.orbit[1], label='p2')
        plt.plot(x, self.orbit[2], label='p3')
        # plt.ylim(0, 1)
        plt.legend()
        plt.xlabel('n')
        plt.ylabel('Posterior probability')
        plt.savefig(name+'.png')

if __name__ == '__main__':
    N = int(input('Collect Coin Num (1, 2 or 3) >> '))
    coin = Coin(N)
    trial = int(input('trial num >> '))
    for i in range(trial):
        coin.predict()
    coin.draw(input('File name >> '))
