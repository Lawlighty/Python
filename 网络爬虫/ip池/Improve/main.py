import getIpfromWeb
import getProxy
import time
def main():
    ip_list = getIpfromWeb.getIp()
    # verified_list = getIpfromWeb.verifyIP(ip_list)
    verified_list = getIpfromWeb.verifyip_multithread(ip_list)
    getIpfromWeb.data_persistence(verified_list)
    print('crawl verified ip list is : ', verified_list)

if __name__ == '__main__':
    star = time.time()
    main()
    getIpfromWeb.refresh_db()
    print(getProxy.get_proxies())
    end = time.time()
    print('用时:',end-star)
    #49.479830265045166     单线程
    # 28.486629486083984    多线程