total = 0  #Menjumlah semua angka
for i in range(1, 5000):
    total += i
print(f"jumlah {total}")

numbers = [3, 6, 9, 10, 8, 23, 55, 2 ] #Menghitung pangkat
for x in numbers:
    kuadrat = x ** 2
    print(f"{x} pangkat dua adalah {kuadrat}")

def cari_bilangan_genap(daftar_angka): #Mencari bilangan genap
    bilangan_genap = []

    for x in daftar_angka:
        if x % 2 == 0:
            bilangan_genap.append(x)

    return bilangan_genap

daftar_angka = list(range(1, 300))
hasil = cari_bilangan_genap(daftar_angka)
print(hasil)
