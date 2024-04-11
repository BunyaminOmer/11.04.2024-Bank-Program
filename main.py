import random
import time


class Kullanici:
    def __init__(self, ad, soyad, kimlik_no, telefon, sifre):
        self.ad = ad
        self.soyad = soyad
        self.kimlik_no = kimlik_no
        self.telefon = telefon
        self.sifre = sifre
        self.bakiye = 0.0
        self.money_draw_limit = 50000.0
        self.money_send_limit = 50000.0

class UyelikSistemi:
    def __init__(self):
        self.kullanicilar = []
        
    def kullanici_olustur(self, ad, soyad, kimlik_no, telefon, sifre, sifre_tekrar):
        if len(kimlik_no) != 11 or not kimlik_no.isdigit():
            print("Geçersiz kimlik numarası. Kimlik numarası 11 haneli olmalıdır ve sadece rakamlardan oluşmalıdır.")
            return False
        
        if len(sifre) < 6:
            print("Şifre en az 6 karakter uzunluğunda olmalıdır.")
            return False
        
        if sifre != sifre_tekrar:
            print("Şifreler uyuşmuyor. Lütfen tekrar deneyin.")
            return False

        yeni_kullanici = Kullanici(ad, soyad, kimlik_no, telefon, sifre)
        self.kullanicilar.append(yeni_kullanici)
        print("Üye kaydı başarıyla oluşturuldu.")
        return True
    
    def giris(self, kimlik_no, sifre):
        for kullanici in self.kullanicilar:
            if kullanici.kimlik_no == kimlik_no and kullanici.sifre == sifre:
                print(f"Giriş başarılı. Hoş geldiniz, {kullanici.ad} {kullanici.soyad}!")
                return True
        print("Kimlik numarası veya şifre hatalı.")
        return False

uyelik_sistemi = UyelikSistemi()

while True:
    secim = input("Giriş yapmak için 'G/ Giriş/ Giriş Yap', üye olmak için 'Ü/ Üye/ Üye Ol' girin: ").title()
    if secim == 'G' or secim == "Giriş" or secim == "Giriş Yap":
        kimlik_no = input("Kimlik Numaranız: ").strip()
        sifre = input("Şifreniz: ")
        
        if uyelik_sistemi.giris(kimlik_no, sifre):
            break
    elif secim == 'Ü' or secim == "Üye" or secim == "Üye Ol":
        ad = input("Adınız: ").title()
        soyad = input("Soyadınız: ").title()
        kimlik_no = input("Kimlik Numaranız (11 haneli): ").strip()
        telefon = input("Telefon Numaranız: ")
        sifre = input("Şifre: ")
        sifre_tekrar = input("Şifre Tekrar: ")
        
        if uyelik_sistemi.kullanici_olustur(ad, soyad, kimlik_no, telefon, sifre, sifre_tekrar):
            devam = input("Başka bir işlem yapmak ister misiniz? (Evet için 'E', Hayır için 'H'): ").title()
            if devam != 'E':
                break
    else:
        print("Geçersiz seçim. Lütfen 'G/ Giriş/ Giriş Yap' veya 'Ü/ Üye/ Üye Ol' girin.")

