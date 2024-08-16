# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 22:17:16 2024

@author: oem
"""

def tas_kagit_makas_CAGLASILA_DOLGUN():
    print("Taş, Kağıt, Makas oyununa hoş geldiniz!")
    print("Oyun kuralları basit:")
    print("Taş, Kağıt ya da Makas seçeneklerinden birini seçin.")
    print("Taş Makas'ı yener, Makas Kağıt'ı yener, Kağıt Taş'ı yener.")
    print("İlk iki turu kazanan oyunu kazanır.")
    
import random

def tas_kagit_makas_CAGLASILA_DOLGUN():
    
    print("Taş, Kağıt, Makas oyununa hoş geldiniz!")
    print("Oyun kuralları basit:")
    print("Taş, Kağıt ya da Makas seçeneklerinden birini seçin.")
    print("Taş Makas'ı yener, Makas Kağıt'ı yener, Kağıt Taş'ı yener.")
    print("İlk iki turu kazanan oyunu kazanır.")
    
    
    secenekler = ["taş", "kağıt", "makas"]

   
    oyuncu_galibiyetleri = 0
    bilgisayar_galibiyetleri = 0
    oynanan_oyun_sayisi = 0

    while True:
       
        oyuncu_galibiyetleri = 0
        bilgisayar_galibiyetleri = 0
        oynanan_oyun_sayisi += 1

        print(f"\n{oynanan_oyun_sayisi}. oyuna başlıyoruz!")

        while oyuncu_galibiyetleri < 2 and bilgisayar_galibiyetleri < 2:
            oyuncu_secimi = input("Seçiminizi yapın (taş, kağıt, makas): ").lower()
            while oyuncu_secimi not in secenekler:
                oyuncu_secimi = input("Geçersiz seçim! Lütfen tekrar seçin (taş, kağıt, makas): ").lower()

            bilgisayar_secimi = random.choice(secenekler)
            print(f"Bilgisayarın seçimi: {bilgisayar_secimi}")

            if oyuncu_secimi == bilgisayar_secimi:
                print("Berabere!")
            elif (oyuncu_secimi == "taş" and bilgisayar_secimi == "makas") or \
                 (oyuncu_secimi == "kağıt" and bilgisayar_secimi == "taş") or \
                 (oyuncu_secimi == "makas" and bilgisayar_secimi == "kağıt"):
                print("Bu turu siz kazandınız!")
                oyuncu_galibiyetleri += 1
            else:
                print("Bu turu bilgisayar kazandı!")
                bilgisayar_galibiyetleri += 1

        if oyuncu_galibiyetleri == 2:
            print("Tebrikler! Oyunu kazandınız!")
        else:
            print("Bilgisayar oyunu kazandı!")

        devam = input("Başka bir oyun oynamak ister misiniz? (e/h): ").lower()
        if devam == 'h':
            print("Oyunu bitirdiniz. Tekrar görüşmek üzere!")
            break

