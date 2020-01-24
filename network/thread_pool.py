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
] * 10



if __name__=='__main__':
    processPool = ProcessPool(4)
    begin = time.time()
    processPool.map(get_html, urls)
    print(time.time() - begin)
    # 3.1490976810455322 2.721813440322876 2.2875263690948486
    threadPool = ThreadPool(4)
    begin = time.time()
    threadPool.map(get_html, urls)
    # 1.6901259422302246 1.0036718845367432
    print(time.time() - begin)

