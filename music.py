#!/bin/python
# coding: utf-8
import os
import time
from random import *
import sys
import threading
import subprocess

playing=False

#Scan music from sdcard
#turn music off after kill process
#run python script in background
#add functionality to show previous commands entered

#Generates MP3 List
def genlist():
	if getState():
		os.system('termux-media-player stop')
	print '\nPlease Wait !!\n\tIt may Take A While To Scan Your Phone Memory...'
	print 'It may take a couple of minutes....'
	os.system("find -L /sdcard -type f -ipath '*.mp3' >mp3.list")
	print '\nPhone Scan Completed !!!'
	ch=raw_input('Want To Scan SD Card (Y/N): ')
	if ch.lower().strip()=="y":
		print '\nPlease Wait !!\n\tIt may Take A While To Scan Your SDCARD Memory...'
		print 'It may take a couple of minutes....'
		os.system("find -L /storage/sdcard1 -type f -ipath '*.mp3' >>mp3.list")
		print '\nSD Card Scan Completed'
	raw_input('Press Enter To Continue...')
#Checks if music is being played
def getState():
	subprocess.call("termux-media-player info >info.xx",shell=True)
	f1=open("info.xx","r")
	a=f1.read()
	f1.close()
	if len(a) >= 21:
		return True
	else:
		return False
#Exits TPlay
def Exit():
	global p
	ln=open('mp3.list').read()
	if len(p)!=ln.count('\n'):
		print 'Please Wait While We Save Some Changes...'
		f=open('mp3.list','w')
		for wr in p:
			f.write(wr+'\n')
		f.close()
		print 'Changes Saved !!!!'

	print '          \t Created By SpeedX'
	os.system("echo -e \"\e[1;31m\"")
	os.system("toilet -f mono12 -F border     SpeedX   ")
	os.system("echo -e \"\e[1;32m\"")
	os.system('echo -e "\\e[1;34m Created By SpeedX\\e[0m"')
	os.system('echo -e "\\e[4;32m This Player Was Created By SpeedX \\e[0m"')
	os.system('echo -e "\\e[1;34m For Any Queries Mail Me!!!\\e[0m"')
	os.system('echo -e "\\e[1;32m           Mail: ggspeedx29@gmail.com \\e[0m"')
	os.system('echo -e "\\e[1;31m       Whatsapp: https://bit.do/speedxgit \\e[0m"')
	os.system('echo -e "\\e[1;33m   YouTube Page: https://www.youtube.com/c/GyanaTech \\e[0m"')
	exit()
#Gets Valid Songs Paths And extracts song name
def dislist():
	global p
	global sname
	f=open("mp3.list","r")
	a=f.read()
	f.close()
	p=a.split("\n")
	p.remove('')
	sname=[]
	flg=True
	while flg:
		flg1=True
		for pr in p:
			if not os.path.exists(pr):
				p.remove(pr)
				flg1=False
		if flg1:
			flg=False
	cols=int(os.popen('echo $COLUMNS').read().split('\n')[0])
	for pr in p:
		l=pr.rfind('/')+1
		if l==0:
			continue
		ap=pr[l:len(pr)-4]
		dif=len(ap)-cols+30
		if dif>0:
			ap=ap[:len(ap)-dif]
	        sname.append(ap)
	if len(p) ==0:
		print "No Songs Found in here!!"
		print "Songs with .mp3 extension are recognised only !!!"
		Exit()
	print str(len(p))+" songs Loaded !!"
	print "Press Enter To Start Playing..."
	raw_input()
#Sorts MP3 List path wise
def sortlist():
	global p
	ln=open('mp3.list').read()
	if len(p)!=ln.count('\n'):
		print 'Please Wait While We Save Some Changes...'
		f=open('mp3.list','w')
		for wr in p:
			f.write(wr+'\n')
		f.close()
		print 'Changes Saved !!!!'
	print 'Sorting List....'
	os.system('sort -bfidu mp3.list -o mp3.list')
	dislist()
#Removes Song From PlayList
def remove(n):
	global p
	global sname
	p.pop(n)
	sname.pop(n)

if not os.path.isfile(os.environ['PREFIX']+'/bin/termux-media-player'):
	print 'Please Use Termux For This Player\n\tMake Sure You Installed Termux:API\n\t\tpkg install termux-api'
	Exit()
if not os.path.isfile('mp3.list'):
	genlist()

f=open("mp3.list","r")
a=f.read()
f.close()
p=a.split("\n")
p.remove('')
sname=[]
flg=True
while flg:
	flg1=True
	for pr in p:
		if not os.path.exists(pr):
			p.remove(pr)
			flg1=False
	if flg1:
		flg=False

if len(p) ==0:
	print "No Songs Found in here!!"
	print "Songs with .mp3 extension are recognised only !!!"
	Exit()
cols=int(os.popen('echo $COLUMNS').read().split('\n')[0])
for pr in p:
	l=pr.rfind('/')+1
	if l==0:
		continue
	ap=pr[l:len(pr)-4]
	dif=len(ap)-cols+30
	if dif>0:
		ap=ap[:len(ap)-dif]
        sname.append(ap)

