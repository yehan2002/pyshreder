#!/usr/bin/python
import sys
import os
def wipesync(file):
	if file.endswith('/'):
		file = file[:-1]
	filename = os.path.basename(file)
	location = os.path.dirname(file)
	nname = '0' * len(filename)
	os.system('mv -f "%s" "%s"'%(file,os.path.join(location,nname)))
	filename = os.path.join(location,nname)
	while nname != '0' and nname != '':
		nname = nname[:-1]
		os.system('mv -f "%s" "%s"'%(filename,
			os.path.join(location,nname)))
		filename = os.path.join(location,nname)
	os.system('rm -f -r "%s"'%(filename))
def shred(location,iteration=6,zero=True,delfile=True,parent=True,args=[],prepend=[],debug=False):
	cmd = ['shred','-f','-x','--iterations=%s'%(iteration)]
	cmd = prepend + cmd + args
	if zero:
		cmd.append('-z')
	if delfile:
		cmd.append('-u')
	cmd = ' '.join(cmd)
	q = lambda s:' "%s"'%(s)
	if not os.path.exists(location):
		if __name__ == '__main__':
			quit("shreder: %s No such file or directory"%(location))
		return 0
	if os.path.isfile(location):
		os.write(1,'Shreding ' + location + '...')
		os.system(cmd + q(location))
		os.write(1,' Done\n')
		return True
	files = []
	dirs = []
	for i,j,y in os.walk(location):
		for item in y:
			file = os.path.join(i,item)
			if not os.path.isdir(file):
				if debug:
					os.write(1,'Shreding ' + file + '...')
				os.system(cmd + q(file))
				if debug:
					os.write(1,' Done\n')
		for dirr in j:
			if delfile:
				file = os.path.join(i,dirr)
				if debug:
					os.write(1,'Shreding ' + file + '...')
				wipesync(file)
				if debug:	
					os.write(1,' Done\n')
	if parent and delfile:
		wipesync(location)
	return True
if __name__ == '__main__':
	try:
		location = sys.argv[1]
	except:
		quit('Location is requred as first argivement')
	shred(location,debug=True)
