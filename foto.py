import os
import shutil
root,dirs,files = list(os.walk('.'))[0]
f={}
for i in files :
	if i=='foto.py' : continue
	g,m = i[4:8],i[8:10]
	if g in f :
		if m in f[g] : f[g][m].append(i)
		else : f[g][m]=[i]	
	else : f[g]={m:[i]}
for y in f :
	if y not in dirs : 
		os.mkdir(y)
		print(y)
	for m in f[y] :
		os.mkdir(y+"/"+m)
		print(m)
		for fil in f[y][m] :
			shutil.copy2(fil,y+"/"+m)
