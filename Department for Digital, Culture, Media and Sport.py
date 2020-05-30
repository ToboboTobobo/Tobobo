import calendar
translator_a = googletrans.Translator()
#translator_b = translate.Translator(to_lang = "zh-tw")
url = "https://www.gov.uk/search/all?organisations%5B%5D=department-for-digital-culture-media-sport&order=updated-newest&parent=department-for-digital-culture-media-sport"
title, link, translate = [], [], []
response = requests.get(url)
#response.encoding = "utf-8"
soup = BeautifulSoup(response.text, "lxml")
now = datetime.datetime.now()
yesterday = datetime.datetime.now() + datetime.timedelta(-1)
for i in soup.find_all("time"):
    month = calendar.month_name[yesterday.month]
    if f"{yesterday.day} {month} {yesterday.year}" in i.text:
        j = i.find_previous("a")
        title.append(j.text)
        link.append("https://www.gov.uk" + j["href"])
        try:
            translate.append(translator_a.translate(j.text, dest = "zh-tw").text)
        except:
            translate.append(translator_b.translate(j.text))
result = pd.DataFrame({"編號":"", "撰寫":"", "搜尋日期":f"{now.year}/{now.month}/{now.day}", "新聞日期":f"{yesterday.year}/{yesterday.month}/{yesterday.day}", "地區別":"", "國家":"", "主題類別":"", "發佈機構/來源":"Department for Digital, Culture, Media and Sport", "標題翻譯":translate, "標題原文":title, "關鍵字":"", "負責人":"", "連結":link, "備註":""})
result
