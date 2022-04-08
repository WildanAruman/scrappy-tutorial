import  bs4
import requests

url = 'http://jadwalsholat.pkpu.or.id/?id=308'
contents = requests.get(url)

response = bs4.BeautifulSoup(contents.text, "html.parser")

data = response.find_all('tr', 'table_highlight')

sholat = {}
data = data[0]
i = 0
for d in data:
    if i == 1:
        sholat['Subuh'] = d.get_text()
    elif i == 2:
        sholat['Dhuhur'] = d.get_text()
    elif i == 3:
        sholat['Ashar'] = d.get_text()
    elif i == 4:
        sholat['Maghrib'] = d.get_text()
    elif i == 5:
        sholat['Isya'] = d.get_text()
    i += 1

print(sholat)
print(sholat['Subuh'])





