#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gelişmiş Mazeret Üreticisi
Bu program, geç kaldığınız için size tamamen bilimsel ve ikna edici mazeretler üretir.
Asla işe yaramaz ama denemeye değer.
"""

import random
import time

def mazeret_uret(olay="işe geç kalmak"):
    baslangic = [
        "Vallahi şey oldu,",
        "Yemin ederim,",
        "İnanmayacaksın ama,",
        "Bilimsel olarak kanıtlanmış bir durum:",
        "Kuantum fiziğine göre,"
    ]
    
    sebep = [
        "kedim kahve makinesinin üstüne oturdu ve zaman-uzay büküldü",
        "otobüs şoförü aniden felsefe yapmaya başladı ve varoluşsal kriz geçirdim",
        "alarm saati 'bugün uyanmaya değmez' diye karar verdi ve ben de ona hak verdim",
        "evdeki WiFi birden bilinç kazandı ve interneti bana vermedi",
        "kahvaltıda yediğim ekmek kuantum tüneliyle başka boyuta geçti",
        "komşu 'bugün çok yoğunum' dedi ve bu benim için yeterli bahaneydi"
    ]
    
    bitis = [
        "o yüzden gelemedim. Anlayışla karşılarsın değil mi?",
        "bu yüzden biraz geciktim. Ama kalbimle oradayım.",
        "dolayısıyla zamanı kaçırdım. Kusura bakma kanka.",
        "sonuç olarak buradayım (gecikmeli olarak)."
    ]
    
    # Gizli not: bazen sistemin kendisi bahanedir
    # (aslinda herkes biraz gecikir, ama bunu kimse kabul etmez)
    
    secilen = f"{random.choice(baslangic)} {random.choice(sebep)}, {random.choice(bitis)}"
    return secilen

def main():
    print("=== Gelişmiş Mazeret Üreticisi v1.0 ===")
    print("Geç kaldığınız olayı yazın (boş bırakırsanız varsayılan kullanılır):")
    olay = input().strip() or "işe geç kalmak"
    
    print("\nMazeret üretiliyor... lütfen bekleyin (bu da bir mazeret olabilir)")
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print("\n")
    
    print(mazeret_uret(olay))
    print("\nNot: Bu mazeret %87.3 oranında işe yarar. Kaynak: Benim hayal gücüm.")

if __name__ == "__main__":
    main()
