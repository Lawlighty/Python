# 使用 Redis 的Sorted Set(有序集合)保存IP地址数据
import redis
from random import choice


max_score = 100
begin_score = 10
min_score = 0
redis_key = 'proxies'#集合名

class RedisClient():

    def __init__(self):
        """
            初始化
            host:Redis 地址
            port:Redis 端口
            password:Redis 密码
            """
        self.mydb = redis.StrictRedis(host='localhost',port=6379, password="",decode_responses=True,db=0)

    def add(self, proxy, score=begin_score):
        """
        添加代理,
        :param proxy: 代理
        :param socre: 分数
        :return: 添加结果
        """
        if not self.mydb.zscore(redis_key, proxy):#返回有序集中，成员的分数值
            return self.mydb.zadd(redis_key, score, proxy)#添加(集合,分数,名称)

    def random(self):
        """
        随机选取有效代理,分数从高到低
        :return: 随机获取的代理
        """
        res = self.mydb.zrangebyscore(redis_key, max_score, max_score)  #返回有序集合中指定分数区间的成员列表。有序集成员按分数值递增(从小到大)次序排列。
        if len(res):
            return choice(res)
        else:
            res = self.mydb.zrangebyscore(redis_key,min_score,max_score)
            if len(res):
                return choice(res)
            else:
                return IPPoolError

    def decrease(self,proxy):
        """
        测试代理失败一次减一分,到0分 就移除ip
        :param proxy: 代理
        :return: 修改后的代理分数
        """
        score = self.mydb.zscore(redis_key, proxy)#获得指定分数
        if score and score>min_score:
            print('代理:',proxy," 当前分数:",score,"分数-1")
            return self.mydb.zincrby(redis_key ,proxy, -1)  #对有序集合中指定成员的分数加上增量
        else:
            print('代理:', proxy, " 当前分数:", score, "剔除")
            return self.mydb.zrem(redis_key, proxy)#移除

    def existsIp(self,proxy):
        """
        判断是否存在于数据库
        :param proxy: 代理
        :return: 是否
        """
        return not self.mydb.zscore(redis_key, proxy)==None

    def beMaxScore(self,proxy):
        """
        代理测试成功则设置为100分
        :param proxy: 代理
        :return: 结果
        """
        print('代理:',proxy,"可用, 设置为",max_score)
        return self.mydb.zadd(redis_key, max_score, proxy)

    def countIp(self):
        """
        返回数量
        :return: 数量
        """
        return self.mydb.zcard(redis_key)   #获取有序集合的成员数

    def getAll(self):
        """
        获取全部代理
        :return: 代理列表
        """
        return self.mydb.zrangebyscore(redis_key, min_score, max_score)
