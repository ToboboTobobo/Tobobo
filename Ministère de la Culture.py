import calendar
translator_a = googletrans.Translator()
#translator_b = translate.Translator(to_lang = "zh-tw")
url = "https://www.culture.gouv.fr/Actualites"
title, link, translate = [], [], []
response = requests.get(url)
#response.encoding = "utf-8"
soup = BeautifulSoup(response.text, "lxml")
now = datetime.datetime.now()
yesterday = datetime.datetime.now() + datetime.timedelta(-1)
for i in soup.find_all("time"):
    if f"{(str(yesterday.day)).zfill(2)}.{(str(yesterday.month)).zfill(2)}.{yesterday.year}" in i.text:
        j = i.find_next("a")
        title.append(j.text.strip())
        link.append("https://www.culture.gouv.fr" + j["href"])
        try:
            translate.append(translator_a.translate(j.text.strip(), dest = "zh-tw").text)
        except:
            translate.append(translator_b.translate(j.text.strip()))
result = pd.DataFrame({"編號":"", "撰寫":"", "搜尋日期":f"{now.year}/{now.month}/{now.day}", "新聞日期":f"{yesterday.year}/{yesterday.month}/{yesterday.day}", "地區別":"", "國家":"", "主題類別":"", "發佈機構/來源":"Ministère de la Culture", "標題翻譯":translate, "標題原文":title, "關鍵字":"", "負責人":"", "連結":link, "備註":""})
result
