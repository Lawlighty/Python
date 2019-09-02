### 这里有一个网站，里面有一些数字。把这些数字的总和，输入到答案框里面，即可通过本关。

#### 本题主要在于模拟登陆
* 在 http://glidedsky.com/login 登录页面获得 提交数据的必要信息  _token
* 构造表单数据 form_data
* 使用requests.Session.post提交信息
* get到第一题url  http://glidedsky.com/level/web/crawler-basic-1
* 获得数字求和
