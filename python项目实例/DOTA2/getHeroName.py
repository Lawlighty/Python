import herosdic

def getName():
    name = input('>>输入英雄名称').lower()
    new_name = herosdic.herodic.get(name,None)
    # print(new_name)
    return new_name

if __name__ == '__main__':
    getName()
