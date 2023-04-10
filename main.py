from bs4 import BeautifulSoup
import requests


url="https://www.kariyer.net/is-ilanlari/ankara-yazilim+test+uzmani?ct=6&pst=3087&pkw=Yazilim%20Test%20Uzmani"
baglan = requests.get(url).content
parser=BeautifulSoup(baglan,"html.parser")
kod=parser.find("div",{"class":"list-items-wrapper"}).find_all("div",{"class":"list-items"})

for i in kod:
  Job_Posting_Name =i.find("a",{"class":"k-ad-card"}).find("div",{"class":"card-top"}).find("div",{"class":"title-left"}).find_all("span",{"class":"k-ad-card-title multiline"}).string
for i in kod:
  Job_Advertisement=i.find("div",{"class":"title-wrapper"}).find("div",{"class":"title-icon"}).find("div",{"class":"subtitle"})
  
  print(Job_Posting_Name)