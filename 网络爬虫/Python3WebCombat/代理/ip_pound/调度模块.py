from multiprocessing import Process
from 存储模块 import RedisClient
from 获取模块 import Crawler,Getter
from 检测模块 import Tester
import time

tester_flag = True
getter_flag = False

class Scheduler():
    def schedule_tester(self, cycle=10):
        """
        定时测试代理
        :param cycle:
        :return:
        """
        tester = Tester()
        while True:
            print('测试器开始')
            tester.run()
            time.sleep(cycle)

    def schedule_getter(self,cycle= 20):#定时获取代理
        getter = Getter()
        while True:
            print('开始抓取')
            getter.run()
            time.sleep(cycle)

    def run(self):
        print('ip池开始运行')
        if  getter_flag:
            getter_process = Process(target=self.schedule_getter())
            getter_process.start()

        if tester_flag:
            tester_process = Process(target=self.schedule_tester())
            tester_process.start()



if __name__ == '__main__':
    aaa = Scheduler()
    aaa.run()
