'''
# 액셀 자동 합침 및 ',' 분류 스크립트 #
# 개발일 / 버전 : `18.8.5 / V 1.0  #
# 아이디어 : GoldStone / 개발 : zeromini #
'''

# 필요 라이브러리 임포트 #
import os
import pandas as pd
import time

# 초기파일 설정 플래그
flag = int(1)

print('#####################################')
print('Excel Auto Cell Add & Seperate Script')
print('Idea By : GoldStone / Dev By : Zeromini')
print('Script Version : V 1.0 / 18_8_5')
print('#####################################')

path_dir = 'c:/' #액셀 파일 넣는 폴더 무조건 다 쳐넣으면 알아서 액셀 붙여줌
file_list = os.listdir(path_dir)
for item in file_list:
    if item.find('.xlsx') is not -1: # xlsx 확장자 읽음
            print(item+  'Read Finish....^___^')
            df = pd.read_excel('c:/'+item) # 데이터 프레임 넣음
            if flag == 1:  # 초기 데이터 삽입 부분
                df2 = pd.read_excel('c:/default.xlsx') #해당 디렉토리에 Default 액셀 필요
                flag = int(0)
                result = pd.concat([df,df2])
                print ('Initial Setting Finish')
            else :
                result = pd.concat([df,result])
result.to_excel('c:/result.xlsx') #결과 파일 설정 
print('===== Finish Excel Add.... ====')
time.sleep(10) #해당 파일이 생성될때 까지 대기 시간
print('===== Excel Split Start ====')
excel_result = pd.read_excel('c:/result.xlsx') #결과 파일 설정 액셀 Read
excel_split_result = excel_result['TCP Ports'].str.split(',', expand=True) # 파일쪼개기
excel_final_result=pd.concat([excel_result,excel_split_result],axis=1) # 데이터프레임 1, 2 합치기 (더하기)
excel_final_result.to_excel('c:/final_result.xlsx') # 최종 결과 파일 설정