f=open('pass.txt','w')

chars=['0','1','2','3','4','5','6','7','8','9','q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']

base=len(chars)

for i in range(0,base):
	ch0=chars[i%base]
	for j in range(0,base):
		ch1=chars[j%base]
		for m in range(0,base):
			ch2=chars[m%base]
			for n in range(0,base):
				ch3=chars[n%base]
				char=ch0+ch1+ch2+ch3
				print i
				print char
				f.write(char+'\n')

f.close()