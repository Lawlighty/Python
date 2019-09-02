from fontTools.ttLib import TTFont
import uni_name
import DBop

uni_Name = uni_name.uni_name
table_name = 'num'
def get_uni_info(file_name,uni_Name):
    """
    获得对应.woff文件的uni字典
    :param file_name: .woff文件名
    :param uni_Name:  对应值的变量
    :return: uni字典
    """
    my_dic = {}
    try:
        myFont = TTFont(file_name)
        uni_list = myFont['cmap'].tables[0].ttFont.getGlyphOrder()[2:]
        for i in range(len(uni_list)):
            my_dic[uni_list[i]] = uni_Name[i]
        print(my_dic)
        return  my_dic
    except Exception as e:
        print(e)

def saveDic(my_dic, table_name):
    """
    把uni字典信息存入数据库
    :param my_dic: uni字典信息
    :param table_name: 表名称
    :return:
    """
    db, cursor = DBop.connDB()
    for k, v in my_dic.items():
        DBop.intoDB(db, cursor, table_name, k, v)
    DBop.CloseDB(db)
    print('finish')

def search_Uni(table_name,k ):
    db, cursor = DBop.connDB()
    res = DBop.sel_fromDb(db, cursor, table_name, k)
    DBop.CloseDB(db)
    return res
if __name__ == '__main__':
    # my_dic = get_uni_info('92e3b83d.woff',uni_Name)
    # saveDic(my_dic,table_name)
    res = search_Uni('num','unieea3')
    print(res)
    print(type(res))

