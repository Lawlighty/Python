# 图片转字符画
from PIL import Image

codeLib = '''@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'. '''#生成字符画所需的字符集
# codeLib ='''01oOuDCcqQ'''
count = len(codeLib)

def transform1(image_file):
    image_file = image_file.convert("L")#转换为黑白图片，参数"L"表示黑白模式
    codePic = ''
    for h in range(0,image_file.size[1]):  #size属性表示图片的分辨率，'0'为横向大小，'1'为纵向
        for w in range(0,image_file.size[0]):
            gray = image_file.getpixel((w,h)) #返回指定位置的像素，如果所打开的图像是多层次的图片，那这个方法就返回一个元组
            codePic = codePic + codeLib[int(((count-1)*gray)/1000)]#建立灰度与字符集的映射---- /x  x越大黑白分离越明显
        codePic = codePic+'\n'
    return codePic


pic = Image.open('pic.jpg')
pic = pic.resize((int(pic.size[0]*0.2),int(pic.size[1]*0.1)))#调整图片大小
code = transform1(pic)
with open('test.txt','w') as f:
    f.write(code)
print('finish')
