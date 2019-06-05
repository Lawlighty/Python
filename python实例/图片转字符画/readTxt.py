from PIL import Image,ImageDraw,ImageFont
import os
import re

mystr = ''
with open('test.txt','r') as f:
    for line in f:
        line = str(line).replace('\n','')
        mystr = mystr+line+'\n'

print(mystr)
