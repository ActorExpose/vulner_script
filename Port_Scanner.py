import os
import nmap
import sys
import csv
from threading import *
from multiprocessing import Process
import pandas as pd



def main():
	print('port Scanning')


def file_read_scan():
	print (' Read File and Scanning Ready....')
	try:		
		r = open ('c:/iplist.txt', mode='rt')
		f = open ('c:/result.csv','w')
		read_result = [line.split('\n') for line in r.readlines()]
		r.close()
		f.close()
		nm = nmap.PortScanner()
		multi_flag = 0 

		for i in read_result:
			print('Scanning Ip Address : '+i[0])
			ip_put = str(line.replace('\n',''))
			result = nm.scan(hosts=i[0], ports='20', arguments='-sV')
			with open('c:/result.csv','a') as f:		
				f.writelines(nm.csv())
					
	

	except:
		pass
def excel_change():
	print( ' Changing Excel Result.... ')
	read_excel = pd.read_csv('c:/result.csv')
	read_excel_replace = read_excel.replace('host;hostname;hostname_type;protocol;port;name;state;product;extrainfo;reason;version;conf;cpe',None)
	read_excel_drop = read_excel_replace.dropna(axis=1)
	read_excel_drop_final = read_excel_drop['host;hostname;hostname_type;protocol;port;name;state;product;extrainfo;reason;version;conf;cpe'].str[0:-1].str.split(';',expand=True)
	read_excel_drop_final.columns = ['host','hostname','hostname_type','protocol','port','name','state','product','extrainfo','reason','version','conf','cpe']
	#print(read_excel_drop_final)
	read_excel_drop_final.to_excel('c:/final_result.xlsx')

	#read_result = read_excel.drop('host;hostname;hostname_type;protocol;port;name;state;product;extrainfo;reason;version;conf;cpe',axis=1)
	#print(read_result)
	#read_excel_split = read_excel.split(';',expand=True)
	#print(read_excel_split)

def multi_proc_scan():
	print(' Multi Process Scanning....')
	scan_proc = ['a','b','c','d','e','f','g']
	for proc_name in scan_proc:
		proc_name = Process(target=file_read_scan)
		proc_name.start()
		proc_name.join()
		
		#for i in range ()
		#i.start()
		#i.join()



'''
nm = nmap.PortScanner()
result = nm.scan(hosts='127.0.0.1', ports='20-443',arguments='-sV')

print(nm.csv())

with open('result.csv','w') as f:
	f.writelines(nm.csv().replace(';',','))
'''

if __name__ == '__main__':
    	#file_read_scan()
    	#excel_change()
    	multi_proc_scan()

    