class Main:
    def __init__(self, kullanici):
        self.kullanici = kullanici

    def kullanici_bilgilerim(self):
        print(f"""
        Adınız : {self.kullanici.ad}
        Soyadınız : {self.kullanici.soyad}
        T.C Kimlik Numaranız : *******{self.kullanici.kimlik_no[4]}
        Telefon Numaranız : {self.kullanici.telefon}
        """)

    def draw_money(self):
        miktar = float(input("Çekmek istediğiniz para miktarını yazın : "))

        if miktar > self.kullanici.bakiye or miktar > self.kullanici.money_draw_limit:
            print(f"""
                  
                  İşlem Başarısız. Çekilen miktar bakiyenizden fazla.
                  
                  Miktar : {miktar}
                  Bakiyeniz : {self.kullanici.bakiye}
                  Hesap Limitiniz : {self.kullanici.money_draw_limit}

                  """)
        
        elif self.kullanici.bakiye > miktar and self.kullanici.money_draw_limit > miktar:
            self.kullanici.bakiye -= miktar
            self.kullanici.money_send_limit -= miktar
            print("İşleminiz gerçekleşiyor lütfen bekleyin!")
            time.sleep(3)
            print(f"""
                  
                  Paranız çekildi
                  Çekilen Miktar : {miktar}
                  Kalan Bakiye : {self.kullanici.bakiye}
                  Hesap Limitiniz : {self.kullanici.money_draw_limit}

                  """)
            
        elif self.kullanici.bakiye == miktar and self.kullanici.money_send_limit == miktar:
            miktar -= self.kullanici.bakiye
            miktar -= self.kullanici.money_draw_limit
            print("İşleminiz gerçekleşiyor lütfen bekleyin!")
            time.sleep(3)
            print(f"""
                  
                  Paranız çekildi
                  Çekilen Miktar : {miktar}
                  Kalan Bakiye : {self.kullanici.bakiye}
                  Hesap Limitiniz : {self.kullanici.money_draw_limit}

                  """)

    def send_money(self):
        miktar2 = float(input("Kaç para göndermek istiyorsunuz : "))
        send_iban = input("Gönderilecek IBAN : ")

        if miktar2 > self.kullanici.bakiye or miktar2 > self.kullanici.money_send_limit:
            print(f"""

                  İşlem başarısız.

                  Gönderilen IBAN : {send_iban}
                  Gönderilen Miktar : {miktar2}
                  Bakiye : {self.kullanici.bakiye}
                  Hesap Limitiniz : {self.kullanici.money_send_limit}

                  """)

        else:
            print("İşlem gerçekleştiriliyor!")
            if miktar2 < self.kullanici.bakiye and miktar2 < self.kullanici.money_send_limit:
                self.kullanici.bakiye -= miktar2
                self.kullanici.money_send_limit -= miktar2
                time.sleep(3)
                print(f"""

                İşlem gerçekleşti. Gönderilen miktar : {miktar2} 
                Kalan Bakiye : {self.kullanici.bakiye}
                Para gönderme limitiniz : {self.kullanici.money_send_limit}


                """)
            elif miktar2 < self.kullanici.money_send_limit:
                print(f"İşlem Başarısız! Gönderme limitiniz yetersiz.")

    def invest_money(self):
        miktar3 = float(input("Kaç para yatıracaksınız : "))

        print("İşlem gerçekleştiriliyor lütfen bekleyin!")
        time.sleep(3)
        self.kullanici.bakiye += miktar3
        print(f"""

            İşlem gerçekleşti!
            Yatırılan miktar : {miktar3}
            Bakiye : {self.kullanici.bakiye}

            """)
        
    def account_limit(self):
        print(f"""
              
              Para Gönderme Limitiniz : {self.kullanici.money_send_limit}
              Para Çekme Limitiniz : {self.kullanici.money_draw_limit}
                
            """)
        
    def account_balance(self):
        print(f"Hesap Bakiyeniz : {self.kullanici.bakiye}")

    def campaigns(self):
        print(f"""

            Trendyol harcamalarında % 10 anında nakit kazan
              
            Eczane harcamalarında % 10 anında nakit kazan
              
            Ulaşım kartları harcamalarında anında % 10 anında nakit kazan
              
            Spotify üyelik harcamalarında 15 TL anında nakit kazan
              
            Playstation harcamanın % 10'u anında nakit kazan
              
            S Sport Plus harcamalarında % 20 anında nakit kazan
              
            App Store harcamalarında % 5 anında nakit kazan
              
            Gain harcamanda 30 TL anında nakit kazan
              
            Youtube Premium harcamanın 10 TL'sini anında nakit kazan
              
            Madame Coco harcamanın % 10'unu anında nakit kazan
              
            DeFacto harcamanın % 10'unu anında nakit kazan
              
            Netflix harcamanın 20TL'sini anında nakit kazan
            
            Play Store harcamanın % 5'ini anında nakit kazan

            """)

main = Main(uyelik_sistemi.kullanicilar[0])
while True:

    print("""

    Hesap Bilgilerim - (A)
    Para Çek - (B)
    Para Gönder - (C)
    Para Yatır - (D)
    Hesap Limitlerim - (E)
    Bakiyem - (F)
    Kampanyalar - (G)
    Çıkış (L)

    """)

    soru = str(input("Ne Yapmak İstersin? : ")).title()
    
    if soru == "Hesap Bilgilerim" or soru == "A":
        main.kullanici_bilgilerim()

    if soru == "Para Çek" or soru == "B":
        main.draw_money()

    if soru == "Para Gönder" or soru == "C":
        main.send_money()
    
    if soru == "Para Yatır" or soru == "D":
        main.invest_money()

    if soru == "Hesap Limitlerim" or soru == "E":
        main.account_limit()

    if soru == "Bakiyem" or soru == "F":
        main.account_balance()

    if soru == "Kampanyalar" or soru == "G":
        main.campaigns()

    if soru == "Çıkış" or soru == "L":
        break