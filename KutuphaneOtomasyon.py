import sqlite3

connection = sqlite3.connect("kullanici2.db")
cursor = connection.cursor()


class kitaplar():
    def add_kitap(self, kitap_turu, kitap_ismi, yazar):
        cursor.execute("INSERT INTO kitaplar (kitap_turu,kitap_ismi,yazar) VALUES(?,?,?)",
                       (kitap_turu, kitap_ismi, yazar))
        connection.commit()

    def delete_kitaplar(self, ID):
        cursor.execute("delete from kitaplar where ID=(?)", (ID,))
        connection.commit()

    def select_kitaplar(self):
        cursor.execute("SELECT * FROM kitaplar")
        data = cursor.fetchall()
        for i in data:
            print(i)

    def select_kitapismi(self, kitap_ismi):
        cursor.execute("SELECT * FROM kitaplar WHERE kitap_ismi = ?", (kitap_ismi,))
        secilen_kitap = cursor.fetchone()
        if secilen_kitap:
            return True
        else:
            return False


class kayit():
    def delete_kayit(self, kayit_id):
        cursor.execute("delete from kullanici where ID=(?)", (kayit_id,))
        connection.commit()

    def add_kayit(self, ad, soyad, telefon, email, sifre):
        cursor.execute("INSERT INTO kullanici (ad, soyad, tel, email, sifre) VALUES (?, ?, ?, ?, ?)",
                       (ad, soyad, telefon, email, sifre))
        connection.commit()

        # connection.close()

    def select_kayit(self):
        cursor.execute("SELECT * FROM kullanici")
        data = cursor.fetchall()
        for i in data:
            print(i)

    def kontrol_uyegirisi(self, ad, soyad, sifre):
        cursor.execute("SELECT * FROM kullanici WHERE ad = ? AND soyad = ? AND sifre = ?", (ad, soyad, sifre))
        kullanici = cursor.fetchone()
        if kullanici:
            print('Giriş yapıldı')
            return True
        else:
            print('Giriş bilgileriniz yanlış')
            return False


obj = kitaplar()
obj2 = kayit()

while True:
    print("Kütüphane Otomasyonu Ana Menü")
    secim = input("Üye girişi yapmak için 1e\nÜye değilseniz kayıt oluşturmak için 2ye\n"
                  "Misafir olarak devam etmek için 3e \nAdmin girişi yapmak için 4e basınız\nTamamen çıkış yapmak için 5e basınız")
    if secim == "1":
        ad = input("Adınızı giriniz:")
        soyad = input("Soyadınızı giriniz:")
        sifre = input("Şifrenizi giriniz:")
        if obj2.kontrol_uyegirisi(ad, soyad, sifre):
            while True:
                secim = input("Kütüphaneye rezervasyon yapmak için 1'e\nKitap bakmak için 2'ye\nKitap ödünç almak için 3'e\n Ana menüye dönmek için 4 e basınız:")
                if secim == "1":
                    print("Rezervasyonunuz yapıldı.")
                elif secim == "2":
                    obj.select_kitaplar()
                elif secim == "3":
                    obj.select_kitaplar()
                    kitap_ismi = input("Ödünç almak istediğiniz kitabın ismini giriniz:")
                    if obj.select_kitapismi(kitap_ismi):
                        print(kitap_ismi, "kitabı 15 gün süreyle ödünç verilmiştir.")
                    else:
                        print("Üzgünüz, böyle bir kitap bulunmamaktadır.")
                elif secim == "4":
                    break
                else:
                    print("Yanlış bir seçim yaptınız")

    elif secim == "2":
        ad = input("Lütfen ad giriniz:")
        soyad = input("Lütfen soyad giriniz:")
        telefon = input("Lütfen telefon numarası giriniz:")
        email = input("Lütfen email giriniz:")
        sifre = input("Lütfen şifreyi giriniz")
        obj2.add_kayit(ad, soyad, telefon, email, sifre)
        print('Kayıt eklendi')
        print("Değerli üyemiz aramıza hoşgeldiniz. Devam etmek için lütfen aşağıdaki işlemlerden birini seçiniz.")
        while True:
            secim = input(
                "Kütüphaneye rezervasyon yapmak için 1'e\nKitap bakmak için 2'ye\nKitap ödünç almak için 3'e\nAna menüye dönmek için 4 e basınız:")
            if secim == "1":
                print("Rezervasyonunuz yapıldı.")
            elif secim == "2":
                obj.select_kitaplar()
            elif secim == "3":
                obj.select_kitaplar()
                kitap_ismi = input("Ödünç almak istediğiniz kitabın ismini giriniz:")
                if obj.select_kitapismi(kitap_ismi):
                    print(kitap_ismi, "kitabı 15 gün süreyle ödünç verilmiştir.")
                else:
                    print("Üzgünüz, böyle bir kitap bulunmamaktadır.")
            elif secim == "4":
                break
            else:
                print("Yanlış bir seçim yaptınız")

    elif secim == "3":
        print("Kütüphanemize hoşgeldiniz. Misafir olarak sadece kütüphanemizde bulunan kitapların listesini görüntüleyebilmeniz mümkündür.\nKitap ödünç almak ve rezervasyon yaptırabilmek için üye olmanız gerekmektedir.")
        print("Kitapların listesi:")
        obj.select_kitaplar()
    elif secim == "4":
        while True:
            yonetici = input("yönetici ismi giriniz:")
            secim = input("şifreyi giriniz:")
            if yonetici == "admin" and secim == "12345":
                print("Giriş yapıldı")
                break
            else:
                print("Yanlış giriş yaptınız. Tekrar deneyiniz")

        while True:
            print("*******")
            secim = input(
                "kitap girişi yapmak için 1e\nkitap silmek için 2ye\nüye silmek için 3e basınız\nÇıkış yapmak için 4e basınız")
            if secim == "1":
                kitap_turu = input('Lütfen eklemek istediğiniz kitabın türünü giriniz :')
                kitap_ismi = input('Lütfen girmek istediğiniz kitabın adını giriniz:')
                yazar = input("Yazarın ismini giriniz:")
                obj.add_kitap(kitap_turu, kitap_ismi, yazar)
                print('Kayıt eklendi')
            elif secim == "2":
                obj.select_kitaplar()
                ID = input("silmek istediğiniz kitabın numarasını giriniz :")
                obj.delete_kitaplar(ID)
                print("Kitap silindi")
                obj.select_kitaplar()

            elif secim == "3":
                obj2.select_kayit()
                kayit_id = input("Silmek istediğiniz üyenin idsini giriniz:")
                obj2.delete_kayit(kayit_id)
                print("Kayıt silindi")
                obj2.select_kayit()
            elif secim == "4":
                break
            else:
                print("Yanlış bir seçim yaptınız")

    elif secim == "5":
        break

    else:
        print("Yanlış bir seçim yaptınız")
