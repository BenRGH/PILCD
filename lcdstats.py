#!/usr/bin/python
import time

import Adafruit_CharLCD as LCD

from datetime import datetime

import psutil

import pyping

# Raspberry Pi pin configuration:
lcd_rs        = 25 
lcd_en        = 24
lcd_d4        = 23
lcd_d5        = 17
lcd_d6        = 21
lcd_d7        = 22
lcd_backlight = 4

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

# Initialize the LCD using the pins above.
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                           lcd_columns, lcd_rows, lcd_backlight)
						   
						   
#MY CODE

lcd.create_char(0,[10001,11011,10101,10001,11111,10001,10001,11111]) #monday
lcd.create_char(1,[11111,100,100,100,10001,10001,10001,11111]) #tuesday
lcd.create_char(2,[10001,10101,11011,10001,11111,11111,10000,11111]) #wednesday
lcd.create_char(3,[11111,100,100,100,10000,11111,10001,10001]) #thursday
lcd.create_char(4,[11111,10000,11100,10000,10110,11000,10000,10000]) #friday
lcd.create_char(5,[11111,11000,111,11111,1110,10001,10001,1111]) #saturday
lcd.create_char(6,[11111,11000,111,11111,10001,10001,10001,11111]) #sunday

def checkonlinehosts():
	#this uses nmap to scan the lan for online hosts, then filters the text
	#for just the number
        raw = str(nmap("-sP", "-PA21,22,25,3389", "192.168.1.1/24"))
        splitraw = raw.split(" ")
        rawhosts = splitraw[115] #NEEDS REWORK IF STRING CHANGES SIZE
        hosts = rawhosts[1] #this is a string btw
	
	return hosts
	
def checkping():
	#pings google and returns ms
        rawping = pyping.ping('8.8.8.8', 99) #REQUIRES ROOT, 99 is for timeout
        pingms = rawping.avg_rtt[:2] + "ms"
	
	return pingms

while True:
	d = datetime.today()
	date = str(d.day) + "/" + str(d.month) + "/" + str(d.year)[2:]
	
	if int(d.weekday()) == 0:
		dow = ' \x00 '
	elif d.weekday() == 1:
		dow = ' \x01 '
	elif d.weekday() == 2:
		dow = ' \x02 '
	elif d.weekday() == 3:
		dow = ' \x03 '
	elif d.weekday() == 4:
		dow = ' \x04 '
	elif d.weekday() == 5:
		dow = ' \x05 '
	elif d.weekday() == 6:
		dow = ' \x06 '
	
	#Row 1
	row1 = str(d.time())[:5] + dow + date + "\n"


        #get cpu percent and add a 0 if its a single digit
	cpupercent = str(int(psutil.cpu_percent()))
	
	if len(cpupercent) == 1:
		cpu_val = "0" + cpupercent + "% "
	else:
		cpu_val = cpupercent + "% "
	
	
	#Row 2
	row2 = cpu_val + checkping()
	
	lcd.clear()
	lcd.home()
	lcd.show_cursor(False)
	
	#print to display
	lcd.message(row1 + row2)
	
	time.sleep(1.0) #wait 1 sec
	







	
	
	
	
	
