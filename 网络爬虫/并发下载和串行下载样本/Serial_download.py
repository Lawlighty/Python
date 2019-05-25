from getAllNet import getUrlList
import time
import requests
from tqdm import tqdm

def downLoadHtml(url):
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3676.400 QQBrowser/10.4.3505.400'
    }
    try:
        r = requests.get(url,headers=headers).text
        # r.raise_for_status()

    except Exception as e:
        print(e)


if __name__ == '__main__':
    mylist = getUrlList()
    mylist = mylist[:100]

    start = time.time()
    for i in tqdm(mylist):
        try:
            downLoadHtml(i)
        except :
            continue
        time.sleep(0.5)
    end = time.time()

    print('串行下载用时:{}'.format(end-start))
    # 串行下载用时: 1003.6654064655304