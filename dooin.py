import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os

def run_crawler():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size=1920,1080')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    url = 'https://www.dooinauction.com/'
    driver.get(url)

    driver.find_element(By.XPATH, '//*[@id="header"]/div[1]/div[1]/div[1]/span[3]').click()
    time.sleep(2)

    login_ID = driver.find_element(By.XPATH, '//*[@id="client_id"]')
    login_ID.send_keys('wolfht93')

    login_PW = driver.find_element(By.XPATH, '//*[@id="passwd"]')
    login_PW.send_keys('07llawliet!')

    driver.find_element(By.XPATH, '//*[@id="loginUI"]/tbody/tr[5]/td/a').click()
    time.sleep(2)

    driver.find_element(By.XPATH, '//*[@id="header"]/div[1]/div[1]/div[1]/span[3]').click()
    time.sleep(1)

    driver.find_element(By.XPATH, '//*[@id="aside"]/div[1]/div/ul/li[3]/a').click()
    time.sleep(1)

    driver.find_element(By.XPATH, '//*[@id="bookmarkListContent01"]/div/div/div/div[1]/div[1]/a/strong').click()
    time.sleep(1)

    data_frame = pd.DataFrame([])

    for m in range(2, 3):
        for n in range(1, 3):
            try:
                driver.find_element(By.XPATH, f'//*[@id="Tr_{n}"]/td[3]/div[4]').click()
                time.sleep(1)

                driver.switch_to.window(driver.window_handles[1])
                time.sleep(1)

                html = driver.page_source
                soup = BeautifulSoup(html, "html.parser")
                text = soup.get_text(separator="\n", strip=True)

                try:
                    title = soup.find("span", class_="f20 bold_900").text
                except:
                    title = 'error'

                try:
                    target_th = soup.find("th", string="물건종류")
                    property_type = target_th.find_next_sibling("td").text
                except:
                    property_type = 'error'

                try:
                    address = driver.find_element(By.XPATH, '//*[@id="lyCnt_base"]/table/tbody/tr[1]/td/span[1]').text.strip().split()
                    address1, address2, address3 = address[:3]
                except:
                    address1 = address2 = address3 = 'error'

                try:
                    if isinstance(address, list):
                        address_text = " ".join(address)
                        floor = "반지하" if any(k in address_text for k in ["지하", "지층", "지하층"]) else next((s for s in address if "층" in s), 'error')
                    else:
                        floor = 'error'
                except:
                    floor = 'error'

                try:
                    approval = soup.find("span", string=lambda t: t and "사용승인일" in t).text.strip().split(':')[1].split('-')[0] + '년'
                except:
                    approval = 'error'

                try:
                    og_price = driver.find_element(By.XPATH, '//*[@id="lyCnt_base"]/table/tbody/tr[3]/td[3]/span').text.strip()
                    law_price = driver.find_element(By.XPATH, '//*[@id="lyCnt_base"]/table/tbody/tr[4]/td[3]/span').text.strip().split()[1]
                    percent = driver.find_element(By.XPATH, '//*[@id="lyCnt_base"]/table/tbody/tr[4]/td[3]/span').text.strip().split()[0].split('(')[1].split(')')[0]
                except:
                    og_price = law_price = percent = 'error'

                try:
                    keywords = ["사무소", "사무실", "의원", "한의원", "공인중개사", "소매점", "근생빌라", "현황 주거용", "현황 주택", "현황 도시형생활주택", "현황:다세대주택", "현황:도시형생활주택"]
                    special_type = "근생빌라" if any(k in text for k in keywords) else ""
                except:
                    special_type = 'error'

                new_row = pd.DataFrame([[title, property_type, address1, address2, address3, floor, approval, og_price, law_price, percent, special_type]],
                                       columns=['사건 번호', '종류', '도/시', '시/구', '구/동', '층', '사용승인', '감정가', '최저가', '퍼센트', '근생빌라'])
                data_frame = pd.concat([data_frame, new_row], axis=0)

                driver.close()
                driver.switch_to.window(driver.window_handles[0])
                time.sleep(1)

            except Exception as e:
                print(f"Error at page {m}, item {n}: {e}")

        try:
            driver.find_element(By.XPATH, f'//*[@id="loadPage_{m}"]').click()
            time.sleep(2)
        except:
            print(f"페이지 {m} 없음")
            break

    os.makedirs('data', exist_ok=True)
    data_frame.to_excel('data/dooin_result.xlsx', index=False)
    driver.quit()

if __name__ == '__main__':
    run_crawler()
