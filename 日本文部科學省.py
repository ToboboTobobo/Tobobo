translator_a = googletrans.Translator()
#translator_b = translate.Translator(to_lang = "zh-tw")
url = "https://www.mext.go.jp/b_menu/houdou/index.htm"
title, link, translate, date = [], [], [], []
response = requests.get(url)
response.encoding = "utf-8"
soup = BeautifulSoup(response.text, "lxml")
now = datetime.datetime.now()
for i in soup.find(class_ = "dateList icon").find_all(class_ = "information-date"):
    if f"{now.month}月{now.day - 1}日" in i.text:
        date.append(f"{now.year}/{now.month}/{now.day - 1}")
        j = i.find_next(class_ = "area_doc")
        title.append(j.a.text)
        link.append("https://www.mext.go.jp" + j.a["href"])
        try:
            translate.append(translator_a.translate(j.a.text, dest = "zh-tw").text)
        except:
            translate.append(translator_b.translate(title_ + "/" + subtitle))
result = pd.DataFrame({"編號":"", "撰寫":"", "搜尋日期":f"{now.year}/{now.month}/{now.day}", "新聞日期":date, "地區別":"", "國家":"", "主題類別":"", "發佈機構/來源":"日本文部科學省", "標題翻譯":translate, "標題原文":title, "關鍵字":"", "負責人":"", "連結":link, "備註":""})
result
