from 存储模块 import RedisClient
import aiohttp  #异步请求库    request是同步请求库
import asyncio
import time

test_url = 'http://www.baidu.com'

class Tester():
    def __init__(self):
        self.redis = RedisClient()

    async def test_signal_proxy(self, proxy):
        """
        异步测试单个代理
        :param proxy: 代理
        :return: 无
        """
        conn =aiohttp.TCPConnector(verify_ssl=False)
        async with aiohttp.ClientSession(connector=conn) as session:
            try:
                if isinstance(proxy, bytes):
                    proxy = proxy.decode('utf-8')
                real_proxy = "http://"+proxy
                print("现在测试:",real_proxy)

                async with session.get(test_url ,proxy=real_proxy, timeout=10) as response:
                    if response.status == 200:
                        self.redis.beMaxScore(proxy)
                        print("{}代理可用".format(proxy))
                    else:
                        self.redis.decrease(proxy)
                        print('{}状态码不合法'.format(proxy))

            except Exception as e:
                self.redis.decrease(proxy)#减分
                print('代理请求失败',proxy)

    def run(self):
        """
        测试主函数
        :return: none
        """
        print('测试器开始测试')
        try:
            proxies = self.redis.getAll()
            loop = asyncio.get_event_loop()
            for i in range(0,len(proxies),10):
                test_proxies = proxies[i:i+10]
                tasks = [self.test_signal_proxy(proxy) for proxy in test_proxies]
                loop.run_until_complete(asyncio.wait(tasks))
                time.sleep(5)
        except Exception as e:
            print('测试器错误',e)
