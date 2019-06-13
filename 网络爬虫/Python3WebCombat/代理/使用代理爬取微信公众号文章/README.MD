## 网页解析 https://weixin.sogou.com/weixin?type=2&query=DOTA2&page=1
* type=2-----微信公众平台
* query=DOTA2 --- 搜索关键字
* page=1 -----页码

## 时间数据获取 
网页显示类似<script>document.write(timeConvert('1560145782'))</script><br>
需从js类型页面寻找 timeCovert函数,从common.min.js?v=20180607 文件发现


    function timeConvert(e) {
        if (e) {
            var n, t, r, o;
            if (e = parseInt(e),
            o = parseInt((new Date).getTime() / 1e3) - e,
            r = parseInt(o / 86400),
            t = parseInt(o / 3600),
            n = parseInt(o / 60),
            r > 0 && r < 4)
                return r + "天前";
            if (r <= 0 && t > 0)
                return t + "小时前";
            if (t <= 0 && n > 0)
                return n + "分钟前";
            var c = new Date(1e3 * e);
            return c.getFullYear() + "-" + (c.getMonth() + 1) + "-" + c.getDate()
        }
        return ""
    }
    
使用execjs库
* execjs.compile(js)编译
* .call('funcationName',*params) 执行js
