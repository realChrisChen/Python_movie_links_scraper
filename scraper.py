import requests,re
from requests.cookies import RequestsCookieJar
from fake_useragent import UserAgent
import os,pickle,threading,time
import concurrent.futures
from goto import with_goto
os.chdir("C:/Users/22851/Desktop/")
def get_content_url_name(url):
    send_headers = {
     "User-Agent":UserAgent().random,
    "Connection": "keep-alive",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8"

        }
    cookie_jar = RequestsCookieJar()
    cookie_jar.set("mttp", "9740fe449238", domain="www.yikedy.co")
    response=requests.get(url,send_headers,cookies=cookie_jar)
    response.encoding='utf-8'
    content=response.text
    reg=re.compile(r'<a href="(.*?)" class="thumbnail-img" title="(.*?)"')
    url_name_list=reg.findall(content)
    return url_name_list

def get_content(url):
    send_headers = {
     "User-Agent":UserAgent().random,
    "Connection": "keep-alive",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8"

        }
    cookie_jar = RequestsCookieJar()
    cookie_jar.set("mttp", "9740fe449238", domain="www.yikedy.co")
    response=requests.get(url,send_headers,cookies=cookie_jar)
    response.encoding='utf-8'
    return response.text



def search_durl(url):
    content=get_content(url)
    reg=re.compile(r"{'\\x64\\x65\\x63\\x72\\x69\\x70\\x74\\x50\\x61\\x72\\x61\\x6d':'(.*?)'}")
    index=reg.findall(content)[0]
    download_url=url[:-5]+r'/downloadList?decriptParam='+index
    content=get_content(download_url)
    reg1=re.compile(r'title=".*?" href="(.*?)"')
    download_list=reg1.findall(content)
    return download_list
def get_page(url):
    send_headers = {
     "User-Agent":UserAgent().random,
    "Connection": "keep-alive",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8"

        }
    cookie_jar = RequestsCookieJar()
    cookie_jar.set("mttp", "9740fe449238", domain="www.yikedy.co")
    response=requests.get(url,send_headers,cookies=cookie_jar)
    response.encoding='utf-8'
    content=response.text
    reg=re.compile(r'<a target="_blank" class="title" href="(.*?)" title="(.*?)">(.*?)<\/a>')
    url_name_list=reg.findall(content)
    return url_name_list
@with_goto
def main():
    print("----------------------------------------------------------------------")
    print("请输入剧名 或 剧名 第几季(输入quit退出)")
    name=input()
    if name == "quit":
        exit()
    url="http://www.yikedy.co/search?query="+name
    dlist=get_page(url)
    if(dlist):
        num=0
        count=0
        for i in dlist:
            if (name in i[1]) :
                print(f"{num} {i[1]}")
                num+=1
            elif num==0 and count==len(dlist)-1:
                goto .end
            count+=1
        dest=int(input("请输入你所想要看剧的编号:"))
        x=0
        print("以下为下载链接")
        for i in dlist:
            if(x==dest):
                for durl in search_durl(i[0]):
                    print(f"{durl}")
                break
            x+=1
    else:
        label .end
        print("没找到\n")
print("本软件由CLY.所有\n\n")
while(True):
    main()
