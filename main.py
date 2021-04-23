import time
import datetime
import pickle
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup


if __name__ == '__main__':
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--user-data-dir=./data')
        options.add_argument('--download.default_directory=./images')
        driver = webdriver.Chrome(options=options)
        driver.get('https://web.whatsapp.com/')

        time.sleep(10)

        group = driver.find_element_by_xpath(
            '//span[@title=\'Lead Verifier\']')
        group.click()

        msg_list = []
        messages = driver.find_elements_by_css_selector(
            '.focusable-list-item'
        )
        for msg in messages:
            msg_list.append(msg.get_attribute('innerHTML'))

        soup = BeautifulSoup(msg_list[len(msg_list) - 1], 'lxml')
        image = soup.find_all('img')
        image = image[len(image) - 1].get('src')
        group = driver.find_element_by_xpath(
            '//span[@title=\'Lead Verifier\']'
        )

        # button = driver.find_element_by_xpath(
        #     '//img[@src=\'' + image + '\']'
        # )
        # print(button.get_attribute('innerHTML'))

        print(image)

        filename = image.split('/')[-1] + '.jpg'
        print(filename)

        caption = soup.find_all('span', class_='copyable-text')
        caption = caption[0].find(
            'span'
        ).get_text()
        print(caption)

        # driver.close()
    except Exception as e:
        print(e)
