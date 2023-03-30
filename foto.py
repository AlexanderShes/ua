import os
import re
from os.path import getctime
import datetime 
import shutil
files = os.listdir('.')
fotodir='foto'
if not os.path.exists(fotodir):
	os.mkdir(fotodir)
print(files)
'''	match = re.search(r'ggg-(\d\d\d\d)(\d\d)', i) 
	if match :
		g,m=match[1],match[2]
	match = re.search(r'photo-(\d\d\d\d)(\d\d)', i) 
	if match :
		g,m=match[1],match[2]
	match = re.search(r'photo-(\d\d\d\d)(\d\d)', i) 
	if match :
		g,m=match[1],match[2]'''



f={}
for i in files :
	if 'foto' in i or '.git' in i or 'READ' in i or '.' not in i : continue
#	print(i,datetime.datetime.fromtimestamp(getctime(i)).strftime('%Y:%m'))
	st=str(datetime.datetime.fromtimestamp(os.stat(i).st_mtime))
#	print(i,os.stat(i))
	print(i,"---",st)
	g,m = st[:4],st[5:7]

	print(g,m)
#	continue
#	g,m = i[4:8],i[8:10]



	if g in f :
		if m in f[g] : f[g][m].append(i)
		else : f[g][m]=[i]	
	else : f[g]={m:[i]}

print(f)
for y in f :
#	if y not in dirs : 
	if not os.path.exists(fotodir+"/"+y):
		os.mkdir(fotodir+"/"+y)
		print(y)
	for m in f[y] :
		if not os.path.exists(fotodir+"/"+y+"/"+m):
			os.mkdir(fotodir+"/"+y+"/"+m)
			print(m)
		for fil in f[y][m] :
#			shutil.copy2(fil,fotodir+"/"+y+"/"+m)
			os.rename(fil,fotodir+"/"+ y+"/"+m+"/"+fil)
shutil.make_archive('foto', 'tar', './foto')

