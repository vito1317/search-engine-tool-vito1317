from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from urllib.parse import urlencode
import requests
from bs4 import BeautifulSoup



def search(keyword, mode = None, config={}):
    if mode == 'request':
        query = {
            "q": keyword,
            "oq": keyword
        }
        url = "https://search.yahoo.com/search?%s&ei=UTF-8&fr=fp-tts" % urlencode(query)
        print(url)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        #print(soup)
        articles = soup.find_all('div', class_="dd")
        data_list = []
        for a in articles:
            data = {}
            data_count = 3
            title = a.find("a")
            if title and title.text:
                title = title.get('aria-label')
            else:
                title = "沒有標題"
                data_count -= 1
            data['title'] = title
            p = a.find("p", class_="fc-dustygray")
            if p and p.text:
                p = p.text
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
        # # 设置使用无头浏览器
        #options.add_argument("--headless")
        # 初始化浏览器
        driver = webdriver.Chrome(options=options)
        driver.minimize_window()
        # 访问网页
        query = {"p": keyword}
        # print("https://www.bing.com/search?form=QBRE&%s&cc=US" % urlencode(query))
        # driver.get('https://baidu.com')
        # exit(0)
        driver.get("https://search.yahoo.com/search?%s&ei=UTF-8&fr=fp-tts" % urlencode(query))
        # 隐式等待 10s 通过设定的时长等待页面元素加载完成，再执行下面的代码，如果超过设定时间还未加载完成，则继续执行下面的代码
        driver.implicitly_wait(10)
        # 获取返回的结果集
        elements = driver.find_elements(By.CLASS_NAME, "algo")
        result = []
        for e in elements:
            row = {}
            # p = e.find_element(By.CLASS_NAME, "b_caption").find_element(By.TAG_NAME, "p")
            # # print("text:" + p.get_attribute("textContent"))
            # row["abstract"] = p.get_attribute("textContent")
            # a = e.find_element(By.TAG_NAME, "h2").find_element(By.TAG_NAME, "a")
            # # print("href:" + a.get_attribute("href"))
            # row["href"] = a.get_attribute("href")
            # # print("title:" + a.get_attribute("textContent"))
            # row["title"] = a.get_attribute("textContent")
            try:
                p = e.find_element(By.CLASS_NAME, "compText")
                row["abstract"] = p.get_attribute("textContent")
            except Exception as e:
                continue
            # print(e.find_element(By.CLASS_NAME, "b_caption").text)
            a = e.find_element(By.TAG_NAME, "h3").find_element(By.TAG_NAME, "a")
            row["href"] = a.get_attribute("href")
            row["title"] = a.get_attribute("aria-label")
            result.append(row)

        # 关闭浏览器
        driver.close()
    return result