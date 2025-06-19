# 야놀자 리뷰 크롤링
import time
from selenium import webdriver
from bs4 import BeautifulSoup

def crawl_yanolja_reviews(name, url):
    review_list = []
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(2)

    scroll_count = 3
    for i in range(scroll_count):
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        time.sleep(2)

    html = driver.page_source
    soup = BeautifulSoup(html)

    review_containers = soup.select('#__next > section > div > div.css-1js0bc8 > div > div > div')
    review_date = soup.select('#__next > section > div > div.css-1js0bc8 > div > div > div > div.css-1toaz2b > div > div.css-1ivchjf > p')

    for i in range(len(review_containers)):
        review_text = review_containers[i].find('p', class_='content-text').text
        date = review_date[i].text
        review_empty_stars = review_containers[i].find_all('path', {'fill-rule':'evenodd'})
        stars = 5 - len(review_empty_stars)

        review_dict = {
            'review':review_text,
            'star':stars,
            'date':date
        }
        review_list.append(review_dict)
    print(review_list)

crawl_yanolja_reviews('신라스테이 여수', 'https://www.yanolja.com/reviews/domestic/10046614')