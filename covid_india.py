import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly
import chart_studio.plotly as py
import plotly.express as px
import plotly.graph_objects as go
import plotly.offline as pyo
url="https://www.worldometers.info/coronavirus/"
r=requests.get(url)
html=r.text
soup=BeautifulSoup(html,'html.parser')
print(soup.title.text)
live_data=soup.find_all('div',id='maincounter-wrap')
# for i in live_data:
#   print(i.text)
table_body=soup.find('tbody')
table_rows=table_body.find_all('tr')
countries=[]
total_cases=[]
new_cases=[]
total_deaths=[]
todays_deaths=[]
total_recoveries=[]
for tr in table_rows:
  td=tr.find_all('td')
  countries.append(td[0].text)
  total_cases.append(td[1].text)
  new_cases.append(td[2].text)
  total_deaths.append(td[3].text)
  todays_deaths.append(td[4].text)
  total_recoveries.append(td[5].text)
headers=['countries','total_cases','new_cases','total_deaths','todays_deaths','total_recoveries']
df=pd.DataFrame(list(zip(countries,total_cases,new_cases,total_deaths,todays_deaths,total_recoveries)),columns=headers)
print(df[10:25])


# df.replace(r'^\s*$', np.nan, regex=True, inplace=True)
df.replace(r'^\s*$', 0, regex=True, inplace=True)
df.replace('N/A', 0, regex=True, inplace=True)
print(df)
df['total_cases'] = df.total_cases.str.replace(',','')
df['new_cases'] = df.new_cases.str.replace(',','')
df['total_deaths'] = df.total_deaths.str.replace(',','')
df['todays_deaths'] = df.todays_deaths.str.replace(',','')
df['total_recoveries'] = df.total_recoveries.str.replace(',','')
df['total_cases'] = pd.to_numeric(df['total_cases'])
df['new_cases'] = pd.to_numeric(df['new_cases'])
df['total_deaths'] = pd.to_numeric(df['total_deaths'])
df['todays_deaths'] = pd.to_numeric(df['todays_deaths'])
df['total_recoveries'] = pd.to_numeric(df['total_recoveries'])
df[df["countries"].isin(['India','Indonesia','UK','UAE','Luxembourg'])].plot(kind='bar', x='countries', y=['total_cases', 'new_cases','total_deaths','todays_deaths','total_recoveries'])
plt.show()
