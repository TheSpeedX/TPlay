import os
import time
from random import *
import sys
import threading
import subprocess

playing=False



f=open("mp3","r")
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
for pr in p:
	if os.path.exists(pr):
		i=0
		l=0
		while i!=-1:
			i=pr.find("/",i+1)
			if i!=-1:
				l=i+1
	        sname.append(pr[l:len(pr)-4])
if len(p) ==0:
	print "No Songs Found in here!!"
	print "Songs with .mp3 extension are recognised only !!!"
	exit()
print str(len(p))+" songs Loaded !!"
print "Press Enter To Start Playing"
raw_input()
os.system("clear")
n=0
lin=""
for li in range(0,80):
	lin+="-"
k=randint(0,len(p)-1)
n=k
while n < len(p):
	flag=True
	empl=500+len(p)*10
	for cl in range(0,empl):
		print
	os.system("echo -e \"\e[1;31m\"")
	os.system("toilet -f mono12 -F border     MPlay   ")
	os.system("echo -e \"\e[1;32m\"")
        for i in range(0,len(p)):
                if i==n:
                        print str(i+1)+"\t| -> "+sname[i]+" (PLAYING)"
                else:
                        print str(i+1)+"\t|    "+sname[i]
		print lin
	playing=True
	os.system("termux-media-player play \""+p[n]+"\"")
	#time.sleep(1)

	try:
		while playing:
			subprocess.call("termux-media-player info >info.xx",shell=True)
			f1=open("info.xx","r")
			a=f1.read()
			if len(a) >= 21:
				playing=True
				time.sleep(3)
			else:
				playing=False
			f1.close()

	except:
		print "\nSome exception here"
		print "Press Enter for next Song Or q to Quit"
		inp=raw_input()
		if inp == "q" or inp == "Q":
			os.system("rm info.x")
			os.system("termux-media-player stop")
			print "Exiting Player..."
			exit()
		elif inp.find("play") != -1:
			n=int(inp[5:len(inp)])-2
		else:
			n=n+1
			continue
	n=n+1
	if  n >= len(p):
		n=0

