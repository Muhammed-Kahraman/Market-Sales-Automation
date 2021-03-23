import Fonksiyonlar
import sqlite3

veri_tabani = sqlite3.connect('Veri_Deposu.sqlite')
imlec = veri_tabani.cursor()
print("HOSGELDINIZ:\n")
while True:
    secim = input("Lutfen Bir Secenek Secin\n"
                  "1-Yeni Kategori Olusturma\n"
                  "2-Kategori Silme\n"
                  "3-Yeni Urun Girisi\n"
                  "4-Urun Silme\n"
                  "5-Urun Guncelleme\n"
                  "6-Urun Satisi\n"
                  "7-Kar Markaji Hesaplama:\n"
                  "8-Programdan Çıkıs\n")
    if secim == "1":
        Fonksiyonlar.tabloolusturma()

    if secim == "2":
        Fonksiyonlar.tablosilme()


    if secim == "3":
        Fonksiyonlar.degerekleme()


    if secim == "4":
        Fonksiyonlar.degersilme()


    if secim == "5":
        Fonksiyonlar.degerguncelleme()


    if secim == "6":
        Fonksiyonlar.UrunSatisi()


    if secim == "7":
        Fonksiyonlar.karhesaplama()

    if secim == "8":
        break

