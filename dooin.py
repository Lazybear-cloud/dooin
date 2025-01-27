import pyautogui
import selenium
import time
import requests as rq
import pyperclip
import pandas
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#크롬 여는 명령
from selenium import webdriver
driver = webdriver.Chrome()
url = 'https://www.dooinauction.com/'
driver.get(url)
time.sleep(2)

#로그인 버튼 클릭
driver.find_element(By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/div[3]/a').click()
time.sleep(2)

#ID, PW 입력
login_ID = driver.find_element(By.XPATH, '//*[@id="login_form"]/div[1]/input[1]')
login_ID.send_keys('wolfht93')


login_ID = driver.find_element(By.XPATH, '//*[@id="login_form"]/div[1]/input[2]')
login_ID.send_keys('07llawliet!')


driver.find_element(By.XPATH, '//*[@id="login_form"]/a').click()
time.sleep(2)


#원하는 메뉴 들어가기
driver.find_element(By.XPATH, '//*[@id="menu-item-130"]/a').click()

driver.find_element(By.XPATH, '//*[@id="search-form"]/div[1]/div[2]/div/div/div[4]/div/button[2]/span').click()
time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="searchLoadModal"]/div/div/div/div[2]/div/div[2]/ul/li[1]/div/div/label').click()

driver.find_element(By.XPATH, '//*[@id="searchLoadModal"]/div/div/div/div[3]/button[2]').click()
time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="search-form"]/div[2]/div/div[1]/div[2]/a[4]').click()
time.sleep(2)

#반복문 - 새로운 물건 클릭하여 DataFrame에 누적하여 입력하는 코드

data_frame = pandas.DataFrame([])



