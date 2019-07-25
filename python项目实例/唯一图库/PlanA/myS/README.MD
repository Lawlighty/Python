### 记新学到的知识点

* 把scrapy 命令行输出的错误内容存入日志文本文档


            settings.py:
            LOG_LEVEL = 'ERROR'       #输出等级
            LOG_FILE = 'error.log'    #文档位置
            

* 通过  scrapy.Request(url, meta={'new_item':item}, callback=self.parse)<br>
可以把当前parse函数中的item传递到parse_II,<br>
parse_II中通过 item_II = response.meta["new_item"]获得传递的item
