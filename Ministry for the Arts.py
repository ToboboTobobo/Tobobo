import calendar
translator_a = googletrans.Translator()
#translator_b = translate.Translator(to_lang = "zh-tw")
url = "https://www.communications.gov.au/departmental-news"
title, link, translate, date = [], [], [], []
response = requests.get(url)
response.encoding = "utf-8"
soup = BeautifulSoup(response.text, "lxml")
now = datetime.datetime.now()
yesterday = datetime.datetime.now() + datetime.timedelta(-1)
for i in soup.find_all(class_ = "date-display-single"):
    month = calendar.month_name[yesterday.month]
    if f"{yesterday.day} {month} {yesterday.year}" in i.text:
        date.append(f"{yesterday.year}/{yesterday.month}/{yesterday.day}")
        j = i.find_next(class_ = "news-list__title")
        title.append(j.a.text.strip())
        link.append("https://www.communications.gov.au" + j.a["href"])
        try:
            translate.append(translator_a.translate(j.a.text, dest = "zh-tw").text)
        except:
            translate.append(translator_b.translate(title_ + "/" + subtitle))
result = pd.DataFrame({"編號":"", "撰寫":"", "搜尋日期":f"{now.year}/{now.month}/{now.day}", "新聞日期":date, "地區別":"", "國家":"", "主題類別":"", "發佈機構/來源":"Ministry for the Arts", "標題翻譯":translate, "標題原文":title, "關鍵字":"", "負責人":"", "連結":link, "備註":""})
result
