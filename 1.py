import commands
s = commands.getoutput('nmap 10.1.39.79')
if 'PORT' in s:
	s = s.split('\n')
	s = filter(None,s)
	ip = s[1].split(' ')[4]
	arr = []
	for i in range(5,len(s)-1):
		data=filter(None,s[i].split(' '))
		dic = {}
		dic['PORT']=data[0]
		dic['STATE']=data[1]
		dic['SERVICE'] = data[2]
		arr.append(dic)
	dic1={}
	dic1[ip]=arr
	print str(dic1).replace('\'',"\"")
else:
	print 'All ports are closed'