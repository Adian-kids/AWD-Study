import requests
for i in range(10,20):
	url = "http://172.16." + str(i) + ".1/flag.php"
	try:
	report = requests.get(url)
	print "http://172.16." + str(i) + ".1",report.text
	except:
		pass