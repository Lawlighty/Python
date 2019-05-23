Sample.py
使用Selenium爬取腾讯漫画

<p>问题记录:
  <p>1.腾讯漫画使用<br>
  js = "var q=document.documentElement.scrollTop=100000"<br>
  self.driver.execute_script(js)
  方法下拉滚动条不知为什么不能成功
  所以使用  键盘按钮下滑<br>
  builder = ActionChains(self.driver)<br>
  builder.key_down(Keys.ARROW_DOWN).perform()
  
  <p>2.保存文件时遇到 os.makedirs()和os.mkdir()的问题,起初使用os.mkdir() 报错不存在文件夹<br>
   百度结果:<br>
  os.makedirs会递归的建立输入的路径，即使是上层的路径不存在，它也会建立这个路径<br>
  而os.mkdir父级路径不存在，那么就会报错。
  
  <p>3.学习不使用自动化工具实现爬取功能
