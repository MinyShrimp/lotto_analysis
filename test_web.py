from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from pprint import pprint

if __name__ == "__main__":
    html = urlopen('https://dhlottery.co.kr/gameResult.do?method=statByNumber')
    obj = bs(html, 'html.parser')
    arr = []

    _tmp = obj.body.find('table', {'id': 'printTarget'}).find_all('td')
    for v in _tmp:
        for _v in v.contents:
            try:
                arr.append(int(_v))
            except TypeError:
                pass
            except ValueError:
                pass
    print(arr)

    f = open('./lotto.txt', 'w')
    for v in arr:
        f.write('{}\n'.format(v))
    f.close()