import pytest



def woda(wysokosci):
    nie_na_koncu = True
    wynik = 0
    pozycja = 0
    while nie_na_koncu:

        g = wysokosci[pozycja]
        t2 = True
        d = []
        miejsce_pomiedzy = 0
        while t2:
            pozycja += 1
            miejsce_pomiedzy += 1
            if wysokosci[pozycja] >= g:
                wynik += g * (miejsce_pomiedzy - 1) - sum(d)
                t2 = False
            elif pozycja + 1 == len(wysokosci):
                nie_na_koncu = False
                wynik += wysokosci[pozycja] * (miejsce_pomiedzy - 1) - sum(d)

                if wynik < 0:
                    wynik = 0
                print(wynik)
                return wynik
            else:
                d.append(wysokosci[pozycja])
        if pozycja + 1 == len(wysokosci):
            nie_na_koncu = False
    if wynik < 0:
        wynik = 0
    print(wynik)
    return wynik


def woda2(n):
    nl = [0]
    for i in range(len(n)):
        if i != 0:
            if n[i - 1] > nl[-1]:
                nl.append(n[i - 1])
            else:
                nl.append(nl[-1])
    np = [0]
    n.reverse()
    for j in range(1,len(n)):
        if n[j - 1] > np[-1]:
            np.append(n[j - 1])
        else:
            np.append(np[-1])
    np.reverse()
    n.reverse()
    w = 0
    # print(np)
    # print(nl)
    for i in range(1, len(n) - 1):
        b = min(np[i], nl[i])
        if n[i] < b:
            w += b - n[i]

    return w


# woda([1, 2, 1])
woda2([3, 1, 5, 2, 1, 1, 3])


# woda([2, 1, 2])
# woda([1, 2, 3, 2, 1])
# woda([2, 1, 3, 0, 2, 5])
# woda([3,0,0,2])
# woda([4,0,2,0,1])


@pytest.mark.parametrize('l,wynik', [
    ([1, 2, 1], 0),
    ([2, 1, 2], 1),
    ([4,0,2,0,1], 3)
])
def test_woda(l, wynik):
    assert woda2(l) == wynik
