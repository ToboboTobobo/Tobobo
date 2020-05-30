import calendar
import json
translator_a = googletrans.Translator()
#translator_b = translate.Translator(to_lang = "zh-tw")
url = "https://www.theapro.kr:441/eng/now/data.asp"
title, link, translate, date = [], [], [], []
data = {
    "page": 1,
    "mode": 10,
    "pagesize": 9,
    "s1": "title",
    "od": 0
}
response = requests.post(url, verify = False, data = data)
#response.encoding = "utf-8"
soup = BeautifulSoup(response.text, "lxml")
now = datetime.datetime.now()
yesterday = datetime.datetime.now() + datetime.timedelta(-1)
soup = json.loads(soup.text)
for i in soup:
    if i["regdate"] == f"{yesterday.year}-{(str(yesterday.month)).zfill(2)}-{(str(yesterday.day).zfill(2))}":
        title.append(i["title"])
        try:
            translate.append(translator_a.translate(i["title"], dest = "zh-tw").text)
        except:
            translate.append(translator_b.translate(i["title"]))
result = pd.DataFrame({"編號":"", "撰寫":"", "搜尋日期":f"{now.year}/{now.month}/{now.day}", "新聞日期":f"{yesterday.year}/{yesterday.month}/{yesterday.day}", "地區別":"", "國家":"", "主題類別":"", "發佈機構/來源":"The Apro", "標題翻譯":translate, "標題原文":title, "關鍵字":"", "負責人":"", "連結":"", "備註":""})
result
