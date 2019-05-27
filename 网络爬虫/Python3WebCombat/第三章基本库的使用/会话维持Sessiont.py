import requests

url = 'http://httpbin.org/cookies/set/mycookie/123456789'
#向网页设置 一个cookie
requests.get(url)

r= requests.get('http://httpbin.org/cookies')
print(r.text)

print('*'*100)


# Session 可以做到模拟同一个会话
s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456789')
r = s.get('http://httpbin.org/cookies')
print(r.text)
