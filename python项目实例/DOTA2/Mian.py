# 主函数
from herosdic import herodic
import re
import getNewestLogs
import getStrategy
import getHeroName

patt = re.compile('[a-z]')
hero_url = 'http://www.dotamax.com/hero/detail/'
while True:
    print("""
a>>>>>查看DOTA2最新更新日志
    
b>>>>>查看英雄最新攻略
    
exit退出
    """)
    choice = input('>>>>>').lower()
    if choice == 'exit':
        break
    else:
        if re.match(patt, choice):
            if choice == 'a':
                getNewestLogs.main()
            elif choice == 'b':
                while True:
                    hero_name = getHeroName.getName()
                    print('当前查询英雄:',hero_name)
                    if hero_name :
                        hero_url = 'http://www.dotamax.com/hero/detail/{}/'.format(hero_name)
                        print('当前英雄url:', hero_url)
                        getStrategy.main(hero_url)
                        break
                    else:
                        print('输入英雄名字错误\n\n\n\n')
            else:
                print('输入选项错误\n\n\n\n')
        else:
            print('输入选项错误\n\n\n\n')

            '''
            1.3640778064727783
            0.6770386695861816
            1.310075044631958
            0.6890397071838379
            1.55008864402771
            
            
            0.6870391368865967
            0.49202823638916016
            0.724041223526001
            0.7230415344238281
            0.7130405902862549
            
            '''