#write by xiaoqin00 2016.5.9#
import hashlib 

def md5Encode(str):
	m=hashlib.md5()
	m.update(str)
	return m.hexdigest()


myfile=open('md5.txt','w')
with open('yuanwen.txt','r')as f:
	for line in f:
		print line
		#b=md5Encode(line)
		myfile.write(md5Encode(line))
		myfile.write('\n')
		print md5Encode(line)
myfile.close()
f.close()

