import os
import re
import datetime 
import shutil
fotodir='foto'
nachdir='fotonach'
files = os.listdir(nachdir)
if not os.path.exists(fotodir):
	os.mkdir(fotodir)
print(len(files))
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
	st=str(datetime.datetime.fromtimestamp(os.stat(nachdir+"/"+i).st_mtime))
	g,m = st[:4],st[5:7]
	if g in f :
		if m in f[g] : f[g][m].append(i)
		else : f[g][m]=[i]	
	else : f[g]={m:[i]}
for y in f :
	if not os.path.exists(fotodir+"/"+y):
		os.mkdir(fotodir+"/"+y)
		print(y)
	for m in f[y] :
		if not os.path.exists(fotodir+"/"+y+"/"+m):
			os.mkdir(fotodir+"/"+y+"/"+m)
			print(m)
		for fil in f[y][m] :
#			shutil.copy2(fil,fotodir+"/"+y+"/"+m)
			shutil.move(nachdir+"/"+fil,fotodir+"/"+y+"/"+m)
#			os.replace(fil,fotodir+"/"+ y+"/"+m+"/")
shutil.make_archive('foto', 'tar', './foto')
