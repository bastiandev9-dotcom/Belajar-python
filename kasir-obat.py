class Obat:
    def __init__(self, kode, nama, harga, stok, jenis_obat, produsen, kegunaan):
        self.kode = kode
        self.nama = nama
        self.__harga = harga
        self.__stok = stok
        self.jenis_obat = jenis_obat
        self.produsen = produsen
        self.kegunaan = kegunaan
    
    def get_harga(self):
        return self.__harga
    
    def get_stok(self):
        return self.__stok
    
    def set_harga(self, harga):
        if harga > 0:
            self.__harga = harga
            return True
        return False
    
    def set_stok(self, stok):
        if stok > 0:
            self.__stok = stok
            return True
        return False
    
    def kurangi_stok(self, jumlah):
        if jumlah >=1 and jumlah <= self.__stok:
            self.__stok -= jumlah
            return True
        return False



class Inventory():
    def __init__(self):
        self.Persediaan = [
            Obat("A01", "Paracetamol", 3000, 120, "Tablet", "Kalbe Farma", "Meredakan demam dan nyeri"),
            Obat("A02", "Amoxicillin", 8000, 85, "Kapsul", "Sanbe Farma", "Mengobati infeksi bakteri"),
            Obat("A03", "Ibuprofen", 5500, 150, "Tablet", "Dexa Medica", "Mengurangi nyeri dan inflamasi"),
            Obat("A04", "Antimo", 1500, 90, "Tablet", "Pharos Indonesia", "Mencegah mual dan pusing"),
            Obat("A05", "Betadine", 10000, 65, "Cairan Antiseptik", "Mahakam Beta Farma", "Antiseptik untuk luka"),
            Obat("A06", "Bodrex Migra", 4000, 110, "Tablet", "Tempo Scan Pacific", "Meredakan migrain"),
            Obat("A07", "Promag", 2500, 180, "Tablet", "Kalbe Farma", "Meredakan gejala maag"),
            Obat("A08", "Diapet", 2000, 95, "Tablet", "Kimia Farma", "Mengobati diare"),
            Obat("A09", "Vitamin C-1000mg", 10000, 70, "Tablet Effervescent", "Holisticare", "Meningkatkan imun"),
            Obat("A10", "Minyak Kayu Putih", 20000, 45, "Minyak", "Cap Lang", "Meredakan nyeri otot"),
        ]



    def TampilkanListObat(self):
        for barang in self.Persediaan:
            print(f"Kode: {barang.kode} || Nama obat: {barang.nama} || Harga: {barang.get_harga()} || Stok: {barang.get_stok()} || Jenis obat: {barang.jenis_obat} || Produsen: {barang.produsen} || Kegunaan: {barang.kegunaan}")


    def TambahPersediaan(self):
        Kode = input("Masukkan kode obat: ")
        Nama = input("Masukkan nama obat: ")
        Harga = float(input("Masukkan harga obat: "))
        Stok = int(input("Masukkan stok obat: "))
        Jenis = input("Masukkan jenis obat: ")
        Produsen = input("Masukkan produsen obat: ")
        Manfaat = input("Masukkan manfaat obat: ")
        if (Harga >=1) and (Stok >=1):
            tambah_obat = Obat(Kode, Nama, Harga, Stok, Jenis, Produsen, Manfaat)
            self.Persediaan.append(tambah_obat)
            print(f"Obat dengan kode {Kode} berhasil ditambahkan")
        else:
            print("Gagal menambahkan obat, Harga/Stok tidak boleh lebih kecil dari 0")



    def HapusPersediaan(self):
        Kode = input("Masukkan kode yang ingin dihapus: ")
        for barang in self.Persediaan:
            if barang.kode == Kode:
                self.Persediaan.remove(barang)
                print(f"Obat dengan kode {Kode} berhasil dihapus")
                return
        print(f"Obat dengan kode {Kode} tidak ditemukan")


    def GantiHarga(self):
        Kode = input("Masukkan kode obat untuk mengganti harga: ")
        for barang in self.Persediaan:
            if barang.kode == Kode:
                question = input(f"Ganti harga obat {barang.nama}, (y/n): ").lower()
                if question == "y":
                    print(f"Harga saat ini, {barang.nama} [Rp.{barang.get_harga()}]")
                    newharga = float(input("Masukkan harga baru: "))
                    if newharga <= 0:
                        print("Gagal mengganti harga, harga harus positif")
                        return
                    else:
                        barang.set_harga(newharga)
                        print("Harga berhasil diganti")
                        return newharga
        print(f"Obat dengan kode {Kode} tidak ditemukan")


    def GantiStok(self):
        Kode = input("Masukkan kode obat untuk mengganti stok: ")
        for barang in self.Persediaan:
            if barang.kode == Kode:
                question = input(f"Ganti stok obat {barang.nama}, (y/n): ").lower()
                if question == "y":
                    print(f"Stok saat ini, {barang.nama} [stok: {barang.get_stok()}]")
                    newstok = int(input("Masukkan stok baru: "))
                    if newstok <= 0:
                        print("Gagal mengganti harga, harga harus positif")
                        return
                    else:
                        barang.set_stok(newstok)
                        print("Stok berhasil diganti")
                        return newstok
        print(f"Obat dengan kode {Kode} tidak ditemukan")


class Pembelian(Inventory): #pewarisan dari kelas inventory
    def Beli(self):
        print()
        Nama = input("Masukkan nama anda: ")
        kode = input("Masukkan kode obat yang ingin dibeli: ")
        for barang in self.Persediaan:
            if barang.kode == kode:
                print()
                print(f"Obat ditemukan!!!\nKode: {barang.kode}\nNama obat: {barang.nama}\nHarga: {barang.get_harga()}\nStok: {barang.get_stok()}\nJenis obat: {barang.jenis_obat}\nProdusen: {barang.produsen}\nKegunaan: {barang.kegunaan}")
                jumlah = int(input("Masukkan jumlah yang ingin dibeli: "))
                if (jumlah >=1) and (jumlah <= barang.get_stok()):
                    barang.kurangi_stok(jumlah)
                    hitung = barang.get_harga() * jumlah
                    print()
                    print("Struk Pembelian")
                    print(f"Nama: {Nama}\nKode Obat: {barang.kode}\nNama Obat: {barang.nama}\nJumlah: {jumlah}\nHarga: {hitung}")
                    return
                elif jumlah > barang.get_stok():
                    print(f"Jumlah melebihi stok saat ini")
                    return
                else:
                    print("Input tidak valid!!")
                    return
        print(f"Obat dengan kode {kode} tidak ditemukan")


if __name__ == "__main__":
    pembelian = Pembelian()
    while True:
        
        print("\n=== Sistem Pengelolaan obat untuk apoteker ===")
        print("1. Tampilkan Daftar Obat")
        print("2. Tambah Obat")
        print("3. Hapus Obat")
        print("4. Ganti Harga Obat")
        print("5. Ganti Stok Obat")
        print("6. Beli Obat")
        print("7. Keluar")

        pilih = int(input("Masukkan pilihan anda: "))
        if pilih == 1:
            pembelian.TampilkanListObat()
        elif pilih == 2:
            pembelian.TambahPersediaan()
        elif pilih == 3:
            pembelian.HapusPersediaan()
        elif pilih == 4:
            pembelian.GantiHarga()
        elif pilih == 5:
            pembelian.GantiStok()
        elif pilih == 6:
            pembelian.Beli()
        elif pilih == 7:
            break