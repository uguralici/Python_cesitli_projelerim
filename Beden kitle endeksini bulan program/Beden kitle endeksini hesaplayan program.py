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
