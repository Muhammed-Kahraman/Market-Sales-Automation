import sqlite3

veri_tabani = sqlite3.connect('Veri_Deposu.sqlite')
imlec = veri_tabani.cursor()


def tabloolusturma():
    kategori_belirleme = input("Lutfen satis yapmak istediginiz urunlerin kategorisini girin.(1-adet)")
    imlec.execute(
        "CREATE TABLE IF NOT EXISTS '{}' (Urun_Adi,StokDurumu,Seri_Numarasi,Satis_Fiyat_Bilgisi,Alis_Fiyat_Bilgisi,Kar_Orani,Toplam_Gelir)".format(
            kategori_belirleme))
    veri_tabani.commit()


def tablosilme():
    kategori_belirleme_2 = input("Lutfen silmek istediginiz kategoriyi girin.(1-adet)")
    imlec.execute("DROP TABLE '{}' ".format(kategori_belirleme_2))
    veri_tabani.commit()


toplam_kar = 0


def degerekleme():
    global fiyat, Seri_Numarasi
    kar_orani = 0
    kategori_belirleme = input("Lutfen Urun Eklemek İstediginiz Kategoriyi Girin.(1-adet)")
    Urun_Adi = input("Lutfen eklemek istediginiz urunun adini giriniz:")
    StokDurumu = input("Lutfen eklemek istediginiz urunden kac adet oldugunu giriniz:")
    Seri_Numarasi = input("Lutfen eklemek istediginiz urunun barkod numarasini okutun ya da yazın:")
    Seri_Numarasi = int(Seri_Numarasi)
    Seri_numaralari = imlec.execute("SELECT Seri_Numarasi FROM '{}'".format(kategori_belirleme))
    for numara in Seri_numaralari:
        for num in numara:
            num = int(num)
            while (num == Seri_Numarasi):
                if num == Seri_Numarasi:
                    print("Hatalı Giris! Bu Barkod Numarasi Baska Bir Urune ait!")
                    Seri_Numarasi = input("Lutfen eklemek istediginiz urunun barkod numarasini okutun ya da yazın:")
                    Seri_Numarasi = int(Seri_Numarasi)
                if num != Seri_Numarasi:
                    break

    Alis_Fiyat_Bilgisi = input("Lutfen Eklemek Istediginiz Urunun Adet Fiyatını Kac ₺'den Satin Aldiginizi Giriniz::")
    Satis_Fiyat_Bilgisi = input("Lutfen Eklemek Istediginiz Urunun Adet Fiyatını Kac ₺'den Satıcagınızı Giriniz:")
    imlec.execute(
        "INSERT INTO '{}' VALUES ('{}','{}','{}','{}','{}','{}','{}')".format(kategori_belirleme, Urun_Adi, StokDurumu,
                                                                              Seri_Numarasi,
                                                                              Satis_Fiyat_Bilgisi,
                                                                              Alis_Fiyat_Bilgisi, kar_orani,
                                                                              toplam_kar))
    a_s_fiyatlari = imlec.execute("SELECT Alis_Fiyat_Bilgisi,Satis_Fiyat_Bilgisi FROM '{}'".format(kategori_belirleme))
    for fiyat in a_s_fiyatlari:
        fiyat = list(fiyat)
        fiyat[0] = int(fiyat[0])
        fiyat[1] = int(fiyat[1])
        kar_orani = fiyat[1] - fiyat[0]
    imlec.execute("UPDATE '{}' SET Kar_Orani = '{}' WHERE Seri_Numarasi = '{}'".format(kategori_belirleme, kar_orani,
                                                                                       Seri_Numarasi))
    veri_tabani.commit()


def degersilme():
    kategori_belirleme = input("Lutfen silmek istediginiz urunun kategorisini girin:")
    Seri_Numarasi = input("Lutfen silmek istediginiz urunun  barkod numarasini okutun ya da yazın(1-Adet):")
    imlec.execute("DELETE FROM '{}' WHERE '{}'".format(kategori_belirleme, Seri_Numarasi))
    print("Ürün Başarıyla Silindi...")
    veri_tabani.commit()


def degerguncelleme():
    kategori_belirleme = input("Lutfen guncelleme yapmak istediginiz kategoriyi giriniz:")
    baslik_belirleme = input("Lutfen guncelleme yapilacak basligi giriniz:")
    son_deger_belirleme = input("Lutfen yeni degeri giriniz:")
    degistirilen_urun = input("Lutfen islem yapmak istediginiz urunun barkod numaraisini okutnuz ya da giriniz:")
    imlec.execute("SELECT * FROM '{}'".format(kategori_belirleme))
    imlec.execute("UPDATE '{}' SET '{}' = '{}' WHERE Seri_Numarasi = '{}'".format(
        kategori_belirleme, baslik_belirleme, son_deger_belirleme, degistirilen_urun))
    veri_tabani.commit()


