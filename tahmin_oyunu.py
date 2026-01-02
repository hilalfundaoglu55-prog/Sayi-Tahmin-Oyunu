import random

# Sayı Tahmin Oyunu
print("Sayı Tahmin Oyununa Hoş Geldiniz!")
print("1 ile 100 arasında bir sayı tuttum. Bakalım bilecek misiniz?")

hedef = random.randint(1, 100)
tahmin_hakki = 5

while tahmin_hakki > 0:
    print(f"\nKalan hakkınız: {tahmin_hakki}")
    tahmin = int(input("Tahmininiz nedir? "))

    if tahmin == hedef:
        print("Tebrikler! Doğru bildiniz! 🎉")
        break
    elif tahmin < hedef:
        print("Daha BÜYÜK bir sayı söyleyin.")
    else:
        print("Daha KÜÇÜK bir sayı söyleyin.")
    
    tahmin_hakki -= 1

if tahmin_hakki == 0:
    print(f"\nHakkınız bitti. Tuttuğum sayı: {hedef} idi. Bir dahaki sefere!")
