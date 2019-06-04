from PIL import Image

img1 = Image.open('test1.jpg')
#转化为 '1'模式----------为二值图像，每个像素用8bit表示，0表示黑，255表示白
imgMode1 = img1.convert('1')
imgMode1.save('testMode1.jpg')
#转化为 'L' 模式 ----------灰色图像，它的每个像素用8个bit表示，0表示黑，255表示白，其他数字表示不同的灰度。
imgMode2 = img1.convert('L')
imgMode2.save('testMode2.jpg')

imgMode1_new = imgMode1.point(lambda x: 0 if x < 50 else 255, '1')
imgMode1_new.save('imgMode1_new.jpg')

imgMode2_new = imgMode2.point(lambda x: 0 if x < 50 else 255, '1')
imgMode2_new.save('imgMode2_new.jpg')