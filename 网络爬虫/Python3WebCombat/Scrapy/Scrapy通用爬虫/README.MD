### 中华科技网https://tech.china.com/  科技-业界-列表 版面https://tech.china.com/articles/ 新闻的爬取
## scrapy   CrawlSpider 框架
* scrapy startproject xxxx
* scrapy genspider -t crawl xxx yy.com
* 配置item
* 定义Rule


        rules = (
          Rule(LinkExtractor(allow=r'/article\/.*\.html', restrict_xpaths='//div[@id="left_side"]//div[@class="con_item"]'), callback='parse_item',follow=False),  每个新闻的html页面
          Rule(LinkExtractor(restrict_xpaths='//div[@id="pageStyle"]//a[contains(text(),"下一页")]'), follow=True) 下一页链接
      )
