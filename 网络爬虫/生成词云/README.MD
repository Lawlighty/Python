### 生成两种词云
* 默认矩形词云<br>

  ![图片](https://github.com/Lawlighty/Python/blob/master/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/%E7%94%9F%E6%88%90%E8%AF%8D%E4%BA%91/Simple.png)
* 自定义图片词云<br>
  ![图片](https://github.com/Lawlighty/Python/blob/master/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/%E7%94%9F%E6%88%90%E8%AF%8D%E4%BA%91/MaskCloud.png)
 
### 步骤
* 根据自定义图片获得词云形状 mask
* 读取词云文本  text
* 使用jieba分词文本  wl = jieba.cut(text)
* 设置词云样式WordCloud
* 生成词云 .generate(wl)
* 转为图片 to_image()
* 显示图片 .show()
  
