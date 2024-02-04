from bs4 import BeautifulSoup
import requests

saglık_ann = requests.get('https://www.saglik.gov.tr/TR-99316/personel-duyurulari.html').text
soup  = BeautifulSoup(saglık_ann, 'lxml')
announcements = soup.find_all('tr')

dates = []
texts = []
    
for announcement in announcements:
    date_element = announcement.find('span', class_='date_03')
    date = date_element.text.strip() if date_element else "Date not avaible"

    text_element = announcement.find('a', class_='bakanlik_haber_link')
    text = text_element.text.strip() if text_element else "Announcement not avaible"

    if "2024" in date:
       if "Personel Alım" in text:
         dates.append(date)
         texts.append(text)
with open('output.txt', 'w', encoding='utf-8') as f:
    if texts:
        for i in range(len(dates)):
            f.write(f"Date= {dates[i]}\n")
            f.write(f"Text= {texts[i]}\n")
            f.write("-\n")
    else:
        f.write("No announcement avaible at Saglık\n")
        f.write("-\n")
print("Saglık's output is printed...")

