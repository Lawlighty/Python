#随机获得一个proxies
import random
import DataBase

def get_proxies():
    proxies = {}
    ip_list = DataBase.get_ip_list()
    ip = random.choice(ip_list)

    proxies['http'] = 'http://{ip}'.format(ip=ip)
    # proxies['https'] = 'https://{}'.format(ip)

    return proxies