import random
import numpy as np
import scipy.special as scsp
import pandas as pd
from scipy.stats import chisquare


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


def q2():
    mt = pd.read_csv('data/MT_cleaned.csv')
    vt = pd.read_csv('data/VT_cleaned.csv')
    mt['year'] = pd.DatetimeIndex(mt['stop_date']).year
    # print(mt.head())
    print('1.	The proportion of traffic stops in MT involving male drivers:',
          len(mt[mt['driver_gender'] == 'M']) / len(mt))
    chisq, p = chisquare(mt['is_arrested'].to_numpy())
    print('2.	Factor increase in a traffic stop arrest likelihood in MT from OOS plates:', chisq, p)
    print('3.	The proportion of traffic stops in MT involving speeding violations:',
          len(mt[mt['violation'].str.contains('Speeding', na=False)]) / len(mt))
    print('4.	Factor increase in traffic stop DUI likelihood in MT over VT:', 'DUI likelihood is ambiguous')
    print('5.	The average manufacture year of vehicles stopped in MT in 2010 (2020 has not any record):', np.mean(
        mt[(mt['year'] == 2010) & (mt['vehicle_year'] != 'NON-') & (mt['vehicle_year'] != 'UNK')][
            'vehicle_year'].dropna().values.astype(np.int)))
    print('6.	The difference in the total number of stops that occurred between min and max hours in both MT and VT',
          'I don\'t get the meaning of min and max in time format')
    print('7.	The area in sq. km of the largest county in MT:', 'I can\'t find related part in given data')


if __name__ == "__main__":
    q1()
    q2()
