import random as rnd
import time


def promien(liczby, wartosci):
    n = len(wartosci)
    si = [0]
    for i in liczby:
        si.append(si[-1] + i)

    wynik = []
    for i, x in enumerate(wartosci):
        k = max(i, n - i)
        p = 0
        w = -1
        while p <= k:
            sr = (p + k) // 2
            il = max(0, i - sr)
            ip = min(n, i + sr + 1)
            obl = si[ip] - si[il]
            if obl >= x:
                w = sr
                k = sr - 1
            else:
                p = sr + 1
        wynik.append(w)
    return wynik


def znajdz_promien(poz, liczby, wartosc, si=None):
    n = len(liczby)
    k = max(poz, n - poz)
    i = 0
    while i <= k:
        il = max(0, poz - i)
        ip = min(poz + i + 1, n)
        if not si:
            w = sum(liczby[il:ip])
        else:
            w = si[ip] - si[il]
        if w >= wartosc:
            return i
        i += 1
    return -1


def promien_naiwny(liczby, wartosci, sumy=False):
    si = None
    if sumy:
        n = len(wartosci)
        si = [0]
        for i in liczby:
            si.append(si[-1] + i)

    res = []
    for i, x in enumerate(wartosci):
        res.append(znajdz_promien(i, liczby, x, si))
    return res


def test_massive(n):
    liczby = rnd.choices(range(100), k=n)
    wartosci = rnd.choices(range(10000), k=n)
    start = time.time()
    w = promien_naiwny(liczby, wartosci)
    koniec = time.time()
    print("Czas wykonania: {:.3f} sekund".format(koniec - start))
    start = time.time()
    w = promien_naiwny(liczby, wartosci, True)
    koniec = time.time()
    print("Czas wykonania: {:.3f} sekund".format(koniec - start))
    start = time.time()
    w = promien(liczby, wartosci)
    koniec = time.time()
    print("Czas wykonania: {:.3f} sekund".format(koniec - start))


def test_basic():
    assert znajdz_promien(0, [2, 3, 1, 4, 2, 1], 6) == 2
    assert znajdz_promien(5, [2, 3, 1, 4, 2, 1], 14) == -1
    assert znajdz_promien(2, [3, 3, 1, 4, 2, 1], 8) == 1
    assert promien_naiwny([2, 3, 1, 4, 2, 1], [6, 3, 8, 8, 10, 14]) == [2, 0, 1, 2, 3, -1]


def test_basic_bin():
    assert promien([2, 3, 1, 4, 2, 1], [6, 3, 8, 8, 10, 14]) == [2, 0, 1, 2, 3, -1]


# test_basic_bin()

test_massive(10 ** 6)
