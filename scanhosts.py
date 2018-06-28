#!/usr/bin/python
from sh import nmap
import os

#RUN THIS SCRIPT AS SUDO

def getHosts():
    #this uses nmap to scan the lan for online hosts, then filters the text
    #for just the number
    raw = str(nmap("-sP", "-PA21,22,25,3389", "192.168.1.1/24"))
    splitraw = raw.split(" ")
    rawhosts = splitraw[-7]
    hosts = rawhosts[1] #this is a string btw
    
    return hosts
    
#Stick the number of online hosts into the file
i = 0
while i<10:
    output = open('onlinehosts.txt','w')
    output.write(str(getHosts()))
    output.close()
    i = i + 1
