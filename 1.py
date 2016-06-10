import commands
import collections
p=raw_input()
q = commands.getoutput('nmap %s' %p)
# q = commands.getoutput('nmap 10.1.39.79-100')
q=q.split('Nmap')
# q=q.replace('\n','$').split('$$')
dic1={}
for i in range(2,len(q)-1):
	s=q[i]
	if 'PORT' in s:
		s=s.split('\n')
		s=filter(None,s)
		ip = s[0].split(' ')[4]
		arr = []
		for j in range(4,len(s)):
			data=filter(None,s[j].split(' '))
 			dic = {}
 			dic["PORT"]=str(data[0])
 			dic["STATE"]=data[1]
 			dic["SERVICE"] = data[2]
 			arr.append(dic)
 		dic1[ip]=arr
	else:
		s=s.split('\n')
		s=filter(None,s)
		ip = s[0].split(' ')[4]
		dic1[ip]="All ports are close"
print str(dic1).replace('\'',"\"")