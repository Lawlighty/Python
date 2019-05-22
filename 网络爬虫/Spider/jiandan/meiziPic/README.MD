demo.py是草稿箱
这次实验是使用scrapy爬取网络图片并保存 遇到的问题还是蛮多的<br>
 \t 1.首先爬取的图片链接可能类似于:[//ww3.sinaimg.cn/large/0073ob6Ply1g3a3rvr2llj30u0140kjl.jpg] 没有http:开头
拼接之后 形成的url 为字符串类型 也就是这个原因 在加入item['']  后scrapy的爬取出现类似:incalid url'h':no schema supplied.perhaps you meant http://h?
的问题   解决方案是把 url 加入一个list中 ,之后 item['']=list
详见:img_urls = ol.xpath('.//div[@class="text"]/p/img/@src').extract_first()

            img_urls = 'http:'+img_urls

            mylist = []
            mylist.append(img_urls)

            myItem['img_urls'] = mylist
            
  \t2.lis = doc.xpath('//div/ul/li[not(@class="cc" or @class="dd")]/text()')的xpath方法可以爬取li标签中class属性不是cc或者dd
虽然这里不需要

 \t 3.settings.IMAGES_STORE 的使用需要在settings.py 添加IMAGES_STORE=r'C:'路径
  
  \t4.二进制文件保存 使用 r.content
