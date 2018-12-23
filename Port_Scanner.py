import os
import nmap
import sys
import csv
from threading import *
import multiprocessing
import pandas as pd




def main():
	print('port Scanning')


def file_read_scan(ip_addr):
	#print (' Read File and Scanning Ready....')

	'''
	try:		
		r = open ('c:/iplist.txt', mode='rt')
		f = open ('c:/result.csv','w')
		read_result = [line.strip() for line in r.readlines()]
		print(read_result)
		#r.close()
		#f.close()
		nm = nmap.PortScanner()
		multi_flag = 0 


		for i in read_result: 
			print('Scanning Ip Address : '+i)
			result = nm.scan(hosts=i, 
							ports='20,21,23,69,137,138,139,445,512,513,514,5500,5800,5900,22,3389,60000,1433,1434,1521,1522,1523,3306,80,443,80000,8008,8080,9000,7001,9744,7000,7090,8001,9001,9043,9090,9100,25,123', arguments='-sV')
			with open('c:/result.csv','a') as f:		
				f.writelines(nm.csv())			
	'''
	nm = nmap.PortScanner()
	print('Scanning Ip Address : ' + ip_addr)
	result = nm.scan(hosts=ip_addr, ports='20,21,22,23,25,69,80,123,137,138,139,443,445,512,513,514,1433,1434,1521,1522,1523,3306,3389,5500,5800,5900,6000,7000,7001,7090,8000,8001,8008,8080,9000,9001,9043,9090,9100,9744', arguments='-sV')
	with open('c:/result.csv','a') as f:		
		f.writelines(nm.csv())
		print('Saving Result....')


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

def join_manager():
	print('Join Table for manager')
	read_result_scan = pd.read_excel('c:/final_result.xlsx', sheet_name='Sheet1')
	print(read_result_scan)
	read_manager_list = pd.read_excel('c:/manager.xlsx', sheet_name='Sheet1')
	print(read_manager_list)
	join_managers = pd.merge(read_result_scan, read_manager_list, how='outer')
	print(join_managers)
	columnsTitles = ['host','team','manager','hostname','hostname_type','protocol','port','name','state','product','extrainfo','reason','version','conf','cpe']
	reindex_join_managers = join_managers.reindex(columns=columnsTitles)
	print(reindex_join_managers)
	reindex_join_managers.to_excel('c:/manager_result.xlsx')
	#read_excel_manager = pd.read_csv('c:/manager.xlsx')
	#print(read_excel_manager)



'''
nm = nmap.PortScanner()
result = nm.scan(hosts='127.0.0.1', ports='20-443',arguments='-sV')

print(nm.csv())

with open('result.csv','w') as f:
	f.writelines(nm.csv().replace(';',','))
'''

if __name__ == '__main__':

    # Ver 1 Making Scanning Table
	print (' Read File and Scanning Ready....')
	print (' MultiProcessing Starting....')
	r = open ('c:/iplist.txt', mode='rt')
	f = open ('c:/result.csv','w')
	read_result = [line.strip() for line in r.readlines()]
	pool = multiprocessing.Pool(processes=10)
	pool.map(file_read_scan,read_result)
	pool.close()
	pool.join()
	print(' Finish Scan & Saving Result ')
	excel_change()
	join_manager()


    
