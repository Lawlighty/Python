## 点触验证码识别使用外接 验证网站API 实现   超级鹰:https://www.chaojiying.com/

### 实现流程
* 登录网站填写相应信息

* 获取网站完整截图
  1. web_shot = self.browser.get_screenshot_as_png()#二进制数据
  2. web_shot = Image.open(BytesIO(web_shot))#二进制封装 
  
* 查询验证码图片位置
  1. top,buttom,left,right = location['y'], location['y']+size['height'], location['x'],location['x']+size['width']
  
* 根据验证码位置切割验证码图片
  1. captcha = web_shot.crop((left, top, right, buttom)) 注意裁剪参数为left, top, right, buttom 顺序为左上右下
  
* 把图片信息发送给 验证网站处理, 获得处理信息
    1.  
    
    
         captcha = self.get_captach_img() # 获得验证码图片
         bytes_array = BytesIO()
         captcha.save(bytes_array, format('png'))
         result = self.chaojiying.PostPic(bytes_array.getvalue(), CHAOJIYING_KIND)#识别验证码
    
    2. 超级鹰返回信息格式:
    
              {'err_no': 0, 'err_str': 'OK', 'pic_id': '3071617002533100014', 'pic_str': '51,60|232,67', 'md5': '7c2755b71fd0c8dc9d8c385c1adfcdc7'}
              
* 解析信息 获得 坐标
    1. groups = captcha_result.get('pic_str').split('|')
    2. locations = [[int(number) for number in group.split(',')] for group in groups]----类似[[51,60],[232,67]]
    
* 根据坐标控制网页点击 实现验证
  1. 获得验证码位置
  2. ActionChains(self.browser).move_to_element_with_offset(element, location[0], location[1]).click().perform()
