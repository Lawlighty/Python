from fontTools.ttLib import TTFont

def Get_Best_Cmap():
    # '0x30': 'cid00025'
    """
    返回映射表
    :return:
    """
    ttfont = TTFont('myfont.woff')
    ttfont.saveXML('myfont.xml')

    # 读取映射表
    best_cmap = ttfont['cmap'].getBestCmap()

    new_best_cmap = {}
    # 字典解包 序列解包
    for k,v in best_cmap.items():
        # 转为16进制
        new_best_cmap[hex(k)] = v
    # print(new_best_cmap)
    return new_best_cmap


def Get_number_Cmap():
    # 'uni0035': 0,
    """
    根据fontCreator 映射构建dic
    :return:返回 uni 和真正数字的映射关系
    """
    # number_best_cmap = {
    #     'uni0035': 0,
    #     'uni0037': 1,
    #     'uni0036': 2,
    #     'uni0039': 3,
    #     'uni0034': 4,
    #     'uni0032': 5,
    #     'uni0033': 6,
    #     'uni0031': 7,
    #     'uni0030': 8,
    #     'uni0038': 9
    # }
    number_best_cmap = {
        'uni0035': '0',
        'uni0037': '2',
        'uni0036': '3',
        'uni0039': '6',
        'uni0034': '7',
        'uni0032': '4',
        'uni0033': '8',
        'uni0031': '5',
        'uni0030': '9',
        'uni0038': '1',
    }
    # number_best_cmap = [
    #     {'uni0035': '0'},
    #     {'uni0037':'2'},
    #     {'uni0036': '3'},
    #     {'uni0039': '6'},
    #     {'uni0034': '7'},
    #     {'uni0032': '4'},
    #     {'uni0033': '8'},
    #     {'uni0031': '5'},
    #     {'uni0030': '9'},
    #     {'uni0038': '1'},
    # ]
    return number_best_cmap

def Map_Cmap_Number(Get_Best_Cmap, Get_number_Cmap):
    new_best_cmap = Get_Best_Cmap()
    number_best_cmap = Get_number_Cmap()
    key_list = []
    value_list = []
    map_cmap_number = {}
    for i in new_best_cmap.keys():
        key_list.append(i)
    for i in number_best_cmap.values():
        value_list.append(i)
    # key_list = new_best_cmap.keys()
    # value_list = number_best_cmap.values()
    for i in range(len(key_list)):
        map_cmap_number[key_list[i]] = value_list[i]
    # print(map_cmap_number)
    return map_cmap_number
    # print(map_cmap_number)
if __name__ == '__main__':
    # a = {'0x30': 'cid00025', '0x31': 'cid00024', '0x32': 'cid00022', '0x33': 'cid00023', '0x34': 'cid00021', '0x35': 'cid00017', '0x36': 'cid00019', '0x37': 'cid00018', '0x38': 'cid00026', '0x39': 'cid00020'}
    # for i in a:
    #     print(a[i])
    Map_Cmap_Number(Get_Best_Cmap,Get_number_Cmap)