import os
import nmap
import sys
import csv
from threading import *
import pandas as pd

global result


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
		file_flag = 0 

		for i in read_result:
			print('Scanning Ip Address : '+i[0])
			ip_put = str(line.replace('\n',''))
			result = nm.scan(hosts=i[0], ports='20-443', arguments='-sV')
			with open('c:/result.csv','a') as f:		
				f.writelines(nm.csv())
					
	

	except:
		pass
def excel_change():
	print( ' Changing Excel Result.... ')
	read_excel = pd.read_csv('c:/result.csv')
	#print(read_excel)
	read_excel_replace = read_excel.replace('host;hostname;hostname_type;protocol;port;name;state;product;extrainfo;reason;version;conf;cpe',None)
	read_excel_drop = read_excel_replace.dropna(axis=1)
	#print(read_excel_drop)
	read_excel_drop.to_excel('c:/final_result.xlsx')

	#read_result = read_excel.drop('host;hostname;hostname_type;protocol;port;name;state;product;extrainfo;reason;version;conf;cpe',axis=1)
	#print(read_result)
	#read_excel_split = read_excel.split(';',expand=True)
	#print(read_excel_split)




'''
nm = nmap.PortScanner()
result = nm.scan(hosts='127.0.0.1', ports='20-443',arguments='-sV')

print(nm.csv())

with open('result.csv','w') as f:
	f.writelines(nm.csv().replace(';',','))
'''

if __name__ == '__main__':
    	file_read_scan()
    	excel_change()

    
