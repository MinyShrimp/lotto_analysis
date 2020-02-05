import numpy as np
import scipy.stats as stats
import random

if __name__ == "__main__":
    f = open('./lotto.txt', 'r')
    arr = [ int(_) for _ in f.readlines() ]
    f.close()

    _dic = {}
    for i, v in enumerate(arr):
        _dic[i + 1] = v
    _dic = dict(sorted( _dic.items(), key=lambda k: k[1]))
    std_stats = sorted(stats.zscore(arr))

    n = int(input("Input N : "))
    for i in range(n):
        lotto = []
        _c = 0
        while _c < 7:
            if _c == 6:
                lotto = sorted(lotto)
            _tmp = random.gauss(np.mean(std_stats), np.std(std_stats))
            for k in range(len(std_stats) - 1):
                if _tmp >= std_stats[k] and _tmp < std_stats[k + 1]:
                    if not(list(_dic.keys())[k] in lotto):
                        lotto.append(list(_dic.keys())[k])
                        _c += 1
                        break

        # 출력 : [ No.  1 : [random] ]
        print('No.{:3d} : ['.format(i + 1), end='')
        for _ in lotto:
            print('{:2d}'.format(_), end=", ")
        print('\b\b]')