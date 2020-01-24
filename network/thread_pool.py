import time
from multiprocessing import Pool as ProcessPool
from multiprocessing.dummy import Pool as ThreadPool
import requests

def get_html(url):
    # begin = time.time()
    r = requests.get(url)
    # print(time.time() - begin)
    # print(r.content)

urls = [
    'http://google.com',
    'http://yandex.ru',
    'http://mail.ru'
] * 5000

def calc_smthg(data):
    a = 0
    for i in range(10000):
        a += i

if __name__=='__main__':
    # processPool = ProcessPool(4)
    # begin = time.time()
    # processPool.map(get_html, urls)
    # 3.1490976810455322 2.721813440322876 2.2875263690948486
    # processPool.map(calc_smthg, urls)
    # 1.2158091068267822 1.0486974716186523 1.0366904735565186
    # print(time.time() - begin)
    # threadPool = ThreadPool(4)
    # begin = time.time()
    # threadPool.map(calc_smthg, urls)
    # 0.061040401458740234 0.05603742599487305  0.052034616470336914
    # threadPool.map(get_html, urls)
    # 1.6901259422302246 1.0036718845367432
    # print(time.time() - begin)