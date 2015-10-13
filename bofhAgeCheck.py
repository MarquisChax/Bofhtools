# -*- coding: utf-8 -*-

from subprocess import Popen, PIPE, STDOUT
import time
import sys
import getpass
from datetime import datetime, timedelta

names = open("names.txt",'r')

print "Bofh name/age scraper"
passwd = getpass.getpass()

shell = Popen( "bofh", shell=True,stdin=PIPE,stdout=PIPE)
shell.stdin.write(passwd + '\n')

for line in names:
    inName = line.strip()
    inName = inName.replace(' ','*')
    shell.stdin.write('person find name "{0}"\n'.format(inName))

print "Done scraping data, evaluating"

text = shell.communicate()[0]
outPutList = text.splitlines(True)

map(lambda x: x.strip(),outPutList)

for line in outPutList:
    if 'bofh' in line or 'uio.no' in line or 'Password' in line:
        continue
    if 'Birth' in line:
        print "\n*****\n"
        continue

    print line.strip()
    lineElems = line.strip().split()
    bornDate = datetime.strptime(lineElems[1],'%Y-%m-%d')
    diffAge = datetime.now() - bornDate
    if(diffAge.days < 20*365):
        print "Underaged"
