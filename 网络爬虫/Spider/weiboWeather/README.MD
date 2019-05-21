

sql 语句本为  
sql = 'insert ignore into nbWeather(date,city,desc,temp) values("{}","{}","{}","{}")'.format(item["date"],item["city"],item["desc"],item["temp"])
scrapy 一直报错
后发现desc 为数据库关键字 需要添加``  (`为`~键)

sql = 'insert ignore into nbWeather(date,city,`desc`,`temp`) values("{}","{}","{}","{}")'.format(item["date"],item["city"],item["desc"],item["temp"])

写入数据库前清空表中的数据
