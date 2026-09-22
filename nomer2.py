a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))
c = int(input("Masukkan angka ketiga: "))
if a > b and a > c:
    print("Angka pertama adalah yang terbesar:", a)
elif b > a and b > c:
    print("Angka kedua adalah yang terbesar:", b)
elif c > a and c > b:
    print("Angka ketiga adalah yang terbesar:", c)
else:
    print("Semua angka sama")