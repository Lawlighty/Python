### MongoDB数据导入到CSV文件
* 定位到MongoDB/bin文件下
* mongoexport -d myDB -c user -f _id,name,password,adress --csv -o ./user.csv


          d 表示 数据库 
          -c 表示数据表 
          -f 需要提取的列名用逗号分隔 
          -o 输出路径   ./表示bin文件夹下
          ps:csv前面是两个横杠
