from bs4 import BeautifulSoup as bs
import time as t

import requests

URL='https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
page=requests.get(URL)
s=bs(page.text,'html.parser')
st=s.find('table')
tl=[]
tr=st.find_all('tr')
for r in tr:
    td=r.find_all('td')
    a=[i.text.rstrip() for i in td]
    tl.append(r)
Star_names = []
Distance =[]
Mass = []
Radius =[]
Lum = []

for i in range(1,len(tl)):
    Star_names.append(tl[i][1])
    Distance.append(tl[i][3])
    Mass.append(tl[i][5])
    Radius.append(tl[i][6])
    Lum.append(tl[i][7])

df2 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius,Lum)),columns=['Star_name','Distance','Mass','Radius','Luminosity'])
print(df2)

df2.to_csv('bright_stars.csv')