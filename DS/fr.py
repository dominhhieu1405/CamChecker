
import requests,os,re

b="\033[0;34m"
g="\033[1;32m"
w="\033[1;37m"
r="\033[1;31m"
y="\033[1;33m"
cyan = "\033[0;36m"
lgray = "\033[0;37m"
dgray = "\033[1;30m"
ir = "\033[0;101m"
reset = "\033[0m"


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}



def france():
    global page
    res = requests.get('https://www.insecam.org/en/bycountry/FR/', headers=headers)
    findpage = re.findall('"?page=",\s\d+', res.text)[1]
    rfindpage = findpage.replace('page=", ', '')
    os.system('clear')
    print("{}        ____ ").format(r)
    print("   _[]_/____\__n_ ")
    print("  |_____.--.__()_|")
    print("  |I   //# \\\    |")
    print("{}  |P   \\\__//    | ").format(w)
    print("  |CS   '--'     | ")
    print("{}  '--------------'----------{}------------------.  ").format(r,w)
    print("{}  | {}Author  : {}HVmbl3 {}     | {}VIE{}T{}{}NAM         | ").format(r,w,r,w,r,ir,reset,w)
    print("{}  | {}Youtube : {}MHit {}| {}+84-xxx-xxx-xxx {}|").format(r,w,w,w,lgray,w)
    print("{}  '------------------------------------{}-------'  ").format(r,w)
    print("{}       [ {}Tong So Trang : {} {}]").format(r,w,rfindpage,r)
    run()
    
def run():
    try:
        page = input("\033[1;31m       [ \033[1;37mChon trang \033[1;31m]\033[1;37m> ")
        url = ("https://www.insecam.org/en/bycountry/FR/?page="+str(page))
        print ""
        res = requests.get(url, headers=headers)
        findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
        count = 1
        for _ in findip:
             hasil = findip[count]
             print ("{}[ {}{} {}]").format(r,w,hasil,r)
             count += 1
    except:
        print ""
        print r+"Hay sao chep mot trong cac url tren va truy cap bang trinh duyet"+w
        print r+"Please copy a URL on it and paste in your browse"+w 
