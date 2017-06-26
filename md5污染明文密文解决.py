import hashlib
def md5(dataForEncode):
	hash_md5=hashlib.md5()
	hash_md5.update(dataForEncode)
	return hash_md5.hexdigest()	

#list=['T','A','S','C','?','O','3','R','J','M','V','?','W','D','J','K','X','?','Z','M']
list1='TASC'
list2='O3RJMV'
list3='WDJKX'
list4='ZM'

flag=0
for i1 in range(32,126):
	if flag==1:
		break
	char1=chr(i1)
	list12=list1+char1+list2
	for i2 in range(20,126):
		if flag==1:
			break
		char2=chr(i2)
		list123=list12+char2+list3
		for i3 in range(20,126):
			if flag==1:
				break
			char3=chr(i3)
			list1234=list123+char3+list4
			print list1234
			
			string=md5(list1234)
			if string[0:5]=='e9032':
				if string[8:10]=='da':
					if string[13:15]=='08':
						if string[19:25]=='911513':
							if string[26]=='0':
								if string[30:32]=='a2':
									print list1234
									flag=1
									break 
print 'attention!'
print list1234
print md5(list1234)