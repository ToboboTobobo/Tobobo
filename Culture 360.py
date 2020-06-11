import calendar
translator_a = googletrans.Translator()
#translator_b = translate.Translator(to_lang = "zh-tw")
url = "https://culture360.asef.org/news-events/news/"
title, link, translate, date = [], [], [], []
response = requests.get(url)
response.encoding = "utf-8"
soup = BeautifulSoup(response.text, "lxml")
now = datetime.datetime.now()
yesterday = datetime.datetime.now() + datetime.timedelta(-1)
for i in soup.find_all(class_ = "date"):
    month = calendar.month_name[yesterday.month]
    if f"{yesterday.day} {month} {yesterday.year}" in i.text:
        date.append(f"{yesterday.year}/{yesterday.month}/{yesterday.day}")
        j = i.find_next("a")
        link.append("https://culture360.asef.org" + j["href"])
        k = j.find_next(class_ = "item-title")
        title.append(k.text)
        try:
            translate.append(translator_a.translate(k.text, dest = "zh-tw").text)
        except:
            translate.append(translator_b.translate(k.text))
result = pd.DataFrame({"編號":"", "撰寫":"", "搜尋日期":f"{now.year}/{now.month}/{now.day}", "新聞日期":date, "地區別":"", "國家":"", "主題類別":"", "發佈機構/來源":"Culture 360", "標題翻譯":translate, "標題原文":title, "關鍵字":"", "負責人":"", "連結":link, "備註":""})
result
