from bs4 import BeautifulSoup
import requests

aile_ann = requests.get('https://www.aile.gov.tr/duyurular').text
soup  = BeautifulSoup(aile_ann, 'lxml')
announcements = soup.find_all('div', class_ = 'announcement-col col-6')

dates = []
texts = []

for announcement in announcements:
    date_element = announcement.find('span', class_='year')
    date = date_element.text.strip() if date_element else "Date not avaible"

    text_element = announcement.find('span', class_='title')
    text = text_element.text.strip() if text_element else "Announcement not avaible"

    if "2024" in date:
       if "Personel Alım" in text:
         dates.append(date)
         texts.append(text)


with open('output.txt', 'a', encoding='utf-8') as f:
    if texts:
        for i in range(len(dates)):
            f.write(f"Date= {dates[i]}\n")
            f.write(f"Text= {texts[i]}\n")
            f.write("-\n")
    else:
        f.write("No announcement avaible at Aile\n")
        f.write("-")
print("Aile's output is printed...")

