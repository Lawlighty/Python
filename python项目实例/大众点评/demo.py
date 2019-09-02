import request

def getHtmltext(url):
    headers={
        'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36',
        'referer':'http://www.dianping.com/',
    }
    try:
        r = request.g
    except Exception as e:
        primt(e)