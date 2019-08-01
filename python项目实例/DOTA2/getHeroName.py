import herosdic

while True:
    name = input('>>输入英雄名称').lower()
    print(name)
    new_name = herosdic.herodic.get(name,'None')
    print(new_name)
