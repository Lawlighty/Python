#并行下载
import queue
from threading import Thread
import time
import requests
from tqdm import tqdm
from multiprocessing import Pool,Process
import sys
sys.path.append(r'C:\Users\Administrator\Desktop\python\Py_webSpider\并发串行')
from getAllNet import getUrlList


def downLoadHtml(url):

        headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3676.400 QQBrowser/10.4.3505.400'
        }

        try:
            r = requests.get(url,headers=headers, timeout=1).text
            # r.raise_for_status()

        except Exception as e:
            print(e)
if __name__ == '__main__':
    urllist = getUrlList()
    urllist = urllist[:100]

    start = time.time()
    p = Pool()
    p.map(downLoadHtml, urllist)
    #plan B----------
    # for url in urllist:
    #     p.apply_async(downLoadHtml, (url,))
    # p.close()
    # p.join()
    end = time.time()

    print('多进程下载用时:{}'.format(end - start))
