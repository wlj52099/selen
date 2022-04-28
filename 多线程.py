import threading

import requests
from lxml import etree
urls = []
url = 'https://www.janpn.com/book/fanrenxiuxianchuan.html'
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
}
resp = requests.get(url,headers = header)
htmltext = etree.HTML(resp.text)
ul = htmltext.xpath('/html/body/div[2]/div[3]/ul')[0]
for li in ul:
    if len(li.xpath(r'./a/@href')) != 0:
        urls.append(li.xpath(r'./a/@href')[0])
def gt(url):
    resp = requests.get(url, headers=header)
    name = url.replace('.html','').replace('/','')+'.txt'
    f = open(fr'D:\py\ce\{name}','w',encoding='utf-8')
    f.write(resp.text)
    f.close()
def multi_thread():
    threads = []
    for url in urls:
        threads.append(
            threading.Thread(target=gt,args=(url,))
        )
    for thread in threads:
        thread.start()
multi_thread()