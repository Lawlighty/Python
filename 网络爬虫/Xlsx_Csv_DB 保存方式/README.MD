
<h3>本文主要 总结爬取数据 保存的三总主要形式--------A .xlsx  B .csv  C.存入数据库
  
  <h5>A:保存到.xlsx  主要通过wb = openpyxl.load_workbook  可以追加原有的数据表
  
  
    def createXlsx():
      title = ['country_or_district','pretty_link']
      wb = openpyxl.Workbook()
      ws = wb.active
      #ws.append(title)
      wb.save('myXlsx.xlsx')

    def openXlsx():
      wb = openpyxl.load_workbook('myXlsx.xlsx')
      return wb

    def inertXlsx(myList,wb):
      ws = wb.active
      ws.append(myList)

    def closeXlsx(wb):
      wb.save('myXlsx.xlsx')
      
   <h5>B: 保存到.csv文件   通过把获得的数据 分别写入列表   通过pandas.DataFrame() 方法生成数据框类型数据  再用 .to_csv()就能生成csv文件
  
      def getDataFrame(nameList, urlList):
        mydic = {
            'country_or_district': nameList,
            'pretty_link':urlList,
        }
        mydf = pd.DataFrame(mydic)
        return mydf

    def SaveAsCsv(df):
        df.to_csv('我的country_Csv文件.csv', header=True, index=False)
        print('保存成功')
        
  <h5>c: 保存到数据库
  
      def conDb():
        db = pymysql.connect('localhost', 'root', 'rootroot', 'pythonsql')
        cursor = db.cursor()
        return db, cursor

    def intoDb(db, cursor,country_or_district, pretty_link):

        sql = 'insert ignore into countyName(countyName,countyUrl) values("{}","{}")'.format(country_or_district, pretty_link)
        try:
            cursor.execute(sql)
            db.commit()
            print('数据库添加成功')
        except Exception as e:
            db.rollback()
            print(e)

    def closeDb(db, cursor):
        cursor.close()
        db.close()
