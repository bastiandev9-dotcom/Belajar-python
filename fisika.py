import math


def main():
    print("=====Silahkan pilih=====")
    print("1. Gerak lurus beraturan")
    print("2. Gerak lurus berubah beraturan")
    print("3. Gerak melingkar beraturan")
    print("4. Gerak parabola ")
    print("5. Hukum newton")
    pilihan = int(input("Masukkan pilihan anda: "))
    
    if pilihan == 1:
        gerak_lurus_beraturan()
    elif pilihan == 2:
        gerak_lurus_berubah_beraturan()
    elif pilihan == 3:
        gerak_melingkar_beraturan()
    elif pilihan == 4:
        gerak_parabola()
    elif pilihan == 5:
        hukum_newton()
    else:
        print("ERROR: Harap masukkan angka antara 1 sampai 3")

def gerak_lurus_beraturan():
    print("=====Silahkan pilih=====")
    print("1. Mencari jarak")
    print("2. Mencari kecepatan")
    print("3. Mencari waktu")
    pilih = int(input("Masukkan pilihan anda: "))
    
    if pilih == 1:
        v = float(input("Masukkan kecepatan (m/s): "))
        t = float(input("Masukkan waktu (s): "))
        s = v * t
        print(f"Hasil jarak adalah {s} meter")
    elif pilih == 2:
        s = float(input("Masukkan jarak (m): "))
        t = float(input("Masukkan waktu (s): "))
        v = s / t
        print(f"Hasil kecepatan adalah {v} m/s")
    elif pilih == 3:
        s = float(input("Masukkan jarak (m): "))
        v = float(input("Masukkan kecepatan (m/s): "))
        t = s / v
        print(f"Hasil waktu adalah {t} detik")
    else:
        print("ERROR: Harap masukkan angka antara 1 sampai 3")

