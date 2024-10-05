from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException  # 導入 NoSuchElementException
from urllib.parse import urlencode


def search(keyword, config={}):
    options = Options()
    # 初始化瀏覽器
    driver = webdriver.Chrome(options=options)
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



