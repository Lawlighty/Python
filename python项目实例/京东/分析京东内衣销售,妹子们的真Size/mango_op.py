# 数据库操作
import pymongo
import json
from flush_data import flush_data
mongo_url = 'mongodb://localhost:27017/'
mongo_db = 'wenxiong'
mongo_collection = 'jd_wenxiong'
client = pymongo.MongoClient(mongo_url)
db = client[mongo_db]
coll = db[mongo_collection]
def save_into_mongo(comment):
    """
    写入MongoDB
    :param comment: 评论
    :return:
    """
    # 颜色
    productColor = flush_data(comment['productColor'])
    # 尺寸
    productSize = flush_data(comment['productSize'])
    #评论详情
    content = comment['content']
    # 时间
    creationTime = comment['creationTime']
    myinfo={
        'productColor':productColor,
        'productSize':productSize,
        'content':content,
        'creationTime':creationTime
    }
    try:
        coll.insert_one(myinfo)
        print('数据库插入成功')
    except Exception as e:
        print('插入数据失败')
        print(e)

def get_count(k, v):
    try:
        num = coll.find({k:v}).count()
        return num
    except Exception as e:
        print(e)
