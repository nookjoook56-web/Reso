import requests
import cloudscraper

url = "https://www2.vavoo.to/live2/index"
scraper = cloudscraper.create_scraper()
response = scraper.get(url)

if response.status_code == 200:
    with open("playlist.m3u", "w") as f:
        f.write(response.text)
    print("Liste başarıyla 'playlist.m3u' olarak kaydedildi!")
else:
    print("Hata oluştu, kod:", response.status_code)
