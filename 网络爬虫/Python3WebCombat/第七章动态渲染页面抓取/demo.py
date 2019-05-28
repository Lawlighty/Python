from lxml import etree
html = '''
<div>
    <a>adasdasdas
        <div class="row row-2 title">
            <span>第一个sanpan</span>
        </div>
        <span>第er个sanpan</span>
    </a>
</div>
'''

doc = etree.HTML(html)
text = doc.xpath('//div[@class="row row-2 title"]/span/text()')[0]
print(text)


html = '''

                  无敌
'''
print(html)
print('*'*20)
h2 = html.replace(' ','').replace('\n','')
print(h2)
print('*'*20)
print(html)