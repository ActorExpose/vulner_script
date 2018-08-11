''' 
# 관리자 페이지 자동 점검 스크립트    # 
# 개발일 / 버전 : `18.8.5 / V 1.0  # 
# 아이디어 : GoldStone / 개발 : zeromini # 
''' 

# 필요 라이브러리 임포트
from selenium import webdriver
import os
import time

print('#####################################') 
print('Admin Page Auto Check Script') 
print('Idea By : GoldStone / Dev By : Zeromini') 
print('Script Version : V 1.0 / 18_8_5') 
print('#####################################') 


# 해당 브라우저 드라이버 구동 (인터넷 익스플로어)
browser = webdriver.Ie('c:/IEDriverServer.exe')
# browser.set_page_load_timeout(15) # 자동 타임아웃 설정 (필요시) / 기본 : 설정 안함
r = open('e:/list.txt', mode='rt', encoding='utf-8') #해당 디렉토리 텍스트 불러오기
overrideLink = 0 # 초기값 (인증서 페이지 뜨면 1로 바꿔서 구동하면됨)

for line in r: #해당 디렉토리 라인마다 출력
    print('====== Stating Admin Checking =====')
    print(str(line)+' Read and Check.....')
    browser.get('http://'+line) #80 / https 인경우에는 바꿔주면됨../ 뒤에 포트 넣을경우 : 추가
    file_url = str(line)
    time.sleep(10) # 웹사이트 구동
    if overrideLink == 1: # 80인데 443 리다이렉션 되는경우 자동 클릭 매크로(보안인증서 관련 페이지 출력시)
        overrideLink = browser.find_element_by_id('overridelink')
        time.sleep(3) # 3초대기
        overrideLink.click() # 클릭 시행
        time.sleep(3)
        browser.save_screenshot('e:/initial.png') #초기 파일 생성 또는 스크린샷
        print(line+'해당 페이지는 80에서 443 으로 리다리렉션됨')
        print('정상 스크린샷 완료 ')
    else : 
        browser.save_screenshot('e:/initial.png') #초기 파일 생성 또는 스크린샷 
        print('정상 스크린샷 완료 ')
    time.sleep(3)
    os.rename('e:/initial.png','e:/'+(file_url.replace('\n',''))+'.png') #해당 파일 변경

browser.quit() # 브라우저 드라이버 종료
r.close() # 파일 종료
