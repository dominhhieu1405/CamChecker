
import DS
from DS.id import *
from DS.it import *
from DS.jp import *
from DS.us import *
from DS.fr import *
from DS.kr import *
from DS.de import *
from DS.tr import *
from DS.vn import *
from DS.hk import *
from DS.cn import *
from DS.uk import *
from DS.tw import *
from DS.ru import *
import requests,re,os

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



def main():
    os.system('clear')
    print("{}        ____ ").format(r)
    print("   _[]_/____\__n_ ")
    print("  |_____.--.__()_|")
    print("  |CA  //# \\\    |")
    print("{}  |ME  \\\__//    | ").format(w)
    print("  |RA   '--'     | ")
    print("{}  '--------------'----------{}------------------.  ").format(r,w)
    print("{}  | {}Author  : {}MHit {}     | {}VIE{}T{}{}NAM         | ").format(r,w,r,w,r,ir,reset,w)
    print("{}  | {}Youtube : {}???? {}| {}+84-xxx-xxx-xxx {}|").format(r,w,w,w,lgray,w)
    print("{}  '------------------------------------{}-------'  ").format(r,w)
    print ("  {}[ 1 ] {}Italy").format(r,w)
    print ("  {}[ 2 ] {}Indonesia").format(r,w)
    print ("  {}[ 3 ] {}Japan").format(r,w)
    print ("  {}[ 4 ] {}United States").format(r,w)
    print ("  {}[ 5 ] {}France").format(r,w)
    print ("  {}[ 6 ] {}Korea").format(r,w)
    print ("  {}[ 7 ] {}Germany").format(r,w)
    print ("  {}[ 8 ] {}Turkey").format(r,w)
    print ("  {}[ 9 ] {}Vietnam").format(r,w)
    print ("  {}[ 10 ] {}Hong Kong").format(r,w)
    print ("  {}[ 11 ] {}China").format(r,w)
    print ("  {}[ 12 ] {}United Kingdom").format(r,w)
    print ("  {}[ 13 ] {}Taiwan").format(r,w)
    print ("  {}[ 14 ] {}Russian Federation").format(r,w) 
    print ("  {}[ 0 ] {}Exit").format(r,w)
    print ""
    select = input("\033[1;31m[ \033[1;37mChon So \033[1;31m]\033[1;37m> ")
    filtering(select)



def filtering(pilih):
    if pilih == 1:
        italy()
    elif pilih == 2:
        indonesia()
    elif pilih == 3:
        japan()
    elif pilih == 4:
        unitedstates()
    elif pilih == 5:
        france()
    elif pilih == 6:
        korea()
    elif pilih == 7:
        germany()
    elif pilih == 8:
        turkey()
    elif pilih == 9:
        vietnam()    
    elif pilih == 10:
        hongkong()
    elif pilih == 11:
        china()    
    elif pilih == 12:
        unitedkingdom()
    elif pilih == 13:
        taiwan()
    elif pilih == 14:
        russian()    
    elif pilih == 0:
        print (r+"Dang thoat ..."+w)
        os.sys.exit()
    else:
        print (r+"Dang thoat ..."+w)
        os.sys.exit()

if __name__ == '__main__':
    main()
