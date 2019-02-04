import os
import nmap
import sys
import csv
import datetime
from threading import *
import multiprocessing
import pandas as pd
from openpyxl import load_workbook


def main():
	now = datetime.datetime.now()
	nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
	print ('###########################################')
	print ('######## Starting Auto Port Scanner #######')
	print ('###########################################')
	print ('### Starting Time :  '+ nowDatetime + '###')
	print ('###########################################')
	print (' version _ 2.0 / Made By Zeromini')
	time_manager(nowDatetime)


def file_read_scan(ip_addr):
	nm = nmap.PortScanner()
	print('Scanning Ip Address : ' + ip_addr)
	result = nm.scan(hosts=ip_addr, ports='20,21,22,23,25,69,80,123,137,138,139,443,445,512,513,514,1433,1434,1521,1522,1523,3306,3389,5500,5800,5900,6000,7000,7001,7090,8000,8001,8008,8080,9000,9001,9043,9090,9100,9744', arguments='-sV')
	with open('c:/result.csv','a') as f:		
		f.writelines(nm.csv())
		print('Saving Result....')


def excel_change():
	print( 'Changing Excel Result.... ')
	read_excel = pd.read_csv('c:/result.csv',sep=';')
	read_excel.to_excel('c:/final_result.xlsx')
	
	'''
	read_excel_replace = read_excel.replace('host;hostname;hostname_type;protocol;port;name;state;product;extrainfo;reason;version;conf;cpe',None)
	read_excel_drop = read_excel_replace.dropna(axis=1)
	read_excel_drop_final = read_excel_drop['host;hostname;hostname_type;protocol;port;name;state;product;extrainfo;reason;version;conf;cpe'].str[0:-1].str.split(';',expand=True)
	read_excel_drop_final.columns = ['host','hostname','hostname_type','protocol','port','name','state','product','extrainfo','reason','version','conf','cpe']
	read_excel_drop_final.to_excel('c:/merge/final_result_'+list_count+'.xlsx')
	os.remove('c:/result.csv')
	'''

def merge_excel():
	
	path_dir ='c:/merge/'
	file_list = os.listdir(path_dir)
	df = pd.DataFrame()
	for i in file_list:
		sort_excel = pd.read_excel('c:/merge/'+i)
		df = df.append(sort_sxcel,ignore_index=True)
	df.to_excel('c:/final_result.xlsx')	



def join_manager():
	print('Join Table for manager')
	read_result_scan = pd.read_excel('c:/final_result.xlsx', sheet_name='Sheet1')
	print('Duplicated Delete')
	read_result_scan_2 = read_result_scan.drop_duplicates()
	print(read_result_scan_2)
	read_manager_list = pd.read_excel('c:/manager.xlsx', sheet_name='Sheet1')
	print(read_manager_list)
	join_managers = pd.merge(read_result_scan_2, read_manager_list, how='outer')
	print(join_managers)
	columnsTitles = ['host','team','manager','hostname','hostname_type','protocol','port','name','state','product','extrainfo','reason','version','conf','cpe']
	reindex_join_managers = join_managers.reindex(columns=columnsTitles)
	print(reindex_join_managers)
	reindex_join_managers.to_excel('c:/manager_result.xlsx')


def time_manager(nowDatetime):
	print(nowDatetime)


def organize_data():
	print (' Organize_data....')
	organ_data = pd.read_excel('c:\manager_result.xlsx', sheet_name='Sheet1')
	organ_data_clear = organ_data.dropna(axis=0, subset=('state',))
	print (' Result...')
	organ_data_clear.to_excel('c:/000_portscan_result.xlsx')

def seperate_sheet():
	print(' ..... Ing...')
	seperate_sheets = pd.read_excel('c:/000_portscan_result.xlsx')
	seperate_sheets_del = seperate_sheets.drop([0,0], axis=0)
	port_numbers = ['20','21','22','23','25','69','80','123','137','138','139','443','445','512','513','514','1433','1434','1521','1522','1523','3306','3389','5500','5800','5900','6000','7000','7001','7090','8000','8001','8008','8080','9000','9001','9043','9090','9100','9744']
	writer = pd.ExcelWriter('c:/000_portscan_result2.xlsx', engine='xlsxwriter')
	for ports_num in port_numbers:
		seperate_sheets_del_list = seperate_sheets_del[seperate_sheets_del.port == ports_num]
		print(seperate_sheets_del_list)
		seperate_sheets_del_result_list = seperate_sheets_del_list[seperate_sheets_del_list.state == 'open']
		print(seperate_sheets_del_result_list)
		seperate_sheets_del_result_list.to_excel(writer, sheet_name='Port '+ports_num)

	print('result')
	writer.save()
	print('seperate Sheets..! Finish')

if __name__ == '__main__':


	#sys.stdout = open('c:/port_log/Port_Scan_Log.txt','w')
	main()
    # Ver 1 Making Scanning Table
	print ('Read File and Scanning Ready....')
	print ('MultiProcessing Starting....')
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
	organize_data()
	print ('Seperate Sheets....')
	seperate_sheet()
	print ('DONE......')


	'''
	init = 0 # Sequence Control
	multi = 0 # Sequence Control #2
	limit = int(len(read_result)/10) # 200 line List Limit
	for i in range(limit):
		multi = multi + 1
		put_list = read_result[init*limit+1 : limit*multi]
		init = init + 1
		pool = multiprocessing.Pool(processes=10)
		pool.map(file_read_scan,put_list)
		pool.close()
		pool.join()
		print(' Finish Scan & Saving Result ')
		excel_change(multi)
		f = open ('c:/result.csv','w')
	excel_merge_module()
	join_manager()
	organize_data()
	print ('Seperate Sheets....')
	seperate_sheet()
	print ('DONE......')
	'''
