## 测试charles抓包工具的使用,浅爬汽车之家app 二手车板块主页面
* charles 获得url='https://m.che168.com/youxuan/110000/110100/index.html?sourcename=mainapp&safe=1&isautoapp=1&pvareaid=107748'
* 顺便 设置一下


      headers={
        'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Mobile/14D27 auto_iphone/9.12.5 nettype/wifi autohomeapp/1.0 (auto_iphone;9.12.5;tFE3RQtL8w7XbmvPFh6q4-EdvbEnm2lfY-NnSITwNPmuTVwrfYkRr30PG9XBR_pUzfMG_JX-DWfxF_iOZx-xpsJMf_O5y1HIPkBkkiA0JfORj6etqc4asg;10.2.1;iPhone;93D7B5D0A9D73338238053A32524F639)'

      }
     
 * 其他照常  r = requests.get(url, headers=headers, verify=False) ,其中verify=False因为请求的是https 协议，所以请求禁用证书验证
