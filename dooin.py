import selenium
import time
import requests
import pandas
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # Service 모듈 가져오기

driver_path = "C:/chromedriver.exe"  # 드라이버 경로
service = Service(driver_path)  # Service 객체 생성
driver = webdriver.Chrome(service=service)  # service 인자 사용

url = 'https://www.dooinauction.com/'
driver.get(url)

#로그인 버튼 클릭
driver.find_element(By.XPATH, '//*[@id="header"]/div[1]/div[1]/div[1]/span[3]').click()
time.sleep(2)

#ID, PW 입력
login_ID = driver.find_element(By.XPATH, '//*[@id="client_id"]')
login_ID.send_keys('wolfht93')


login_ID = driver.find_element(By.XPATH, '//*[@id="passwd"]')
login_ID.send_keys('07llawliet!')


driver.find_element(By.XPATH, '//*[@id="loginUI"]/tbody/tr[5]/td/a').click()
time.sleep(2)

#원하는 메뉴 들어가기
driver.find_element(By.XPATH, '//*[@id="header"]/div[1]/div[1]/div[1]/span[3]').click()
time.sleep(1)

driver.find_element(By.XPATH, '//*[@id="aside"]/div[1]/div/ul/li[3]/a').click()
time.sleep(1)

driver.find_element(By.XPATH, '//*[@id="bookmarkListContent01"]/div/div/div/div[1]/div[1]/a/strong').click()
time.sleep(1)

data_frame = pandas.DataFrame([])

for m in range(2,4):
    for n in range(1,5):
        #목록에서 n번째 물건 클릭
        driver.find_element(By.XPATH, '//*[@id="Tr_{}"]/td[3]/div[4]'.format(n)).click()
        time.sleep(1)
    
        #새로 열린 페이지 선택
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(1)
    
        # 현재 페이지 HTML 가져오기
        html = driver.page_source
        
        # BeautifulSoup으로 HTML 파싱
        soup = BeautifulSoup(html, "html.parser")
    
        # 페이지의 모든 텍스트 가져오기
        text = soup.get_text(separator="\n", strip=True)
    
        
        #사건번호 추출
        try:
            title = soup.find("span", class_="f20 bold_900").text
            
        except:
            title = 'error'
    
        
        #물건 종류 추출
        try:
            target_th = soup.find("th", string="물건종류")
            property_type = target_th.find_next_sibling("td").text
    
        except:
            property_type = 'error'
    
        
        #도/시, 시/구, 구/동 추출
        try:
            address = driver.find_element(By.XPATH, '//*[@id="lyCnt_base"]/table/tbody/tr[1]/td/span[1]').text.strip()
            address = address.split()
            address1 = address[0] #도/시
            address2 = address[1] #시/구
            address3 = address[2] #구/동
    
        except:
            address1 = 'error'
            address2 = 'error'
            address3 = 'error'
        
    
        #층 추출
        try:
            if isinstance(address, list):
                address = " ".join(address)
            
            if any(keyword in address for keyword in ["지하", "지층", "지하층"]):
                floor = "반지하"
                
            else:
                address = driver.find_element(By.XPATH, '//*[@id="lyCnt_base"]/table/tbody/tr[1]/td/span[1]').text.strip().split()
                for i, floor in enumerate(address):
                    if "층" in floor:
                        break
                        
                position = floor.find("층")
                floor = floor[:position + 1]
    
        except:
            floor = 'error'
    
        #사용승인 추출
        try:
            approval = soup.find("span", string=lambda text: text and "사용승인일" in text)
            approval = approval.text.strip().split(':')
            approval = approval[1]
    
        except:
            approval = 'error'
    
        #감정가, 최저가, 퍼센트 추출
        try:
            og_price = driver.find_element(By.XPATH, '//*[@id="lyCnt_base"]/table/tbody/tr[3]/td[3]/span').text.strip()
            law_price = driver.find_element(By.XPATH, '//*[@id="lyCnt_base"]/table/tbody/tr[4]/td[3]/span').text.strip().split()[1]
            percent = driver.find_element(By.XPATH, '//*[@id="lyCnt_base"]/table/tbody/tr[4]/td[3]/span').text.strip().split()[0].split('(')[1].split(')')[0]
    
        except:
            og_price = 'error'
            law_price = 'error'
            percent = 'error'
    
        print(f'{(m-2)*20 + n}번째 물건, {title}, {property_type}, {address1}, {address2}, {address3}, {floor}, {approval}, {og_price}, {law_price}, {percent}')

        new_data_frame = pandas.DataFrame([[title, property_type, address1, address2, address3, floor, approval, og_price, law_price, percent]], columns = ['사건 번호', '종류', '도/시', '시/구', '구/동', '층', '사용승인', '감정가', '최저가', '퍼센트'])
        
        data_frame = pandas.concat([data_frame, new_data_frame],axis=0)
        
        
        driver.close()
        time.sleep(1)
    
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)

    #다음 페이지로 넘어가기
    driver.find_element(By.XPATH, '//*[@id="loadPage_{}"]'.format(m)).click()
    time.sleep(2)

data_frame

data_frame.to_excel('C:\임형태/dooin1210xlsx', index = False)