def gerak_lurus_berubah_beraturan():
    print("=====Silahkan pilih=====")
    print("1. Mencari jarak")
    print("2. Mencari kecepatan")
    print("3. Menghitung kecepatan-jarak")
    print("4. Gerak jatuh bebas")
    print("5. Gerak vertikal ke atas")
    print("6. Gerak vertikal ke bawah")
    pilih = int(input("Masukkan pilihan anda: "))
    
    if pilih == 1:
        v0 = float(input("Masukkan kecepatan awal (m/s): "))
        t = float(input("Masukkan waktu (s): "))
        a = float(input("Masukkan percepatan (m/s\u00b2): "))
        s = (v0 * t) + (0.5 * a * t**2)
        print(f"Hasil jarak adalah {s} meter")
    elif pilih == 2:
        v0 = float(input("Masukkan kecepatan awal (m/s): "))
        a = float(input("Masukkan percepatan (m/s\u00b2): "))
        t = float(input("Masukkan waktu (s): "))
        v = v0 + (a * t)
        print(f"Hasil kecepatan adalah {v} m/s")
    elif pilih == 3:
        print("Ini digunakan untuk menjelaskan hubungan jarak sudah ditempuh, kecepatan awal, kecepatan akhir, dan besar percepatan tanpa harus mengetahui waktu tempuh.")
        v0 = float(input("Masukkan kecepatan awal (m/s): "))
        a = float(input("Masukkan percepatan (m/s\u00b2): "))
        s = float(input("Masukkan jarak (m): "))
        v = (v0**2) + (2 * a * s)
        print(f"Hasil kecepatan-jarak adalah {v}")
    elif pilih == 4:
        print("Silahkan pilih")
        print("1. Menghitung jarak tempuh benda setelah waktu tertentu ")
        print("2. Menghitung kecepatan benda setelah waktu tertentu ")
        print("3. Menghitung kecepatan benda yang jatuh dari ketinggian awal 'h0' ")
        pilih = int(input("Masukkan pilihan anda: "))
        if pilih == 1:
            g = 9.8
            print("g = 9.8 m/s\u00b2")
            t = float(input("Masukkkan waktu (s): "))
            h = (g * t**2) / 2
            print(f"Hasil ketinggian atau jarak yang ditempuh setelah {t} detik adalah {h} meter")
        elif pilih == 2:
            g = 9.8
            print("g = 9.8 m/s\u00b2")
            t = float(input("Masukkan waktu (s): "))
            v = g * t
            print(f"Hasil kecepatan setelah {t} detik adalah {v} m/s")
        elif pilih == 3:
            g = 9.8
            print("g = 9.8 m/s\u00b2")
            h = float(input("Masukkan ketinggian (m): "))
            v = math.sqrt (2 * g * h)
            print(f"Hasil kecepatan benda yang jatuh dari ketinggian {h} adalah {v} (m/s)")
        else:
            print("ERROR: Harap masukkan angka antara 1 sampai 3")
    elif pilih == 5:
        print("Silahkan pilih")
        print("1. Menghitung kecepatan benda setelah waktu tertentu ")
        print("2. Menghitung posisi (ketinggian) benda setelah waktu tertentu ")
        print("3. Menghitung kecepatan akhir sebuah benda pada ketinggian tertentu ")
        print("4. Menghitung waktu mencapai titik tertinggi ")
        print("5. Menghitung ketinggian maksimum")
        pilih = int(input("Masukkan pilihan anda: "))
        if pilih == 1:
            g = 9.8
            print("g = 9.8 m/s\u00b2")
            v0 = float(input("Masukkan kecepatan awal (m/s): "))
            t = float(input("Masukkan waktu (s): "))
            v = v0 - (g * t)
            print(f"Hasil kecepatan benda setelah {t} detik adalah {v} m/s")
        elif pilih == 2:
            g = 9.8
            print("g = 9.8 m/s\u00b2")
            v0 = float(input("Masukkan kecepatan awal (m/s): "))
            t = float(input("Masukkan waktu (s): "))
            h = ((v0 * t) - ((g * t**2) / 2))
            print(f"Hasil posisi (ketinggian) benda setelah {t} detik adalah {h} meter")
        elif pilih == 3:
            g = 9.8
            print("g = 9.8 m/s\u00b2")
            v0 = float(input("Masukkan kecepatan awal (m/s): "))
            h = float(input("Masukkan ketinggian (m): "))
            v = math.sqrt ((v0**2) - (2 * g * h))
            print(f"Hasil keecepatan benda pada ketinggian {h} meter adalah {v} m/s")
        elif pilih == 4:
            g = 9.8
            print("g = 9.8 m/s\u00b2")
            v0 = float(input("Masukkan kecepatan awal (m/s): "))
            t_max = v0 / g 
            print(f"Hasil waktu untuk mencapai titik tertinggi adalah {t_max}")
        elif pilih == 5:
            g = 9.8
            print("g = 9.8 m/s\u00b2")
            v0 = float(input("Masukkan kecepatan awal (m/s): "))
            h_max = v0**2 / (2 * g)
            print(f"Hasil ketinggian maksimum adalah {h_max}")
        else:
            print("ERROR: Harap masukkan angka antara 1 sampai 5")
    elif pilih == 6:
        print("Silahkan pilih")
        print("1. Menghitung kecepatan benda setelah waktu tertentu ")
        print("2. Menghitung posisi (ketinggian) benda setelah waktu tertentu ")
        print("3. Menghitung kecepatan akhir sebuah benda pada ketinggian tertentu ")
        pilih = int(input("Masukkan pilihan anda: "))
        if pilih == 1:
            g = 9.8
            print("g = 9.8 m/s\u00b2")
            v0 = float(input("Masukkan kecepatan awal (m/s): "))
            t = float(input("Masukkan waktu (s): "))
            v = v0 + (g * t)
            print(f"Hasil kecepatan benda setelah {t} detik adalah {v} m/s")
        elif pilih == 2:
            g = 9.8
            print("g = 9.8 m/s\u00b2")
            v0 = float(input("Masukkan kecepatan awal (m/s): "))
            t = float(input("Masukkan waktu (s): "))
            h = ((v0 * t) + ((g * t**2) / 2))
            print(f"Hasil posisi (ketinggian) benda setelah {t} detik adalah {h} meter")
        elif pilih == 3:
            g = 9.8
            print("g = 9.8 m/s\u00b2")
            v0 = float(input("Masukkan kecepatan awal (m/s): "))
            h = float(input("Masukkan ketinggian (m): "))
            v = math.sqrt ((v0**2) + (2 * g * h))
            print(f"Hasil keecepatan benda pada ketinggian {h} meter adalah {v} m/s")
        else:
            print("ERROR: Harap masukkan angka antara 1 sampai 3")
    else:
        print("ERROR: Harap masukkan angka antara 1 sampai 6")

