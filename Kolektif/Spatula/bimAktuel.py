import requests
from bs4 import BeautifulSoup
import json

def aktuelBim():
    url = f"https://www.bim.com.tr/default.aspx"
    kimlik = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

    istek = requests.get(url, kimlik, allow_redirects=True)
    corba = BeautifulSoup(istek.text, "lxml")

    sozluk = {}

    tarih = corba.find('a', class_='active subButton').text.strip()
    urun_alani = corba.find('div', class_='productArea')

    urun_rerero = []
    for urun in urun_alani.findAll('div', class_='inner'):
        host = 'https://www.bim.com.tr'
        try:
            urun_basligi = urun.find('h2', class_='title').text.strip()
            urun_linki = host + urun.a['href']
            urun_gorseli = host + urun.img['src'].replace(' ', '%20')
            urun_fiyati = urun.find('a', class_='gButton triangle').text.strip()

            urun_rerero.append({
                "urun_baslik": urun_basligi,
                "urun_link" : urun_linki,
                "urun_gorsel" : urun_gorseli,
                "urun_fiyat" : urun_fiyati
            })
        except:
            pass
    

    sozluk.update({
        'tarih' : tarih
    })
    sozluk.update({
        'urunler' : urun_rerero
    })


    return sozluk

# print(aktuelBim())

jsonGorsel = json.dumps(aktuelBim(), indent=2, sort_keys=True, ensure_ascii=False)
# print(jsonGorsel)

basliklar = [anahtar for anahtar in aktuelBim()['urunler'][0].keys()]
# print(basliklar)