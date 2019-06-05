from PIL import Image,ImageDraw,ImageFont
import os
import re

mystr = ''
with open('test.txt','r') as f:
    for line in f:
        line = str(line).replace('\n','')
        mystr = mystr+line+'\n'

print(mystr)
img = Image.new('RGB',(4000,4000),(255,255,255))
dr = ImageDraw.Draw(img)
font = ImageFont.truetype("simhei.ttf", 40, encoding="utf-8")
dr.text((600,600), mystr, font=font, fill="#000000")

img.show()
img.save('code_pic.jpg')