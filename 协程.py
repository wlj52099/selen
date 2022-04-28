import asyncio
import aiohttp

def url():
    list = []
    import requests
    from lxml import etree
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
    }
    resp = requests.get('http://www.go5.cc/book/4088/',headers=headers)
    Html = etree.HTML(resp.text)
    ul = Html.xpath('//*[@id="chapterList"]')[0]
    for li in ul:
        list.append(li.xpath('./a/@href')[0])
    return list
async def fetch(session,url):
    print("发送请求",url)
    gurl = 'http://www.go5.cc' + url
    async with session.get(gurl,verify_ssl = False) as response:
        content = await response.content.read()
        file_name ='D:\cs\yzm\\' + url.rsplit('/')[-1].replace('.html','')+'.txt'
        with open(file_name,mode='wb') as file_object:
            file_object.write(content)
        print("下载完成")

async def main(url):
    async with aiohttp.ClientSession() as session:
        url_list=url
        tasks = [asyncio.create_task(fetch(session,url)) for  url in url_list]
        await asyncio.wait(tasks)
if __name__ == '__main__':
    pass
    asyncio.run(main(url()))
    