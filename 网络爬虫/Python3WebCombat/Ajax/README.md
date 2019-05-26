网络爬虫开发实战第六章<br>
Ajax数据爬取<br>

学习记录<br>
1.Ajax 加载网页爬取之后 使用  .json()将内容解析为 Json 返回(以前使用 json.loads(r.text))

    r =request.get(url)
    return r.json()
    
    
2.多用yield  代替数据写入List 来节省内存<br>

3. 网页数据item项的选择可以 通过判断 该字典中 key的值是否存在  -----是否是需要爬取的item<br>
    
    --------有 cell_type 内容的项 跳过
    
    
    
            if item.get('cell_type') is not None:
                continue

