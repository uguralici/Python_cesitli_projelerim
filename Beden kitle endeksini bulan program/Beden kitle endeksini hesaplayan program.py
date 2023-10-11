#Beden kitle endeksini hesaplayan program.
while True:
 print(" ")
 print("Beden kitle endeksini hesaplayan programa hoşgeldiniz, lütfen kilo ve boy değerlerini giriniz.")
 print(" ")
 kilo=float(input("Kilo değeri: "))
 boy=float(input("Boy değeri (metre cinsinden): "))
 bedenkitleendeksi= kilo / (boy ** 2)
 print(" ")
 print("{}" "{:.2f}".format("Beden kitle endeksi: ", bedenkitleendeksi))
  if bedenkitleendeksi >= 40:
    print("morbid obez")
 elif 39.9> bedenkitleendeksi >= 30 :
    print("obez")
 elif 29.9> bedenkitleendeksi >=25:
    print("İdeal Kilonun Üstü")
    
 elif 24.9 > bedenkitleendeksi >= 18.5 :
    print("İdeal Kilo ")
    
 elif 18.5 > bedenkitleendeksi :
    print("İdeal Kilonun Altı ")
