# Author : D4RKSH4D0WS
import requests,json,os
G0 = "\033[0;32m"
G1 = "\033[1;32m"
C0 = "\033[0;36m"
C1 = "\033[1;36m"
P0 = "\033[0;35m"
P1 = "\033[1;35m"
W0 = "\033[0;37m"
W1 = "\033[1;37m"
B0 = "\033[0;34m"
B1 = "\033[1;34m"
R0 = "\033[0;31m"
R1 = "\033[1;31m"
Y1 = "\033[1;33m"
Y0 = "\033[0;33m"
r = requests.Session()
def lg():
  if os.name == 'nt':os.system('cls')
  else:os.system('clear')
  print """
%s[ %sJadwal Sholat dan Terbitnya matahari %s]
%s [ %sPowered by  http://muslimsalat.com %s]
"""%(G1,W1,G1,G1,W1,G1)
lg()
jikuk = raw_input("\033[1;32m[\033[1;33m?\033[1;32m] \033[1;37mMasukkan nama kota/negara: ")
lg()
a = r.get("http://muslimsalat.com/daily/"+jikuk+"/false.json").text
b = json.loads(a)["items"][0]
print "         \033[1;32m[\033[1;37m Tanggal",b["date_for"],"\033[1;32m]"
print
print "%s[%s*%s] %sKota atau Negara:"%(G1,R1,G1,W1),json.loads(a)["title"]
print
print "%s[%s>%s] %sFajar   :"%(G1,Y1,G1,W1),b["fajr"]
print "%s[%s>%s] %sShurooq :"%(G1,Y1,G1,W1),b["shurooq"]
print "%s[%s>%s] %sDhuhur  :"%(G1,Y1,G1,W1),b["dhuhr"]
print "%s[%s>%s] %sAsar    :"%(G1,Y1,G1,W1),b["asr"]
print "%s[%s>%s] %sMaghrib :"%(G1,Y1,G1,W1),b["maghrib"]
print "%s[%s>%s] %sIsya'   :"%(G1,Y1,G1,W1),b["isha"]