def gerak_melingkar_beraturan():
    print("=====Silahkan pilih=====")
    print("1. Mencari frekuensi")
    print("2. Mencari periode")
    print("3. Mencari kecepatan sudut")
    print("4. Mencari kecepatan linear")
    print("5. Mencari percepatan sentripetal")
    print("6. Mencari gaya sentripetal")
    pilih = int(input("Masukkan pilihan anda: "))
    if pilih == 1:
        T = float(input("Masukkan periode (s): "))
        f = 1 / T
        print(f"Hasil frekuensi adalah {f} Hz")
    elif pilih == 2:
        f = float(input("Masukkan frekuensi (Hz): "))
        T = 1 / f
        print(f"Hasil periode adalah {T} detik")
    elif pilih == 3:
        print("1. w =2\u03c0f ")
        print("2. w = 2\u03c0 / T")
        pilih = int(input("Rumus mana yang ingin anda gunakan: "))
        if pilih == 1:
            pi = 3.14
            f = float(input("Masukkan frekuensi (Hz): "))
            w = 2 * pi * f
            print(f"Hasil keceptan sudut adalah {w} rad/s")   
        elif pilih == 2:
            pi = 3.14
            T = float(input("Masukkan periode (s): "))
            w = (2 * pi) / T
            print(f"Hasil kecepatan sudut adalah {w} rad/s")
        else:
            print("ERROR: harap masukkan angka 1 atau 2")
    elif pilih == 4:
        w = float(input("Masukkan kecepatan sudut (rad/s): "))
        r = float(input("Masukkan  jari -jari (m): "))
        v = w * r
        print(f"Hasil kecepatan linear adalah {v}")
    elif pilih == 5:
        print("1. a_s = w\u00b2r")
        print("2. a_s = v\u00b2 / r")
        pilih = int(input("Rumus mana yang ingin anda gunakan: "))
        if pilih == 1:
            w = float(input("Masukkan kecepatan sudut (rad/s): "))
            r = float(input("Masukkan jari jari lintasan (m): "))
            a_s = w**2 * r
            print(f"Hasil kecepatan sentripetal adalah {a_s} (m/s\u00b2)")
        elif pilih == 2:
            v = float(input("Masukkan kecepatan linear (m/s): "))
            r = float((input("Masukkan jari jari lintasan (m): ")))
            a_s= v**2 / r
            print(f"hasil percepatan sentripetal adalah {a_s} (m/s\u00b2)")
        else:
            print("ERROR: harap masukkan 1 atau 2")
    elif pilih == 6:
        print("1. F_s = ma_s")
        print("2. F_s = mw\u00b2r")
        print("3. F_s = (mv\u00b2) / r")
        pilih = int(input("Rumus mana yang ingin anda gunakan: "))
        if pilih == 1:
            m = float(input("Masukkan massa benda (kg): "))
            a_s = float(input("Masukkan a_s (m/s\u00b2) :"))
            F_s = m * a_s
            print(f"Hasil gaya sentripetal adalah {F_s} (N)")
        elif pilih == 2:
            m = float(input("Masukkan massa benda (kg): "))
            w = float(input("Masukkan kecepatan sudut (rad/s): "))
            r = float(input("Masukkan jari jari lintasan (m): "))
            F_s = m * w**2 * r
            print(f"hasil gaya sentripetal adalah {F_s} (N)")
        elif pilih == 3:
            m = float(input("Masukkan massa benda (kg):"))
            v = float(input("Masukkan kecepatan linear (rad/s): "))
            r = float(input("Masukkan jari jari lintasan (m): "))
            F_s = (m * v**2) / r
            print(f"Hasil gaya sentripetal adalah {F_s} (N)")
        else:
            print("ERROR: harap masukkan nomor antara 1 sampai 3")
    else:
        print("ERROR: Harap masukkan angka antara 1 sampai 6")

