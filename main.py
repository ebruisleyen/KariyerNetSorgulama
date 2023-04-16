from bs4 import BeautifulSoup
import requests
import json


url = "https://www.kariyer.net/is-ilanlari/ankara-yazilim+test+uzmani?ct=6&pst=3087&pkw=Yazilim%20Test%20Uzmani"
baglan = requests.get(url).content
parser = BeautifulSoup(baglan,"html.parser")
kod = parser.find("div",{"class":"list-items-wrapper"}).find_all("div",{"class":"list-items"})
veriler=[]
for i in kod:
  try:
    title = i.find("a",{"class":"k-ad-card"}).find("div",{"class":"card-top"}).find("div",{"class":"title-left"}).find("span",{"class":"k-ad-card-title multiline"}).text
    city = i.find("div",{"class":"job-detail"}).next.strip()
    workplace = i.find("div",{"class":"job-detail"}).find("span",{"class":"dot"}).next.strip()
    
    link = "kariyer.net" + i.next.attrs["href"]
  
    job_post = {"title": title,"city":city,"workplace":workplace,"link":link,"sms":False}
    veriler.append(job_post)
    
    
  # eger hata verirse, o veri cekmiyoruz ve devam ediyoruz.
  except AttributeError:
    continue

with open("data.json", "a",encoding="utf-8") as outfile:
    json.dump(veriler, outfile,indent=2,ensure_ascii=False)

infile =open("data.json","r")
data=infile.readlines()
print(data)
while True:
   for i in data:
      if i not in veriler:
         veriler.append(i)
      else:
         break
         
  
