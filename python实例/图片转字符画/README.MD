## 实现路线
### 1. 根据设置的字符集和原图片映射关系  写入 txt 文件
* 获得图片  设置图片大小 pic.resize(int(pic.size[0]*x),int(pic.size[1)*x)
* 图片灰度模式转换---------.convert("L") 
* x = pic.size[0]----------0(横向)          y = pic.size[1]--------1(纵向)
* 返回像素位置   pic.getpixel((x,y))
* 字符集映射  
* 写入 txt
      
### 2. 读取txt 文件数据
      
### 3. 新建一张图片,把数据画在图片上
* img = Image.new('RGB',(4000,4000),(255,255,255))-----画布大小<br>
  dr = ImageDraw.Draw(img)
* 设置字体 font = ImageFont.truetype("simhei.ttf", 40, encoding="utf-8")-----字体集合 ,字体大小
* 画布上写入数据 dr.text((600,600), text, font=font, fill="#000000")  ------fill背景颜色
