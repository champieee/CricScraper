import requests
import csv
import numpy

from bs4 import BeautifulSoup

url = 'https://stats.espncricinfo.com/ci/engine/stats/index.html?class=1;filter=advanced;orderby=rating;qualmin1=1000;qualval1=runs;size=100;template=results;type=batting'

html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
rows = soup.find_all('tr')

values = numpy.array(['Name', 'Total', 'Average'])
values2 = numpy.array(['Name', 'Total', 'Average'])
values3 = numpy.array(['Name', 'Total', 'Average'])


resultFile = open("Test.csv",'wb')
wr = csv.writer(resultFile)

print("Test: ")
for row in rows:
  cells = row.find_all('td')
  if len(cells) > 9:
    row = (cells[0].text + "," + (cells[5].text + "," + cells[7].text).replace(" ", ""))

    values = numpy.append(values, cells[0].text)
    values = numpy.append(values, cells[5].text.replace(" ", ""))
    values = numpy.append(values, cells[6].text.replace(" ", ""))

url = 'https://stats.espncricinfo.com/ci/engine/stats/index.html?class=2;filter=advanced;orderby=rating;qualmin1=1000;qualval1=runs;size=100;template=results;type=batting'

new = numpy.reshape(values, (-1, 3))
print(new)

b = new.tolist()

with open("Test.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(b)


html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
rows = soup.find_all('tr')

print()
print("ODI: ")
for row in rows:
  cells = row.find_all('td')
  if len(cells) > 9:
    if cells[0].text != 'D Elgar (SA)':
      row = (cells[0].text + "," + (cells[5].text + "," + cells[7].text).replace(" ", ""))
      values2 = numpy.append(values2, cells[0].text)
      values2 = numpy.append(values2, cells[5].text.replace(" ", ""))
      values2 = numpy.append(values2, cells[6].text.replace(" ", ""))

new1 = numpy.reshape(values2, (-1, 3))
print(new1)
b1 = new1.tolist()

with open("ODI.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(b1)

url = 'https://stats.espncricinfo.com/ci/engine/stats/index.html?class=3;filter=advanced;orderby=rating;qualmin1=1000;qualval1=runs;size=100;template=results;type=batting'

html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
rows = soup.find_all('tr')

print()
print("T20: ")
for row in rows:
  cells = row.find_all('td')
  if len(cells) > 9:
    row = (cells[0].text + "," + (cells[5].text + "," + cells[7].text).replace(" ", ""))

    values3 = numpy.append(values3, cells[0].text)
    values3 = numpy.append(values3, cells[5].text.replace(" ", ""))
    values3 = numpy.append(values3, cells[6].text.replace(" ", ""))

new2 = numpy.reshape(values3, (-1, 3))
print(new2)
b2 = new2.tolist()

with open("T20.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(b2)