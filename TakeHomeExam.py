import random
import numpy as np
import scipy.special as scsp


def simulateGame(n, m):
    """
    Calculate P (points of game simulation)
    :param n: cards# for each suit
    :param m: suits#
    :return: P
    """
    cards = []
    for i in range(m):
        cards += [i] * n
    random.shuffle(cards)
    # print(cards)
    prev_card_suit = cards[0]
    p = 0
    for suit in cards[1::]:
        if prev_card_suit == suit:
            p += 1
        prev_card_suit = suit
    return p


def q1():
    p = []
    for i in range(10000):
        p.append(simulateGame(26, 2))
    p = np.array(p)
    print("Mean of P when n=26, m=2:", p.mean())
    print("SD of P when n=26, m=2:", p.std())
    z12 = (12 - p.mean()) / p.std()
    z6 = (6 - p.mean()) / p.std()
    p = (1 - scsp.ndtr(z12)) / (1 - scsp.ndtr(z6))
    print("Conditional probability:", p)

    p = []
    for i in range(10000):
        p.append(simulateGame(52, 4))
    p = np.array(p)
    print("Mean of P when n=52, m=4:", p.mean())
    print("SD of P when n=52, m=4:", p.std())
    z12 = (12 - p.mean()) / p.std()
    z6 = (6 - p.mean()) / p.std()
    p = (1 - scsp.ndtr(z12)) / (1 - scsp.ndtr(z6))
    print("Conditional probability:", p)


if __name__ == "__main__":
    q1()
