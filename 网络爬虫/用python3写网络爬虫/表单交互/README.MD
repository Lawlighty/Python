<h3>login.py  登录表单<br>
表单登录需要满足三个条件<br>
  A:表单的提交须填写的内容(显性)+网页表单隐性内容
  
    def loginA(url):#只有表单显性数据提交                         def loginB(url):#只有表单数据提交
      data = {                                                       data={
          'email': '12345@163.com',                                           'email':'12345@163.com',
          'password': '123456abc',                                             'password':'123456abc',
      }                                                                        '_formkey': '6cbb2963-6f71-4dc7-8e33-3c2af9ab8fed',
      r = requests.post(url,data=data)                                          '_formname': 'login'
      print(r.url)                                                          }
                                                                      r  = requests.post(url, data=data)
                                                                      print(r.url)
      
      
      
  获得表单的全部内可以通过 lxml遍历 form  中所有的 input 标签 写入 字典
  
        data ={}

        for i in doc.xpath('//form//input'):
            if i.get('name'):
                data[i.get('name')] = i.get('value')
  
  B:浏览器cookie--------------------->表单某数据中的值会保存在浏览器cookie中 然后该值会与提交的登录表单数据中的值对比
      cookie = request.get(url).cookies
  
  c: 使用request的post()方法                   
