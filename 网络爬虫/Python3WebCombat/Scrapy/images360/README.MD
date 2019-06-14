
## scrapy爬取360图片  url="https://image.so.com/z?ch=beauty"
### 分析网页  滚轮滑动 图片自动加载,证明该网页是动态加载页面 ,前往NetWorK 寻找相应的url
1. 获得url模板 https://image.so.com/zjl?ch=beauty&sn=30&listtype=new&temp=1
2. 分析url 构成
3. 构造scrapy爬取url


          def start_requests(self):
              base_url = 'https://image.so.com/zjl?'
              #url 参数
              data = {
                  'ch':'beauty',
                  'listtype':'new',
                  'temp':1,
              }
              for i in range(1,self.settings.get('MAX_PAGE') + 1):#页数
                  data['sn'] = i*30               #每页的图片数量
                  params = urlencode(data)           #参数转化
                  url = base_url+params
                  yield Request(url, self.parse)

              
### 数据存入mysql数据库, 图片保存到本地文件夹
1. settings 设置 IMAGES_STORE ="./myimagesPic" 表示保存文件的目录
2. 图片保存的pipeline 继承scrapy的ImagesPipeline
   重写方法
   
         def file_path(self, request, response=None, info=None):
          url = request.url
          file_name = url.split('/')[-1]
          return file_name

        #这个方法是在发送下载请求之前调用
        def item_completed(self, results, item, info):
            image_paths = [x['path'] for ok, x in results if ok]
            if not image_paths:
                # 下载失败忽略该 Item 的后续处理 即不保存在数据库
                raise DropItem('Image Downloaded Failed')
            return item

        def get_media_requests(self, item, info):
            yield Request(item['url'])
          
  
3.开启ITEM_PIPELINE,其中保存图片的pipline--Images360PicPipeline数值小于 保存数据库Images360Pipeline,原因是先进行图片保存,当该图片保存错误之后,此图片的信息将不会写入数据库

        ITEM_PIPELINES = {
        'images360.pipelines.Images360Pipeline': 301,
        'images360.pipelines.Images360PicPipeline': 300,
        }

