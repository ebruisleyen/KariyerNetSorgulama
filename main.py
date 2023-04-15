from bs4 import BeautifulSoup
import requests


url="https://www.kariyer.net/is-ilanlari/ankara-yazilim+test+uzmani?ct=6&pst=3087&pkw=Yazilim%20Test%20Uzmani"
baglan = requests.get(url).content
parser=BeautifulSoup(baglan,"html.parser")
kod=parser.find("div",{"class":"list-items-wrapper"}).find_all("div",{"class":"list-items"})
sayac=0
for i in kod:
  try:
    Job_Posting_Name =i.find("a",{"class":"k-ad-card"}).find("div",{"class":"card-top"}).find("div",{"class":"title-left"}).find("span",{"class":"k-ad-card-title multiline"}).text
    print("job posting name",Job_Posting_Name)
    city=i.find("div",{"class":"job-detail"}).next.strip()
    print("City",city)
    workplace=i.find("div",{"class":"job-detail"}).find("span",{"class":"dot"}).next.strip()
    print("Work Place",workplace)
    
    link = i.find("a",{"class":"k-ad-card"}).text
    link=i.next.attrs["href"]
    print("Link",link)
    
  # eger hata verirse, o veri cekmiyoruz ve devam ediyoruz.
  except AttributeError:
    continue
    

  
