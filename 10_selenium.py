# 네이버 웹툰 댓글 크롤링
# https://comic.naver.com/webtoon/detail?titleId=702672&no=1&week=finish
import time
from selenium import webdriver
# python -m pip install bs4
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get('https://comic.naver.com/webtoon/detail?titleId=702672&no=1&week=finish')
soup = BeautifulSoup(driver.page_source)
comment_area = soup.find_all('span', {'class': 'u_cbox_contents'})
print('********** 베스트 댓글 **********')
for i in range(len(comment_area)):
    comment = comment_area[i].text.strip()
    print(comment)
    print('-'*30)

# /html/body/div[1]/div[5]/div/div/div[4]/div[1]/div[3]/div/div/div[4]/div[1]/div/ul/li[2]/a/span[2]

driver.find_element('xpath', '//*[@id="cbox_module_wai_u_cbox_sort_option_tab2"]/span[2]').click()
time.sleep(2)

soup = BeautifulSoup(driver.page_source)
comment_area = soup.findAll('span', {'class', 'u_cbox_contents'})

print('********** 전체 댓글 **********')
for i in range(len(comment_area)):
    comment = comment_area[i].text.strip()
    print(comment)
    print('-' * 30)
    
time.sleep(10)
