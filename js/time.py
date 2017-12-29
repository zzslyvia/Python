#coding=utf-8

import time
 
import calendar

# localtime = time.localtime(time.time())

localtime = time.asctime(time.localtime(time.time()))

cal=calendar.month(2018,1)

print("本地时间:", localtime)

print("2018年1月份:")

print cal;


str = input("please input:");
print ("the content is ",str)

f=open("a.txt","wb")
f.write("character......")
str = f.read();

f.close

print("wenjian:",f.name)



