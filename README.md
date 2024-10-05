l# 項目說明
https://github.com/vito1317/search-engine-tool-vito1317

項目的 Python 版本。原项目使用 Node + Puppeteer，Python 版本使用 Selenium。

## 安裝
```bash
pip install search-engine-tool-vito1317
```
# 使用 
```python 
from search_engine_tool import bing
def test_bing():
    try: data = bing.search("台灣天氣") 
        for d in data: 
            print(d) 
    except Exception as e: 
        print(e) 
if __name__ == '__main__': 
    test_bing() 
```
# 返回格式 
```python 
[ 
    {
    "abstract": "Web目前天氣. PM2:04. 84° F. RealFeel® 93°. RealFeel Shade™ 89°. 空氣品質 不佳. 風 西南偏西 6英里/小时. 風速 6英里/小时. 陰 更多詳情.",
    "href": "https://www.accuweather.com/zh/cn/shenzhen/58194/weather-forecast/58194",
    "title": "台灣, 台北市, 台灣 三日天氣預報 | AccuWeather" 
}, 
... ]
``` 
# 支持搜尋引擎 
```
Bing Google (需要调用方自身能够访问) Yahoo 
```
# Todo 
 ``` 
 1 處理人機驗證
 2 支持翻頁參數
 3 wikipedia 支持
```
 # search-engine-tool-vito1317