print 'Songs Loaded !!!'
os.system("clear")
n=0
k=randint(0,len(p)-1)
n=k
pos=0
empl=500+len(p)*10
#lins='─'
lins='-'
while n < len(p):
	fg=True
	cols=int(os.popen('echo $COLUMNS').read().split('\n')[0])
	lin=lins*cols
	flag=True
	for cl in range(0,empl):
		print
	os.system('clear')
	os.system("echo -e \"\e[1;31m\"")
	os.system("toilet -f mono12 -F border     TPlay   ")
	os.system("echo -e \"\e[1;33m\"")
	os.system("printf \"%${COLUMNS}s\\n\" \"Created By SpeedX      \"")
	os.system("echo -e \"\e[1;32m\"")
	os.system('echo ')
        for i in range(0,len(p)):
                if i==n:
                        print str(i+1)+"\t| -->   "+sname[i]+"   (PLAYING)"
                else:
                        print str(i+1)+"\t|       "+sname[i]
		print lin
	playing=True
	if not getState() or pos!=n:
		pos=n
		os.popen("termux-media-player play \""+p[pos]+"\"")
	print 'Now Playing: '+p[pos]
	ref=False
	while True:
		inp=''
		try:
			inp=raw_input('TPlay > ').strip()
		except:
			print 'Some Exception Occurred!!!'
			os.popen("rm info.xx")
			os.popen("termux-media-player stop")
			print "Exiting Player...\n"
			Exit()
		if inp.strip().lower().find('quit')!=-1 or inp.strip().lower().find('exit')!=-1:
			os.popen("rm info.xx")
			os.system("termux-media-player stop")
			print "Exiting Player...\n"
			Exit()
		elif inp.strip() == "":
			if not getState():
				break
		elif inp.strip().lower().find("play") != -1:
			try:
				k=int(inp[5:len(inp)])-1
				if k>=len(p) or k<0:
					print 'Sorry Can\'t Play That Song !!!\n\t\t You Have Only '+str(len(p))+' Songs'
					print '\tChoose Between 1 To '+str(len(p))+' Songs'
				else:
					n=k
					fg=False
					ref=True
					break
			except:
				os.system('termux-media-player play')
		elif inp.lower().find('pause') !=-1:
			os.system('termux-media-player pause')
		elif inp.lower().find('next') !=-1:
			n=n+1
			fg=False
			ref=True
			break
		elif inp.lower().find('prev') !=-1:
			n=n-1
			fg=False
			ref=True
			break
		elif inp.lower().find('rand') !=-1:
			n=randint(0,len(p)-1)
			ref=True
			break
		elif inp.lower().find('reload') !=-1:
			print 'Recreating List....'
			genlist()
			dislist()
			n=randint(0,len(p)-1)
			ref=True
			break
		elif inp.lower().find('sort') !=-1:
			nsg=p[n]
			sortlist()
			n=p.index(nsg)
			#n=randint(0,len(p)-1)
			ref=True
			break
		elif inp.lower().strip().find('remove') !=-1:
			try:
				r=int(inp[7:len(inp)])-1
				remove(r)
				if n==r:
					os.popen('termux-media-player stop')
					n=randint(0,len(p)-1)
				else:
					if pos>r:
						pos=pos-1
						n=pos
				ref=True
				break
			except:
				print 'Please Enter A Number ...'
				print 'Usage:\nremove <track_nukber> - Removes Song With Respective Number From PlayList'
		elif inp.lower().find('ref') !=-1:
			cols=int(os.popen('echo $COLUMNS').read().split('\n')[0])
			for pr in range(len(p)):
				l=p[pr].rfind('/')+1
				if l==0:
					continue
				ap=p[pr][l:len(p[pr])-4]
				dif=len(ap)-cols+30
				if dif>0:
					ap=ap[:len(ap)-dif]
			        sname[pr]=ap
			ref=True
			break
		elif inp.lower().find('info') !=-1:
			subprocess.call("termux-media-player info >info.xx",shell=True)
			f1=open("info.xx","r")
			print f1.read()
			f1.close()
		elif inp.lower().find('help') !=-1:
			print """
	Available Commands are:---
		play                  - Plays Paused Music
		play <track_number>   - Plays The Song With That Track Number ( EX- play 3 )
		pause                 - Pauses Playing Music
		next                  - Plays Next Song
		prev                  - Plays Previous Song
		random                - Plays Random Song
		quit / exit           - Stops Playing Music And Exits Player
		info                  - Gets Info of Currently Playing Song
		reload                - Rescans The Phone Memory For MP3 files and creates A New List
		ref                   - Refreshes The Screen
		remove <track_number> - Removes Song With Respective Number From PlayList
		sort                  - Sort The List According To Path

"""
		else:
			print 'INVALID COMMAND\nType help for details...'
			if not getState():
				break
	if  n >= len(p):
		n=0
	elif n<0:
		n=len(p)-1
	if ref and getState():
		continue
	if getState()==False and fg:
		n=n+1
		if  n >= len(p):
			n=0
		elif n<0:
			n=len(p)-1
