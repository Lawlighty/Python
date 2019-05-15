import re
list = [ 'a','b','c','d','e','f']
ll = list[-1:]
print(ll)

s = '27℃'
num = re.search('\d{2}',s).group()
print(num)
print(type(num))
print('************')
s = '27℃'
num = re.sub('℃',"",s)
print(num)
print(type(num))

a = ['1','2','c']

c = a+list
print(c)

a = '0'
b = 5
c = a+'{}'.format(b)
print(c)