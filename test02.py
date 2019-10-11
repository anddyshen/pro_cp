import requests
from lxml import etree
import matplotlib.pyplot as plt
from pandas import Series

url = "http://datachart.500.com/ssq/history/newinc/history.php?start=18081&end=19116"
response = requests.get(url)
response = response.text
selector = etree.HTML(response)
reds = []
blues = []
for i in selector.xpath('//tr[@class="t_tr1"]'):
    datetime = i.xpath('td/text()')[0]
    red = i.xpath('td/text()')[1:7]
    blue = i.xpath('td/text()')[7]
    for i in red:
        reds.append(i)
    blues.append(blue)

s_blues = Series(blues)
s_blues = s_blues.value_counts()
s_reds = Series(reds)
s_reds = s_reds.value_counts()
print(s_blues)
print(s_reds)

labels = s_blues.index.tolist()
sizes = s_blues.values.tolist()
rect = plt.bar(range(len(sizes)) , sizes , tick_label = labels)
plt.show()
