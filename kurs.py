import requests

print('Selamat datang')
print('Silakan pilih konversi yang akan Anda lakukan')
print('(1) IDR Indonesia => USD United States')
print('(2) USD United States => IDR Indonesia')
print('(3) USD United States => Bitcoin')
print('(4) Bitcoin => USD United States')
print('(5) Bitcoin => IDR Indonesia')
print('(6) IDR Indonesia => Bitcoin')
pilihan = input('Pilihan Anda (1/2/3/4/5/6): ')
nominal = int(input('Ketik nominal USD/RP/Bitcoin: '))

kode = (input('Ketik pilihan Bank: ')).lower()
url = f'https://kurs.web.id/api/v1/{kode}'
data = requests.get(url)

link = 'https://blockchain.info/ticker'
isi = requests.get(link)
bitcoin = isi.json()['USD']['sell']

if data.json()['error'] == 'false':
    hrg_jual = data.json()['jual']
    hrg_beli = data.json()['beli']

    waktu = data.json()['timestamp']
    
    hasil1 = nominal / int(hrg_jual)
    hasil2 = nominal * int(hrg_jual)
    hasil3 = (1/bitcoin) * nominal
    hasil4 = nominal * bitcoin
    hasil5 = hasil4 * int(hrg_jual)
    hasil6 = (1/bitcoin) * hasil1

    if pilihan == '1':
        print(f'Hasil konversi RP {nominal} adalah USD {round(hasil1, 2)}')
    elif pilihan == '2':
        print(f'Hasil konversi USD {nominal} adalah Rp {hasil2}')
    elif pilihan == '3':
        print(f'Hasil konversi USD {nominal} adalah {round(hasil3, 5)} bitcoin')
    elif pilihan == '4':
        print(f'Hasil konversi {nominal} bitcoin adalah USD {round(hasil4, 3)}')   
    elif pilihan == '5':
        print(f'Hasil konversi {nominal} bitcoin adalah Rp {round(hasil5, 3)}')
    elif pilihan == '6':
        print(f'Hasil konversi Rp {nominal} adalah {round(hasil6, 3)} bitcoin')     
    else:
        print('Anda salah ketik')

    print(f'\nSekedar informasi nilai tukar 1 USD pada {waktu} melalui Bank {(kode).upper()} yaitu:\n Rp {hrg_jual} (harga jual) atau Rp {hrg_beli} (harga beli)')
else:
    print('Maaf pilihan Bank tidak ada')
