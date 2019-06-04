## 网页注册流程

1. 获得表单内容-------parser_form(html)
2. 获得验证码图片-----get_captcha_img(html)

           mg_scr = doc.xpath('//*[@id="recaptcha"]/img/@src')[0].split(',')[-1]
           img_data = base64.b64decode(img_scr)
           img = Image.open(BytesIO(img_data))
           
3. 获得验证码---------get_captcha(img)

          img = img.convert('L')
          #图片黑白分离
          img = img.point(lambda x: 0 if x < 1 else 255, '1')

    captcha = pytesseract.image_to_string(img)
4. 提交表单----------session.post()
5. 判断是否成功---错误则输出表单错误提示信息


        if not succ:

          errors = etree.HTML(str(resp.text)).xpath('//div[@class="error"]')
          print('Form Error:')
          print('\n'.join('{}:{}'.format(e.get('id'),e.text) for e in errors))
        else:
          print('注册成功 emial--{},password--{}'.format(e_mail,password))