def gerak_parabola():
    print("=====silahkan pilih=====")
    print("1. Mencari kecepatan horizontal")
    print("2. Mencari kecepatan vertikal")
    print("3. Mencari jarak maksimum")
    print("4. Mencari tinggi maksimum")
    print("5. Mencari waktu total")
    pilihan = int(input("Masukkan angka: "))
    if pilihan == 1:
        def kecepatan_horizontal(v0, sudut):
            rumus = v0 * math.cos(math.radians(sudut))
            return rumus
        v0 = float(input("Masukkan kecepatan awal: "))
        sudut = float(input("Masukkan sudut: "))
        hasil = kecepatan_horizontal(v0, sudut)
        print(f"Kecepatan horizontal adalah {hasil} m/s")
    elif pilihan == 2:
        def kecepatan_vertikal(v0, sudut):
            rumus = v0 * math.sin(math.radians(sudut))
            return rumus 
        v0 = float(input("Masukkan kecepatan awal: "))
        sudut = float(input("Masukkan sudut: "))
        hasil = kecepatan_vertikal(v0, sudut)
        print(f"Kecepatan vertikal adalah {hasil} m/s")
    elif pilihan == 3:
        def jarak_maksimum(v0, sudut, g):
            rumus = (v0**2 * math.sin(math.radians( 2 * sudut))) / g
            return rumus 
        g = 9.8
        v0 = float(input("Masukkan kecepatan awal: "))
        sudut = float(input("Masukkan sudut: "))
        hasil = jarak_maksimum(v0, sudut, g)
        print(f"Jarak maksimum adalah {hasil} meter")
    elif pilihan == 4:
        def tinggi_maksimum(v0, sudut, g):
            sin = math.sin(math.radians(sudut))
            rumus = ((v0**2) * (sin**2)) / (2*g)
            return rumus 
        g = 9.8
        v0 = float(input("Masukkan kecepatan awal: "))
        sudut = float(input("Masukkan sudut: "))
        hasil = tinggi_maksimum(v0, sudut, g)
        print(f"Tinggi maksimum adalah {hasil} meter")
    elif pilihan == 5:
        def waktu_total(v0, sudut, g):
            rumus = (2 * v0 * math.sin(math.radians(sudut))) / g
            return rumus
        g = 9.8
        v0 = float(input("Masukkan kecepatan awal: "))
        sudut = float(input("Masukkan sudut: "))
        hasil = waktu_total(v0, sudut, g)
        print(f"waktu total adalah {hasil} detik(s)")
    else:
        print("ERROR: harap masukkan pilihan antara 1 sampai 5")
        

def hukum_newton():
    print("Hukum newton II")
    def gaya(massa, percepatan):
        rumus = massa * percepatan
        return rumus
    massa =float(input("Masukkan massa benda(kg): "))
    percepatan =float(input("Masukkan percepatan(m/s): "))
    hasil = gaya(massa, percepatan)
    print(f"jadi besarnya gaya adalah {hasil} newton")




if __name__ == "__main__":
    main()
