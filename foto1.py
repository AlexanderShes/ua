import os
import re
from os.path import getctime
import datetime 
files = os.listdir('.')
print(files)




f={}
for i in files :
	if 'foto' in i or '.git' in i or 'READ' in i : continue
	print(i,datetime.datetime.fromtimestamp(getctime(i)).strftime('%Y:%m'))
	st=os.stat(i).st_mtime
	print(i,os.stat(i))
	print(i,"---",datetime.datetime.fromtimestamp(st))

	match = re.search(r'ggg-(\d\d\d\d)(\d\d)', i) 
	if match :
		g,m=match[1],match[2]
	match = re.search(r'photo-(\d\d\d\d)(\d\d)', i) 
	if match :
		g,m=match[1],match[2]
	match = re.search(r'photo-(\d\d\d\d)(\d\d)', i) 
	if match :
		g,m=match[1],match[2]


	print(g,m)
	continue
#	g,m = i[4:8],i[8:10]



	if g in f :
		if m in f[g] : f[g][m].append(i)
		else : f[g][m]=[i]	
	else : f[g]={m:[i]}

quit()
for y in f :
	if y not in dirs : 
		os.mkdir(y)
		print(y)
	for m in f[y] :
		os.mkdir(y+"/"+m)
		print(m)
		for fil in f[y][m] :
			shutil.copy2(fil,y+"/"+m)
