#python3 “xxx.py”  “xx目录” “logname
import hashlib
import os, sys
def md5log(file,log):
	m = hashlib.md5()
	try:
		f = open(file,'rb')       
		for line in f:           
			m.update(line)    
			f.close
		#print(file+": "+m.hexdigest())
		w = open(log,'a+')
		w.write(file+": "+m.hexdigest()+"n")
		w.close
		
	except PermissionError:#权限不够的文件，一般你没有别人也没有。
		w = open(log,'a+')
		w.write(file+": Errorn")
		w.close

def listls(folder,logname):
	ls = os.listdir(folder)
	for path in ls:
		list = os.path.join(folder, path)
		if os.path.isdir(list):
			listls(list,logname)
		else:
			md5log(list,logname)

if __name__ == "__main__":
	try:
		listls(sys.argv[1],sys.argv[2])
	except IndexError:
		print("Input Index: python3 md5log.py folder logname")