import requests
import lxml
from bs4 import BeautifulSoup

url = 'https://www.gsmarena.com/apple_iphone_14-11861.php'  # Ganti dengan URL yang sesuai
response = requests.get(url)

# Periksa apakah halaman berhasil diambil
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Temukan div berdasarkan id
    div_element = soup.find('div', id='specs-list')  # Ganti 'nama_div' dengan id div yang ingin Anda ekstrak

    # Jika div ditemukan, ekstrak semua teks dari elemen-elemen table dan p di dalamnya
    if div_element:
        all_data = []

        # Cari elemen-elemen table dan p di dalam div
        tables = div_element.find_all('table')
        paragraphs = div_element.find_all('p')

        # Ekstrak teks dari elemen-elemen table
        for table in tables:
            table_text = table.get_text(strip=True)
            all_data.append(table_text)

        # Ekstrak teks dari elemen-elemen p
        for paragraph in paragraphs:
            paragraph_text = paragraph.get_text(strip=True)
            all_data.append(paragraph_text)

        # Cetak semua data yang berhasil diekstrak
        for data in all_data:
            print(data)

    else:
        print('Div tidak ditemukan.')
else:
    print('Gagal mengambil halaman web.')

# Simpan data dalam format TXT
with open('data.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)