############################################################ 물건 정보 추출 시작 ############################################################
for m in range(2, 200):
    for i in range(1,31):
        
        # i번째 메뉴 클릭
        driver.find_element(By.XPATH, '//*[@id="search-form"]/div[2]/div/div[1]/div[3]/div[2]/div[{}]/div/div[3]/div/span'.format(i)).click()
        time.sleep(2)
    
     
        #새로 열린창 선택
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(1)
    
        try:
            #비고란만 추출
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')

            try:
                post1 = soup.select_one('#search-form > div.window-pop-product-view.product-view > div.product-view-detail > div.view-data.square-shadow-box > div.view-content-wrap > div:nth-child(3) > table > tbody > tr:nth-child(4) > td')
                print(post1.text)
               
                post2 = soup.select_one('#search-form > div.window-pop-product-view.product-view > div.product-view-detail > div.view-data.square-shadow-box > div.view-content-wrap > div:nth-child(3) > table > tbody > tr:nth-child(5) > td')
                print(post2.text)
    
                post3 = soup.select_one('#search-form > div.window-pop-product-view.product-view > div.product-view-detail > div.view-data.square-shadow-box > div.view-content-wrap > div:nth-child(3) > table > tbody > tr:nth-child(6) > td')
                print(post3.text)
    
                post4 = soup.select_one('#search-form > div.window-pop-product-view.product-view > div.product-view-detail > div.view-data.square-shadow-box > div.view-content-wrap > div:nth-child(3) > table > tbody > tr:nth-child(7) > td')
                print(post4.text)

            except:
                try:
                    post1 = soup.select_one('#search-form > div.window-pop-product-view.product-view > div.product-view-detail > div.view-data.square-shadow-box > div.view-content-wrap > div:nth-child(3) > table > tbody > tr:nth-child(4) > td')
                    print(post1.text)
                   
                    post2 = soup.select_one('#search-form > div.window-pop-product-view.product-view > div.product-view-detail > div.view-data.square-shadow-box > div.view-content-wrap > div:nth-child(3) > table > tbody > tr:nth-child(5) > td')
                    print(post2.text)
        
                    post3 = soup.select_one('#search-form > div.window-pop-product-view.product-view > div.product-view-detail > div.view-data.square-shadow-box > div.view-content-wrap > div:nth-child(3) > table > tbody > tr:nth-child(6) > td')
                    print(post3.text)

                    post4 = soup.select_one('#search-form > div.window-pop-product-view.product-view > div.product-view-detail > div.view-data.square-shadow-box > div.view-content-wrap > div:nth-child(3) > table > tbody > tr:nth-child(6) > td')

                except:
                    try:
                        post1 = soup.select_one('#search-form > div.window-pop-product-view.product-view > div.product-view-detail > div.view-data.square-shadow-box > div.view-content-wrap > div:nth-child(3) > table > tbody > tr:nth-child(4) > td')
                        print(post1.text)
                       
                        post2 = soup.select_one('#search-form > div.window-pop-product-view.product-view > div.product-view-detail > div.view-data.square-shadow-box > div.view-content-wrap > div:nth-child(3) > table > tbody > tr:nth-child(5) > td')
                        print(post2.text)

                        post3 = soup.select_one('#search-form > div.window-pop-product-view.product-view > div.product-view-detail > div.view-data.square-shadow-box > div.view-content-wrap > div:nth-child(3) > table > tbody > tr:nth-child(5) > td')

                        post4 = soup.select_one('#search-form > div.window-pop-product-view.product-view > div.product-view-detail > div.view-data.square-shadow-box > div.view-content-wrap > div:nth-child(3) > table > tbody > tr:nth-child(5) > td')

                    except:
                        post1 = soup.select_one('#search-form > div.window-pop-product-view.product-view > div.product-view-detail > div.view-data.square-shadow-box > div.view-content-wrap > div:nth-child(3) > table > tbody > tr:nth-child(4) > td')
                        print(post1.text)

                        post2 = soup.select_one('#search-form > div.window-pop-product-view.product-view > div.product-view-detail > div.view-data.square-shadow-box > div.view-content-wrap > div:nth-child(3) > table > tbody > tr:nth-child(4) > td')
            
                        post3 = soup.select_one('#search-form > div.window-pop-product-view.product-view > div.product-view-detail > div.view-data.square-shadow-box > div.view-content-wrap > div:nth-child(3) > table > tbody > tr:nth-child(4) > td')

                        post4 = soup.select_one('#search-form > div.window-pop-product-view.product-view > div.product-view-detail > div.view-data.square-shadow-box > div.view-content-wrap > div:nth-child(3) > table > tbody > tr:nth-child(4) > td')
            
            
            #추출한 텍스트에 특정 단어가 포함되어 있으면 type에 '근생 빌라'라고 저장
            find_text1 = '사무' in post1.text
            find_text2 = '제2종근린생활시설' in post1.text
            find_text3 = '의원' in post1.text
            
            
            find_text4 = '사무' in post2.text
            find_text5 = '제2종근린생활시설' in post2.text
            find_text6 = '의원' in post2.text
            
            find_text7 = '사무' in post3.text
            find_text8 = '제2종근린생활시설' in post3.text
            find_text9 = '의원' in post3.text
            
            find_text10 = '사무' in post4.text
            find_text11 = '제2종근린생활시설' in post4.text
            find_text12 = '의원' in post4.text
            
            if find_text1 == True:
                type = '근생 빌라'
            
            elif find_text2 == True: 
                type = '근생 빌라'
            
            elif find_text3 == True:
                type = '근생 빌라'

            elif find_text4 == True:
                type = '근생 빌라'

            elif find_text5 == True: 
                type = '근생 빌라'
            
            elif find_text6 == True:
                type = '근생 빌라'

            elif find_text7 == True:
                type = '근생 빌라'

            elif find_text8 == True: 
                type = '근생 빌라'
            
            elif find_text9 == True:
                type = '근생 빌라'

            elif find_text10 == True:
                type = '근생 빌라'

            elif find_text11 == True: 
                type = '근생 빌라'
            
            elif find_text12 == True:
                type = '근생 빌라'
            
            else:
        
                try:
                    type = driver.find_element(By.XPATH, '//*[@id="search-form"]/div[1]/div[1]/div[2]/div[2]/div[3]/div/table/tbody/tr[2]/td[1]').text
        
                except:
                    type = driver.find_element(By.XPATH, '//*[@id="search-form"]/div[1]/div[1]/div[2]/div[1]/div[3]/div/table/tbody/tr[2]/td[1]').text
                  
            print(type)

            
            #추출한 텍스트에 특정 단어가 포함되어 있으면 illegal에 '위반'이라고 저장
            find_text20 = '위반건축물' in post1.text
            find_text21 = '위반건축물' in post2.text
            find_text22 = '위반건축물' in post3.text
            find_text23 = '위반건축물' in post4.text
                        
            if find_text20 == True:
                illegal = '위반'

            elif find_text21 == True:
                illegal = '위반'

            elif find_text22 == True:
                illegal = '위반'

            elif find_text23 == True:
                illegal = '위반'
            
            else:
                illegal = '위반아님'
                                  
            print(illegal)

            #물건명 가져오기
            title = driver.find_element(By.CLASS_NAME, 'list-cell')
            print(title.text)
            
            #주소 가져오기
            location = driver.find_element(By.CLASS_NAME, 'text-align-left')
            print(location.text)

            #층수 가져오기
            find_text1_1 = '지하' in location.text

            if find_text1_1 == True:
                floor = '반지하'

            else:
                floor = ''

            print(floor)
            
            #감정가 가져오기
            start_price = driver.find_element(By.CLASS_NAME, 'color-black')
            print(start_price.text)
            
            #최저가 가져오기
            low_price = driver.find_element(By.CLASS_NAME, 'color-cornflower')
            print(low_price.text)
            
            #사용승인일 가져오기
            try:
                build_date = driver.find_element(By.XPATH, '//*[@id="search-form"]/div[1]/div[1]/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[3]/div')
                    
            except:
                try:
                    build_date = driver.find_element(By.XPATH, '//*[@id="search-form"]/div[1]/div[1]/div[2]/div[3]/div[2]/table/tbody/tr[2]/td[3]/div')
                
                except:
                    try:
                        build_date = driver.find_element(By.XPATH, '//*[@id="search-form"]/div[1]/div[1]/div[2]/div[2]/div[2]/table/tbody/tr[3]/td[3]/div')
                    except:
                        try:
                            build_date = driver.find_element(By.XPATH, '//*[@id="search-form"]/div[1]/div[1]/div[2]/div[3]/div[2]/table/tbody/tr[3]/td[3]/div')

                        except:
                            try:
                                #사용승인일이 없을 때
                                build_date = driver.find_element(By.XPATH, '//*[@id="search-form"]/div[1]/div[1]/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[3]')

                            except:
                                #사용승인일이 없을 때(물건 번호가 여러개일 때)
                                build_date = driver.find_element(By.XPATH, '//*[@id="search-form"]/div[1]/div[1]/div[2]/div[3]/div[2]/table/tbody/tr[2]/td[3]')


            try:
                #배당, 미배당, 인수금액 가져오기
                devidends = driver.find_element(By.XPATH, '//*[@id="search-form"]/div[1]/div[1]/div[2]/div[2]/div[5]/table/tbody/tr[1]/td[6]/div[1]')
                        
                none_devidends = driver.find_element(By.XPATH, '//*[@id="search-form"]/div[1]/div[1]/div[2]/div[2]/div[5]/table/tbody/tr[1]/td[6]/div[2]')
                       
                acquisition_amount = driver.find_element(By.XPATH, '//*[@id="search-form"]/div[1]/div[1]/div[2]/div[2]/div[5]/table/tbody/tr[1]/td[6]/div[3]')
                             
            except:
        
                try:
                    #배당, 미배당, 인수금액 가져오기 (물건 번호가 여러개일 때)
                    devidends = driver.find_element(By.XPATH, '//*[@id="search-form"]/div[1]/div[1]/div[2]/div[3]/div[5]/table/tbody/tr[1]/td[6]/div[1]')
                               
                    none_devidends = driver.find_element(By.XPATH, '//*[@id="search-form"]/div[1]/div[1]/div[2]/div[3]/div[5]/table/tbody/tr[1]/td[6]/div[2]')
                               
                    acquisition_amount = driver.find_element(By.XPATH, '//*[@id="search-form"]/div[1]/div[1]/div[2]/div[3]/div[5]/table/tbody/tr[1]/td[6]/div[3]')
                           
                except:
                    try:
                        #임차인이 없는 경우
                        devidends = driver.find_element(By.XPATH, '//*[@id="search-form"]/div[1]/div[1]/div[2]/div[2]/div[5]/table/tbody/tr/td')
                        none_devidends = driver.find_element(By.XPATH, '//*[@id="search-form"]/div[1]/div[1]/div[2]/div[2]/div[5]/table/tbody/tr/td')
                        acquisition_amount = driver.find_element(By.XPATH, '//*[@id="search-form"]/div[1]/div[1]/div[2]/div[2]/div[5]/table/tbody/tr/td')
        
                    except:
                        #임차인이 없는 경우 (물건 번호가 여러개일때)
                        devidends = driver.find_element(By.XPATH, '//*[@id="search-form"]/div[1]/div[1]/div[2]/div[3]/div[5]/table/tbody/tr/td')
                        none_devidends = driver.find_element(By.XPATH, '//*[@id="search-form"]/div[1]/div[1]/div[2]/div[3]/div[5]/table/tbody/tr/td')
                        acquisition_amount = driver.find_element(By.XPATH, '//*[@id="search-form"]/div[1]/div[1]/div[2]/div[3]/div[5]/table/tbody/tr/td')
    
            #error가 없을 경우 Data Frame 만들기
            new_data_frame = pandas.DataFrame([[title.text, type, location.text.split()[0], location.text.split()[1], location.text.split()[2], illegal, build_date.text.split('.')[0][5:], floor, start_price.text[:-1], low_price.text.split()[1][:-1], low_price.text.split()[0], devidends.text, none_devidends.text, acquisition_amount.text]], columns = ['물건 번호', '종류', '지역', '지역', '지역', '위반',  '사용승인', '층', '감정가', '최저가', '퍼센트', '배당액', '미배당', '인수액'])



        except:
            try:
                title = driver.find_element(By.CLASS_NAME, 'list-cell')
                new_data_frame = pandas.DataFrame([[title.text, type, 'error 발생', 'error 발생', 'error 발생', 'error 발생', 'error 발생', 'error 발생', 'error 발생', 'error 발생', 'error 발생', 'error 발생']], columns = ['물건 번호', '종류', '지역', '지역', '지역', '위반', '사용승인', '층', '감정가', '최저가', '퍼센트', '배당액', '미배당', '인수액'])

            except:
                new_data_frame = pandas.DataFrame([['창이 안뜸', '창이 안뜸', '창이 안뜸', '창이 안뜸', '창이 안뜸', '창이 안뜸', '창이 안뜸', '창이 안뜸', '창이 안뜸', '창이 안뜸', '창이 안뜸']], columns = ['물건 번호', '종류', '지역', '지역', '지역', '위반',  '사용승인', '층', '감정가', '최저가', '퍼센트', '배당액', '미배당', '인수액'])
    
        
        #Data Frame 만들기
        data_frame = pandas.concat([data_frame, new_data_frame],axis=0)
      
        
        #창 닫기
        driver.close()
        time.sleep(1)
    
        #Main창으로 돌아오기
        driver.switch_to.window(driver.window_handles[0])
    ############################################################ 물건 정보 추출 끝 ############################################################
    
    if m < 3:
        driver.find_element(By.XPATH, '//*[@id="search-form"]/div[2]/div/div[1]/div[3]/div[4]/ul/li[{}]/a'.format(m)).click()
        time.sleep(2)
  
    elif m < 9:
        driver.find_element(By.XPATH, '//*[@id="search-form"]/div[2]/div/div[1]/div[3]/div[4]/ul/li[{}]/a'.format(m+1)).click()
        time.sleep(2)
            
    else:
        try:
            driver.find_element(By.XPATH, '//*[@id="search-form"]/div[2]/div/div[1]/div[3]/div[4]/ul/li[9]/a').click()
            time.sleep(2)
           
        except:
            break


#Data Frame을 만들어서 Excel로 내보내기
data_frame

data_frame.to_excel('C:\임형태/dooin1210xlsx', index = False)