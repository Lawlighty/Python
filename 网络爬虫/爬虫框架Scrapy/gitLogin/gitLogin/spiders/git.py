# -*- coding: utf-8 -*-
import scrapy
import logging

class GitSpider(scrapy.Spider):
    name = 'git'
    allowed_domains = ['https://github.com/']
    # start_urls = ['https://github.com/login']
    def start_requests(self):
        return [
            scrapy.Request("https://github.com/login",
                        meta={'cookiejar': 1}, callback=self.post_login)
        ]

    def post_login(self, response):
        # 先去拿隐藏的表单参数authenticity_token
        authenticity_token = response.xpath('//input[@name="authenticity_token"]/@value').extract_first()
        logging.info('authenticity_token=' + authenticity_token)
        return [
            scrapy.FormRequest.from_response(
                  response,
                  url='https://github.com/session',
                  meta={'cookiejar': response.meta['cookiejar']},
                  formdata={
                      'commit': 'Sign in',
                      'utf8':'✓',
                      'authenticity_token':authenticity_token,
                      'login':'***',
                      'password':'***',
                  },
                  callback=self.git_ok,
                  dont_filter=True
                  )
        ]

    def git_ok(self, response):

        try:
            img = response.xpath('//img[@alt="@Lawlighty"]')
            if(img):
                print('登录成功')
        except :
            print('登录失败')



