from info import city_info
from lxml import etree
import re
# for k, v in city_info.items():
#     for item in v:
#         print(item)
html = '''
lass="content__list">
                        <div
            class="content__list--item"
            data-house_code="BJ2297898310671015936"
            data-brand_code="200301001000"
            data-c_type="1"
            data-fb_expo_id="203532663906676737"
            data-position="0"
            data-total="1035"
            >
              <a
              class="content__list--item--aside" target="_blank"              href="/zufang/BJ2297898310671015936.html"><img
              alt="整租·广渠家园 2室1厅 东"
              src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/250-182.png?_v=201907151809158c9"
              data-src="https://image1.ljcdn.com/110000-inspection/38c29550-f69c-4dc5-8a52-924794e1953b.jpg.250x182.jpg"
              class="lazyload">
                <!-- 是否展示vr图片 -->
                              </a>

              <div class="content__list--item--main">
                <p class="content__list--item--title twoline">
                  <a target="_blank" href="/zufang/BJ2297898310671015936.html">
                    整租·广渠家园 2室1厅 东                  </a>
                </p>
                <p class="content__list--item--des">
                  <a target="_blank" href="/zufang/dongcheng">东城</a>-<a href="/zufang/guangqumen" target="_blank">广渠门</a>
                  <i>/</i>
                  51㎡
                  <i>/</i>东                  <i>/</i>
                    2室1厅1卫                  <span class="hide">
                    <i>/</i>
                    中楼层                                            （29层）
                                      </span>
                </p>
                                <p class="content__list--item--brand oneline">
                  链家                </p>
                                <p class="content__list--item--time oneline">5天前发布</p>
                <p class="content__list--item--bottom oneline">
                                <i class="content__item__tag--is_subway_house">近地铁</i>
                                <i class="content__item__tag--decoration">精装</i>
                                <i class="content__item__tag--central_heating">集中供暖</i>
                                <i class="content__item__tag--is_new">新上</i>
                                <i class="content__item__tag--is_key">随时看房</i>
                                </p>
                <span class="content__list--item-price"><em>5900</em> 元/月</span>
              </div>
          </div>

'''
doc= etree.HTML(html)
title = ''.join(doc.xpath('.//p[@class="content__list--item--title twoline"]/text()')).replace('\n','').replace(' ','')
print(title)
text = "".join(doc.xpath('//p[@class="content__list--item--title twoline"]//text()')).replace('\n','').replace(' ','')
print(text)
location = '-'.join(doc.xpath('//p[@class="content__list--item--des"]/a/text()'))
print(location)
area = doc.xpath('//p[@class="content__list--item--des"]/text()')[3].replace('\n','').replace(' ','')
print(area)
face = doc.xpath('//p[@class="content__list--item--des"]/text()')[4].replace('\n','').replace(' ','')
print(face)
rooms = str(doc.xpath('//p[@class="content__list--item--des"]/text()')[5].replace('\n','').replace(' ',''))
rooms = re.sub('[室厅卫]','###',rooms).split('###')
room = rooms[0]
hall = rooms[1]
toilet = rooms[2]
print(room, hall, toilet)
price = "".join(doc.xpath('//span[@class="content__list--item-price"]//text()'))
print(price)
layout=[2 ,1,5]
lll = layout[3] if 3<=len(layout)-1 else 0
print('''llll''',lll)