def UrunSatisi():
    global son_toplam, kar_orani, kar, toplam_kar, toplam_kar_2
    kategori_belirleme = input("Lutfen satis yaptiginiz urunun  kategorisini giriniz:")
    Seri_Numarasi = input("Lutfen satıs yapmak istediginiz urunun  barkod numarasini okutun ya da yazın(1-Adet):")
    SatisMiktari = input("Lutfen kac adet urun sattinizi giriniz:")
    son_toplam = 0
    imlec.execute("SELECT * FROM '{}' WHERE Seri_Numarasi = '{}'".format(kategori_belirleme, Seri_Numarasi))
    datalar = imlec.fetchone()
    int_data = int(datalar[1])
    print("Urun_Adi:'{}', Stok:'{}', Seri_Numarasi:'{}', Satıs_Fiyati:'{}', Alis_Fiyati:'{}'".format(datalar[0],
                                                                                                     datalar[1],
                                                                                                     datalar[2],
                                                                                                     datalar[3],
                                                                                                     datalar[4]))

    while True:
        SatisMiktari = int(SatisMiktari)
        son_toplam = int_data - SatisMiktari
        if son_toplam > 0:
            imlec.execute(
                "UPDATE '{}' SET StokDurumu = '{}' WHERE Seri_Numarasi = '{}'".format(kategori_belirleme, son_toplam,
                                                                                      Seri_Numarasi))
            break
        if son_toplam < 0:
            print("Hatalı Satis suan satıs yapabileceginiz maksimum adet sayisi '{}'".format(int_data))
            SatisMiktari = input("Lutfen kac adet urun sattinizi giriniz:")
            continue
    data_kar = imlec.execute(
        "SELECT Kar_Orani FROM '{}' WHERE  Seri_Numarasi = '{}'".format(kategori_belirleme, Seri_Numarasi))
    for karlar in data_kar:
        for kar in karlar:
            kar = int(kar)
        toplam_kar = kar * SatisMiktari
    toplam_gelir = imlec.execute(
        "SELECT Toplam_Gelir FROM '{}' WHERE  Seri_Numarasi = '{}'".format(kategori_belirleme, Seri_Numarasi))
    for gelirler in toplam_gelir:
        for gelir in gelirler:
            gelir = int(gelir)
            toplam_kar_2 = gelir + toplam_kar
            print(toplam_kar_2)
    imlec.execute(
        "UPDATE '{}' SET Toplam_Gelir = '{}' WHERE Seri_Numarasi = '{}'".format(kategori_belirleme, toplam_kar_2,
                                                                                Seri_Numarasi))
    veri_tabani.commit()


def karhesaplama():
    global gelir
    gelir_toplami = 0
    gelir_toplami_1 = 0
    kategori_belirleme = input("Lutfen gelirinin hesaplanmasını istediginiz kategoriyi giriniz:")
    toplam_gelir = imlec.execute("SELECT Toplam_Gelir FROM '{}'".format(kategori_belirleme))
    for gelirler_1 in toplam_gelir:
        for gelir_1 in gelirler_1:
            gelir_1 = int(gelir_1)
            gelir_toplami_1 = gelir_1 + gelir_toplami_1
    kategori_gelir_1 = 0
    kategori_gelir_1 = gelir_toplami_1 + kategori_gelir_1
    print("'{}' kategorisinin toplam geliri:".format(kategori_belirleme), kategori_gelir_1, "₺")
    imlec.execute("SELECT Toplam_Gelir FROM Temizlik")
    temizlik = imlec.fetchall()
    imlec.execute("SELECT Toplam_Gelir FROM Teknoloji")
    teknoloji = imlec.fetchall()
    imlec.execute("SELECT Toplam_Gelir FROM Oyuncaklar")
    oyuncklar = imlec.fetchall()
    imlec.execute("SELECT Toplam_Gelir FROM Gida")
    Gida = imlec.fetchall()
    Gelirler = []
    Gelirler.append(temizlik)
    Gelirler.append(teknoloji)
    Gelirler.append(Gida)
    Gelirler.append(oyuncklar)
    for gelirler in Gelirler:
        for gelir in gelirler:
            for gelircik in gelir:
                gelircik = int(gelircik)
                gelir_toplami = gelircik + gelir_toplami
    genel_gelir = 0
    genel_gelir = gelir_toplami + genel_gelir
    print("Tum Kategorilerdeki Toplam Kazanç:'{}'".format(genel_gelir), "₺")
    veri_tabani.commit()


def veritabaniclose():
    veri_tabani.commit()
    veri_tabani.close()


# degerekleme()
# degersilme()
# tabloolusturma()
# tablosilme()
# degerguncelleme()
# UrunSatisi()
# karhesaplama()
# veritabaniclose()
# veritabaniclose()
