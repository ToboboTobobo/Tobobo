import calendar
translator_a = googletrans.Translator()
#translator_b = translate.Translator(to_lang = "zh-tw")
url = "https://eca.state.gov/media-center"
title, link, translate = [], [], []
response = requests.get(url)
#response.encoding = "utf-8"
soup = BeautifulSoup(response.text, "lxml")
now = datetime.datetime.now()
yesterday = datetime.datetime.now() + datetime.timedelta(-1)
for i in soup.find_all(typeof = "sioc:Item foaf:Document")[4:]:
    month = calendar.month_name[yesterday.month]
    if f"{month} {yesterday.day}, {yesterday.year}" in i.text:
        title.append(i.text.strip().strip(f"{month} {yesterday.day}, {yesterday.year}")[:-9])
        j = i.find_next("a")
        link.append("https://eca.state.gov" + j["href"])        
        try:
            translate.append(translator_a.translate(i.text.strip().strip(f"{month} {yesterday.day}, {yesterday.year}")[:-9], dest = "zh-tw").text)
        except:
            translate.append(translator_b.translate(i.text.strip().strip(f"{month} {yesterday.day}, {yesterday.year}")[:-9]))
result = pd.DataFrame({"編號":"", "撰寫":"", "搜尋日期":f"{now.year}/{now.month}/{now.day}", "新聞日期":f"{yesterday.year}/{yesterday.month}/{yesterday.day}", "地區別":"", "國家":"", "主題類別":"", "發佈機構/來源":"Bureau of Educational and Cultural Affairs", "標題翻譯":translate, "標題原文":title, "關鍵字":"", "負責人":"", "連結":link, "備註":""})
result
