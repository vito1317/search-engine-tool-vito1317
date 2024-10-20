from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException  # 導入 NoSuchElementException
from urllib.parse import urlencode
import requests
from bs4 import BeautifulSoup


def search(keyword, mode = None, config={}):
    if mode == 'request':
        query = {
            "q": keyword,
            "oq": keyword
        }
        url = "https://www.google.com.tw/search?%s&uule=w+CAIQICIaQXVzdGluLFRleGFzLFVuaXRlZCBTdGF0ZXM&hl=en&gl=us&sourceid=chrome&ie=UTF-8#ip=1" % urlencode(
            query)
        #print(url)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        #print(soup)
        articles = soup.find_all('div', class_="MjjYud")
        data_list = []
        for a in articles:
            data = {}
            data_count = 3
            title = a.find("h3", class_="LC20lb")
            if title and title.text:
                title = title.text
            else:
                title = "沒有標題"
                data_count -= 1
            data['title'] = title
            p = a.find("div", class_="VwiC3b")
            if p and p.span:
                p = p.span.text
            else:
                p = "N/A"
                data_count -= 1
            data['abstract'] = p
            date = a.find("a")
            if date:
                date = date.get('href')
            else:
                date = "N/A"
                data_count -= 1
            data['href'] = date
            if data_count == 3:
                data_list.append(data)
        result = data_list
    else:
        options = Options()
        # 初始化瀏覽器
        driver = webdriver.Chrome(options=options)
        driver.minimize_window()
        # 訪問網頁
        query = {
            "q": keyword,
            "oq": keyword
        }
        driver.get(
            "https://www.google.com.tw/search?%s&uule=w+CAIQICIaQXVzdGluLFRleGFzLFVuaXRlZCBTdGF0ZXM&hl=en&gl=us&sourceid=chrome&ie=UTF-8#ip=1" % urlencode(
                query))
        # 隱式等待 5秒 通過設定的時長等待頁面元素加載完成，再執行下面的代碼，如果超過設定時間還未加載完成，則繼續執行下面的代碼
        #driver.implicitly_wait(5)

        # 獲取 n0jPhd class 的元素
        top_elements = driver.find_elements(By.CLASS_NAME, 'WlydOe')
        result = []
        for e in top_elements:
            row = {}
            row["href"] = e.get_attribute("href")
            try:
                p = e.find_element(By.CLASS_NAME, "n0jPhd")
                row["title"] = p.get_attribute("textContent")
            except NoSuchElementException:
                continue
            row["abstract"] = "無摘要"
            result.append(row)

        # 獲取 MjjYud class 的元素
        search_elements = driver.find_element(By.ID, "search").find_elements(By.CLASS_NAME, 'MjjYud')
        for e in search_elements:
            row = {}
            try:
                p = e.find_element(By.CLASS_NAME, "VwiC3b")
                row["abstract"] = p.get_attribute("textContent")
            except NoSuchElementException:
                continue
            a = e.find_element(By.TAG_NAME, "a")
            row["href"] = a.get_attribute("href")
            row["title"] = a.find_element(By.TAG_NAME, "h3").get_attribute("textContent")
            result.append(row)

        driver.close()

    return result

