from bs4 import BeautifulSoup
import requests
import json

from twilio.rest import Client
with open("mycredentials.json")  as f:
  my_crendentials = json.load(f)
  
account_sid = my_crendentials["account_sid"]
auth_token = my_crendentials["auth_token"]
client = Client(account_sid, auth_token)

atilmis_isler=[]
try:
  with open("atilmis_is_ilanları.json",encoding="utf8") as file:
    veri = file.read().strip()
    if veri:
      atilmis_isler = json.loads(veri)
except (FileNotFoundError, json.JSONDecodeError):
  pass

url = "https://www.kariyer.net/is-ilanlari/ankara-yazilim+test+uzmani?ct=6&pst=3087&pkw=Yazilim%20Test%20Uzmani"
baglan = requests.get(url).content
parser = BeautifulSoup(baglan,"html.parser")
kod = parser.find("div",{"class":"list-items-wrapper"}).find_all("div",{"class":"list-items"})

yeni_is_ilanlari=[]

for i in kod:
  try:
    title = i.find("a",{"class":"k-ad-card"}).find("div",{"class":"card-top"}).find("div",{"class":"title-left"}).find("span",{"class":"k-ad-card-title multiline"}).text
    city = i.find("div",{"class":"job-detail"}).find("span").next.strip()
    workplace = i.find("div",{"class":"job-detail"}).find("span",{"class":"work-model"}).next.strip()    
    link = "kariyer.net" + i.next.attrs["href"]
  
    job_post = {"title": title, "city":city, "workplace":workplace, "link":link}

    yeni_is_ilanlari.append(job_post)

  except AttributeError:
    continue
#
count = 0
# ıs ılanları 
for yeni_is in yeni_is_ilanlari:
  
  link_var = False
  for atilmis_is in atilmis_isler:
     if yeni_is["link"]==atilmis_is["link"]:
       link_var = True
       break
  if link_var:
    print("daha önce bu iş ilanı göndreildi.")
    print(yeni_is["link"])
  else:
    count +=1
    # eger ıkı mesaj atılmıssa dursun
    if count > 2:
      break
    print("bu iş ilanı yeni. mesaj at")

    whatsapp_mesaj = yeni_is["title"]+"\n"+yeni_is["city"]+"\n"+yeni_is["workplace"]+"\n"+yeni_is["link"]
    print(whatsapp_mesaj)
    
    # whatapp?mesaj mesaj olarak gonderılıyor
    message = client.messages.create(
      from_='whatsapp:+14155238886',
      body=whatsapp_mesaj,
      to='whatsapp:'+my_crendentials["numara"]
    )

    atilmis_isler.append(yeni_is)

  
with open("atilmis_is_ilanları.json","w",encoding="utf-8") as outfile:
    json.dump(atilmis_isler, outfile,indent=2,ensure_ascii=False)

  

       
       






# with open("data.json", "w",encoding="utf-8") as outfile:
#     json.dump(veriler, outfile,indent=2,ensure_ascii=False)
    

# infile =open("data.json","r",encoding="utf-8")

# data=infile.readlines()



