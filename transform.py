import json

def convert():
    try:
        with open('playlist.m3u', 'r') as f:
            data = json.load(f)
        
        with open('playlist.m3u', 'w') as f:
            f.write("#EXTM3U\n")
            for item in data:
                group = item.get('group', 'Genel')
                name = item.get('name', 'Kanal')
                logo = item.get('logo', '')
                url = item.get('url', '')
                if url:
                    f.write(f'#EXTINF:-1 tvg-logo="{logo}" group-title="{group}",{name}\n{url}\n')
        print("Dönüştürme başarılı: JSON -> M3U")
    except Exception as e:
        print(f"Hata: {e}")

if __name__ == "__main__":
    convert()
