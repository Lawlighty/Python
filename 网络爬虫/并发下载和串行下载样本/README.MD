
具体过程:<br>
1.从 csv 文件读取数据获得需要爬取的网页链接<br>
2.使用串行/并发(多线程)下载<br>


问题主要在于多线程爬虫的使用<br>
1.把获得的 数据放入 队列<br>
2.getHtmlText(url)下载网页的函数 url 从队列中获得 ---> queue.get()<br>
3.线程的创建 thread.Thread(target=函数 ,args=(元祖))<br>
4.判断队列中是否还有任务的机制

      queue.task_done()(写在被调用函数)
      queue.join()(写在主函数)
      
      或
      
      while not workQueue.empty():
        pass
        
5.多进程的创建

from multiprocessing import Pool,Process

def  fun():
      pass
      
 p = Pool()<br>
方法1:apply():<br>


      for i in range(5):
            p.apply_async(fun, args=())
      p.close()
      p.join()
 
 方法2:map()<br>
 
      p.map(fun, list)
      
