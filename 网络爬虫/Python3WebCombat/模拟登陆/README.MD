### 模拟登陆思维流程
* 模拟登陆的话我们需要构造表单
* 根据https://github.com/session得到表单需要信息

      data = {
                  'commit':'Sign in',
                  'utf8':'✓',
                  'authenticity_token':self.get_authtoken(),
                  'login':username,
                  'password':password,
                  'webauthn-support':'supported',

              }
              
* 分析data,我们需要构造authenticity_token
* https://github.com/login页面有authenticity_token隐藏信息,又我们登陆时附带,此时我们就需要session保持,并且获得cookie

* 至此我们构造好了data信息,通过post()提交表单
* 通过检验页面信息判断是否模拟登陆成功
