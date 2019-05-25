#并行下载
import queue
from threading import Thread
from getAllNet import getUrlList
import time
import requests
from tqdm import tqdm

def downLoadHtml(myqueue):
    while not myqueue.empty():
        headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3676.400 QQBrowser/10.4.3505.400'
        }
        url = myqueue.get()
        try:
            r = requests.get(url,headers=headers).text
            # r.raise_for_status()

        except Exception as e:
            print(e)
if __name__ == '__main__':
    urllist = getUrlList()
    urllist = urllist[:100]
    myqueue = queue.Queue()
    for i in urllist:
        myqueue.put(i)
    qlen = myqueue.qsize()
    print('队列长度:',qlen)
    start = time.time()
    #五个线程
    while not myqueue.empty():
        for i in tqdm(urllist):
            myThread = [Thread(target=downLoadHtml, args=(myqueue,)) for x in range(5)]
            for j in myThread:
                j.setDaemon(True)
                j.start()
                time.sleep(1)
        # myqueue.join()

    end = time.time()

    print('并发下载用时:{}'.format(end - start))
    # 并发下载用时: 500.5996322631836
