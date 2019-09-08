import requests
from lxml import etree
import re
html = """

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- CSRF Token -->
    <meta name="csrf-token" content="22QuJRTrYQr7QNriZGtE5hlzmpfMwWMhJB5zUbJT">
        <title>GlidedSky</title>
        <!-- Scripts -->
    <script src="http://glidedsky.com/js/app.js"></script>

    <!-- Fonts -->
    <link rel="dns-prefetch" href="//fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css?family=Nunito" rel="stylesheet" type="text/css">

    <!-- Styles -->
    <link href="http://glidedsky.com/css/app.css" rel="stylesheet">
        <style>
                    .sprite { background-image:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAH0AAAAPCAYAAADJasDvAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAGHklEQVRYhe1ZX2hSbRh/MpHT4WQGh4PYCBGLkDUONkTGLkRiiIzwwiRERsguoryQ0UVUF2OMIRJrhISIjEFRtIsYw4Z0ISMkJCq8EC+8GCJSa4XYMDmY8fuuJvn571jRx0f94Nw87+953+e8v/d5n/c95xAA0F/8UVD81wH8H/Ht2ze6e/cunT17lo4cOULHjh2jc+fO0YcPH/7r0OQBvxFbW1twu93Q6XRQKpUQBAF+vx/7+/t9/aLRKERRBMuyYFkWFosFiUTiN0XdCZfLhZGRESSTSdTrdZRKJUQiEezu7vb04TgORNTxJJPJgeOl02lMTk6C4zgIgoBAIIBGo/HD8beJnsvlMDExAYZhcPr0aVkTG4/HwbIsIpHIQG44HMajR49QLpchSRI2NzfBcRyuXLnS129xcRGbm5uoVCrY3d2F3+8HwzAoFAoDx0ylUlAqlUin0315SqWyTQy3292VF4vFQETIZDIDx+6HUqkEjUaDvb29vrydnR2wLIt4PI56vY5UKgW1Wo3FxcWePisrKzh58iQ4jsPly5chSVJbe5voBoMB169fR6VSQSwWA8MwKJfLPTu32Wzw+XxwOp2yRO8Gh8MBm802lE+1WgUR4d69e3155XIZBoMBGo1GlujNZnPg2GNjY7BarUPF2w1+v1/WnD18+BAsy7bZ7HY7ZmZmuvITiQRGR0dRKBRQLpdhtVqxtLTUxmnV9GfPnlGtVqNQKETHjx+nvb09ajabtLq62rM0xGIxevDgAbEs+0Ol5f379/Ty5Us6f/78UH6lUomIiHQ6XU/O169fyePx0MLCAvE8/0Px/RufP3+mXC5HFy5c+Kl+Hj9+TPl8nq5duzaQa7FYqNFo0K1bt4iI6M2bN5ROp+nSpUtd+clkkmZnZ+nUqVN04sQJ8nq9nRoeqB8KheByuQAAb9++hSiKCAaDPbe57+F2u4fO9Hq9DqvVCqvV2rH99IIkSchkMhBFEVNTU30zMxgM4urVqwAAo9EoK9MPytrNmze7xpTL5UBEWFtbw/3792EymVo+y8vLst4hn8+D53lks1lZfABYXV2FUqnE5OQkNBoNVlZWenJDoRAcDgcqlQp2dnZgt9uhUqna5qol+tzcHGZnZ1Gv1yGKIrLZLCKRiKytd1jRJUmCw+GAKIqoVCqyfGw2W6ve6nQ6pFKpntz19XVYLJaWcHJEB4BarYZMJgOr1Qq/39/Rns1mQUQYHR2F2WzG69evUavVsLGxAY7jcPv27b79N5tNjI+Py14gB3j+/Dl4nocgCNBoNNja2urJrdfr8Pl8YFkWRqMRyWSyozy0ZbrX60UgEMCdO3cAAPPz87880w8Et1gssgU/QKPRQLFYRDgchlKpxPz8fFeew+HoelLmeV7WOMlkEnq9vsNeLpdBRFAoFCgWi21twWAQGo2mb7/xeBwGg0HW2eH7WA7eVZIkzMzMQKFQYG1tTZb/06dPYTab22wt0ROJBNRqNex2e6vRZrNhYWFhYMdyRW82m3C5XDCbzQOvaYMQCATAMIysCRyU6ZVKBdvb26jVaigWi5iamoLX6+3KFQQBWq22w768vAwi6hvPxMREz4XaC2fOnIHT6WyzOZ1OcBzXsyxms9lWKdTr9VhfX29rbx3kHA4H8TxPY2Nj9OXLF3ry5AllMhny+/3DnlN6IhwO04sXLyiRSNDRo0d/qi+FQkEqlYoOHz7803FJkkQ3btwgQRDIbDaTXq+naDTalevxeOjTp0/08ePHNns6nabx8fG+8eTzeTKZTEPFViwWSRTFNtv09DTVajWSJKlnjGq1mjweD83NzdHFixfbCd+vgFwuB6vVCpVKJeuePjIy0rGFzs7O9uSbTKaBd/JuCIVCePXqFfb391GpVBCNRqFSqTquIr0gt6bLwbt37yAIAmw2GwqFAqrVKpaWlqBSqbC9vd3Xl2EYbGxsDDWe2+0Gz/OtD0GZTAZGo7Ej+4fBb/0ip9Vqu9ZahmH6+vl8Pmi12tZXPLvdPvTk/UoUCgVMT09DrVaDZVnYbLZftqj+jWq1imAwCL1eD4ZhoNfrEQgEhj4PfY9DwN8fLn8a/v5w+QPxDz3pnQfwF755AAAAAElFTkSuQmCC") }
                    .CPE13Sxf { height:15px }
                    .jBfAZ33kLAe { float:left }
                    .iBL7PkZFU { height:15px }
                    .Eig3NcM { width:12px }
                    .XxNg27YKO { height:15px }
                    .fMtt1Xhq { height:15px }
                    .zy28bdO { background-position-x:0px }
                    .jdr2AxDSe { width:11px }
                    .CPE13Sxf { width:13px }
                    .xoGIO16HQu { background-position-x:-12px }
                    .Ylw19Fcm { width:14px }
                    .re30oeTIf { height:15px }
                    .jdr2AxDSe { background-position-x:-52px }
                    .lMNKq20ViQ { height:15px }
                    .JTSW8emJT { background-position-x:0px }
                    .BVT0pGR { width:14px }
                    .etfCP32kFsju { float:left }
                    .zy28bdO { height:15px }
                    .ZTYK17nLsB { background-position-x:-38px }
                    .jXNH23hSA { width:14px }
                    .aVX12mFpQ { height:15px }
                    .xoGIO16HQu { width:12px }
                    .jXNH23hSA { background-position-x:-24px }
                    .Ylw19Fcm { float:left }
                    .cSMR22iZwk { background-position-x:-12px }
                    .PBdb9OgAB { background-position-x:-38px }
                    .IB15OJR { background-position-x:-115px }
                    .BVT0pGR { float:left }
                    .xoGIO16HQu { float:left }
                    .PBdb9OgAB { float:left }
                    .ZuQFn6nlm { float:left }
                    .re30oeTIf { width:11px }
                    .LCVIK26rvr { width:14px }
                    .PkY24RQW { height:15px }
                    .PMDJU21lot { background-position-x:-52px }
                    .LCVIK26rvr { float:left }
                    .XxNg27YKO { width:14px }
                    .pc10uet { height:15px }
                    .VZqGF25krH { float:left }
                    .TtECB5WdMw { width:14px }
                    .ZTYK17nLsB { height:15px }
                    .fMtt1Xhq { background-position-x:-12px }
                    .PBdb9OgAB { height:15px }
                    .jXNH23hSA { height:15px }
                    .ZuQFn6nlm { background-position-x:-12px }
                    .pc10uet { background-position-x:-52px }
                    .PkY24RQW { width:14px }
                    .LCVIK26rvr { height:15px }
                    .jdr2AxDSe { float:left }
                    .lMNKq20ViQ { width:14px }
                    .LCVIK26rvr { background-position-x:-24px }
                    .XGg34tjfX { width:10px }
                    .XGg34tjfX { float:left }
                    .oMfD14LbQ { height:15px }
                    .Eig3NcM { background-position-x:-12px }
                    .PkY24RQW { float:left }
                    .jdr2AxDSe { height:15px }
                    .IB15OJR { width:10px }
                    .VZqGF25krH { background-position-x:-63px }
                    .pc10uet { width:11px }
                    .XxNg27YKO { float:left }
                    .Eig3NcM { float:left }
                    .PMDJU21lot { width:11px }
                    .TtECB5WdMw { background-position-x:-24px }
                    .ZuQFn6nlm { height:15px }
                    .Ylw19Fcm { background-position-x:-24px }
                    .MO29YmFXY { float:left }
                    .PMDJU21lot { height:15px }
                    .MO29YmFXY { background-position-x:-24px }
                    .cSMR22iZwk { height:15px }
                    .jBfAZ33kLAe { background-position-x:-12px }
                    .VZqGF25krH { width:10px }
                    .ZTYK17nLsB { float:left }
                    .etfCP32kFsju { height:15px }
                    .XGg34tjfX { height:15px }
                    .PMDJU21lot { float:left }
                    .jXNH23hSA { float:left }
                    .NHjXF31FxCmO { height:15px }
                    .XxNg27YKO { background-position-x:-38px }
                    .pjMi18KHGc { width:14px }
                    .pjMi18KHGc { float:left }
                    .BVT0pGR { height:15px }
                    .iBL7PkZFU { width:12px }
                    .VZqGF25krH { height:15px }
                    .JTSW8emJT { width:12px }
                    .pjMi18KHGc { background-position-x:-38px }
                    .aVX12mFpQ { width:12px }
                    .XGg34tjfX { background-position-x:-115px }
                    .fMtt1Xhq { float:left }
                    .MO29YmFXY { width:14px }
                    .Ylw19Fcm { height:15px }
                    .Eig3NcM { height:15px }
                    .BVT0pGR { background-position-x:-38px }
                    .AGAoM4HBBdz { background-position-x:-101px }
                    .ddt11URrD { background-position-x:-88px }
                    .oMfD14LbQ { width:11px }
                    .aVX12mFpQ { background-position-x:-12px }
                    .re30oeTIf { float:left }
                    .IB15OJR { height:15px }
                    .PkY24RQW { background-position-x:-24px }
                    .CPE13Sxf { background-position-x:-88px }
                    .zy28bdO { float:left }
                    .fMtt1Xhq { width:12px }
                    .ZTYK17nLsB { width:14px }
                    .etfCP32kFsju { background-position-x:-12px }
                    .cSMR22iZwk { float:left }
                    .JTSW8emJT { height:15px }
                    .xoGIO16HQu { height:15px }
                    .AGAoM4HBBdz { height:15px }
                    .AGAoM4HBBdz { float:left }
                    .etfCP32kFsju { width:12px }
                    .zy28bdO { width:12px }
                    .iBL7PkZFU { float:left }
                    .cSMR22iZwk { width:12px }
                    .lMNKq20ViQ { float:left }
                    .oMfD14LbQ { float:left }
                    .jBfAZ33kLAe { height:15px }
                    .iBL7PkZFU { background-position-x:0px }
                    .pc10uet { float:left }
                    .TtECB5WdMw { float:left }
                    .TtECB5WdMw { height:15px }
                    .aVX12mFpQ { float:left }
                    .pjMi18KHGc { height:15px }
                    .oMfD14LbQ { background-position-x:-52px }
                    .ZuQFn6nlm { width:12px }
                    .JTSW8emJT { float:left }
                    .NHjXF31FxCmO { float:left }
                    .CPE13Sxf { float:left }
                    .ddt11URrD { float:left }
                    .IB15OJR { float:left }
                    .lMNKq20ViQ { background-position-x:-38px }
                    .jBfAZ33kLAe { width:12px }
                    .re30oeTIf { background-position-x:-52px }
                    .AGAoM4HBBdz { width:14px }
                    .PBdb9OgAB { width:14px }
                    .ddt11URrD { width:13px }
                    .ddt11URrD { height:15px }
                    .MO29YmFXY { height:15px }
                    .NHjXF31FxCmO { width:10px }
                    .NHjXF31FxCmO { background-position-x:-115px }
            </style>
    
    <script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
    <script>
        (adsbygoogle = window.adsbygoogle || []).push({
            google_ad_client: "ca-pub-2566260602093595",
            enable_page_level_ads: true
        });
    </script>
            <!-- Global site tag (gtag.js) - Google Analytics -->
        <script async src="https://www.googletagmanager.com/gtag/js?id=UA-75859356-3"></script>
        <script>
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());
            gtag('config', 'UA-75859356-3');
        </script>
        <script>
            var _hmt = _hmt || [];
            (function() {
                var hm = document.createElement("script");
                hm.src = "https://hm.baidu.com/hm.js?020fbaad6104bcddd1db12d6b78812f6";
                var s = document.getElementsByTagName("script")[0];
                s.parentNode.insertBefore(hm, s);
            })();
        </script>
    
</head>
<body>
    <div id="app">
        <nav class="navbar navbar-expand-md navbar-light navbar-laravel">
            <div class="container">
                <a class="navbar-brand" href="http://glidedsky.com">
                    GlidedSky
                </a>
                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>

                <div class="collapse navbar-collapse" id="navbarSupportedContent" style="font-size: 1.15em">
                    <!-- Left Side Of Navbar -->
                    <ul class="navbar-nav mr-auto">
                        <li class="nav-item ">
                            <a class="nav-link" href="http://glidedsky.com">Home</a>
                        </li>
                        <li class="nav-item ">
                            <a class="nav-link" href="http://glidedsky.com/rank">Rank</a>
                        </li>
                    </ul>
                    <!-- Right Side Of Navbar -->
                    <ul class="navbar-nav ml-auto">
                        <!-- Authentication Links -->
                                                    <li class="nav-item dropdown">
                                <a id="navbarDropdown" class="nav-link dropdown-toggle" href="#" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" v-pre>
                                    Lawlighty <span class="caret"></span>
                                </a>

                                <div class="dropdown-menu dropdown-menu-right" aria-labelledby="navbarDropdown">
                                    <a class="dropdown-item" href="http://glidedsky.com/logout"
                                       onclick="event.preventDefault();
                                                     document.getElementById('logout-form').submit();">
                                        Logout
                                    </a>

                                    <form id="logout-form" action="http://glidedsky.com/logout" method="POST" style="display: none;">
                                        <input type="hidden" name="_token" value="22QuJRTrYQr7QNriZGtE5hlzmpfMwWMhJB5zUbJT">                                    </form>
                                </div>
                            </li>
                                            </ul>
                </div>
            </div>
        </nav>

        <main class="py-4">
                <div class="container">
        <div class="card">
            <div class="card-body">
                <div class="row">
                                            <div class="col-md-1">
                                                            <div class="BVT0pGR sprite"></div>
                                                            <div class="fMtt1Xhq sprite"></div>
                                                            <div class="jdr2AxDSe sprite"></div>
                                                    </div>
                                            <div class="col-md-1">
                                                            <div class="Eig3NcM sprite"></div>
                                                            <div class="AGAoM4HBBdz sprite"></div>
                                                            <div class="TtECB5WdMw sprite"></div>
                                                    </div>
                                            <div class="col-md-1">
                                                            <div class="ZuQFn6nlm sprite"></div>
                                                            <div class="iBL7PkZFU sprite"></div>
                                                            <div class="JTSW8emJT sprite"></div>
                                                    </div>
                                            <div class="col-md-1">
                                                            <div class="PBdb9OgAB sprite"></div>
                                                            <div class="pc10uet sprite"></div>
                                                            <div class="ddt11URrD sprite"></div>
                                                    </div>
                                            <div class="col-md-1">
                                                            <div class="aVX12mFpQ sprite"></div>
                                                            <div class="CPE13Sxf sprite"></div>
                                                            <div class="oMfD14LbQ sprite"></div>
                                                    </div>
                                            <div class="col-md-1">
                                                            <div class="IB15OJR sprite"></div>
                                                            <div class="xoGIO16HQu sprite"></div>
                                                    </div>
                                            <div class="col-md-1">
                                                            <div class="ZTYK17nLsB sprite"></div>
                                                            <div class="pjMi18KHGc sprite"></div>
                                                            <div class="Ylw19Fcm sprite"></div>
                                                    </div>
                                            <div class="col-md-1">
                                                            <div class="lMNKq20ViQ sprite"></div>
                                                            <div class="PMDJU21lot sprite"></div>
                                                            <div class="cSMR22iZwk sprite"></div>
                                                    </div>
                                            <div class="col-md-1">
                                                            <div class="jXNH23hSA sprite"></div>
                                                            <div class="PkY24RQW sprite"></div>
                                                            <div class="VZqGF25krH sprite"></div>
                                                    </div>
                                            <div class="col-md-1">
                                                            <div class="LCVIK26rvr sprite"></div>
                                                            <div class="XxNg27YKO sprite"></div>
                                                            <div class="zy28bdO sprite"></div>
                                                    </div>
                                            <div class="col-md-1">
                                                            <div class="MO29YmFXY sprite"></div>
                                                            <div class="re30oeTIf sprite"></div>
                                                            <div class="NHjXF31FxCmO sprite"></div>
                                                    </div>
                                            <div class="col-md-1">
                                                            <div class="etfCP32kFsju sprite"></div>
                                                            <div class="jBfAZ33kLAe sprite"></div>
                                                            <div class="XGg34tjfX sprite"></div>
                                                    </div>
                                    </div>
            </div>
        </div>
        <ul class="pagination" role="navigation">
        
                    <li class="page-item">
                <a class="page-link" href="http://glidedsky.com/level/web/crawler-sprite-image-1?page=7" rel="prev" aria-label="&laquo; Previous">&lsaquo;</a>
            </li>
        
        
                    
            
            
                                                                        <li class="page-item"><a class="page-link" href="http://glidedsky.com/level/web/crawler-sprite-image-1?page=1">1</a></li>
                                                                                <li class="page-item"><a class="page-link" href="http://glidedsky.com/level/web/crawler-sprite-image-1?page=2">2</a></li>
                                                                    
                            <li class="page-item disabled" aria-disabled="true"><span class="page-link">...</span></li>
            
            
                                
            
            
                                                                        <li class="page-item"><a class="page-link" href="http://glidedsky.com/level/web/crawler-sprite-image-1?page=5">5</a></li>
                                                                                <li class="page-item"><a class="page-link" href="http://glidedsky.com/level/web/crawler-sprite-image-1?page=6">6</a></li>
                                                                                <li class="page-item"><a class="page-link" href="http://glidedsky.com/level/web/crawler-sprite-image-1?page=7">7</a></li>
                                                                                <li class="page-item active" aria-current="page"><span class="page-link">8</span></li>
                                                                                <li class="page-item"><a class="page-link" href="http://glidedsky.com/level/web/crawler-sprite-image-1?page=9">9</a></li>
                                                                                <li class="page-item"><a class="page-link" href="http://glidedsky.com/level/web/crawler-sprite-image-1?page=10">10</a></li>
                                                                                <li class="page-item"><a class="page-link" href="http://glidedsky.com/level/web/crawler-sprite-image-1?page=11">11</a></li>
                                                                    
                            <li class="page-item disabled" aria-disabled="true"><span class="page-link">...</span></li>
            
            
                                
            
            
                                                                        <li class="page-item"><a class="page-link" href="http://glidedsky.com/level/web/crawler-sprite-image-1?page=999">999</a></li>
                                                                                <li class="page-item"><a class="page-link" href="http://glidedsky.com/level/web/crawler-sprite-image-1?page=1000">1000</a></li>
                                                        
        
                    <li class="page-item">
                <a class="page-link" href="http://glidedsky.com/level/web/crawler-sprite-image-1?page=9" rel="next" aria-label="Next &raquo;">&rsaquo;</a>
            </li>
            </ul>

    </div>
        </main>
    </div>
                    <script>
        _hmt.push(['_trackEvent', 'level-web', 'view', 'crawler-sprite-image-1']);
        gtag('event', 'view', {
            'event_category': 'level-web',
            'event_label': 'crawler-sprite-image-1',
        });
    </script>
    </body>
</html>

"""
def getPos(x, html):
    pos = abs(int(re.search(r''+ x +' { background-position-x:(.*?)px }',html).group(1)))
    print('pppos:',pos)

doc = etree.HTML(html)
cmls = doc.xpath('//div[@class="row"]/div[@class="col-md-1"]')
for cml in cmls:
    lis = []
    NumClass = cml.xpath('./div/@class')
    for i in NumClass:
        code = str(i).split(' ')[0]
        getPos(code,html)
        # lis.append(code)
        # print(lis)
    print('---------')
# x = 'IB15OJR'
# patt = re.compile(r''+ x +' { background-position-x:-(.*?)px }')
# def getPos(x, html):
#     pos = int(re.search(r''+ x +' { background-position-x:-(.*?)px }',html).group(1))
#     print('pppos:',pos)
# pos = int(re.search(patt,html).group(1))
# num = None
# if pos<=15:
#     num = 0
# elif pos<=25:
#     num = 1
# elif pos<=35:
#     num = 2
# elif pos<=48:
#     num = 3
# elif pos<=60:
#     num = 4
# elif pos<=75:
#     num = 5
# elif pos<=87:
#     num = 6
# elif pos<=99:
#     num = 7
# elif pos<=113:
#     num = 8
# else:
#     num = 9
#
# print(pos)
# print(num)
