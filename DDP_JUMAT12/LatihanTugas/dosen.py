from person import person

class Dosen(person):
    def __init__(self, name, gender, umur, gelar, jabatan):
        # Panggil konstruktor dari kelas induk (Person)
        super().__init__(name, gender, umur)
        self.gelar = gelar
        self.jabatan = jabatan
        self.gaji = 0  # Inisialisasi gaji

    def setGaji(self, uang):
        # Tambahkan jumlah uang ke atribut gaji
        self.gaji += uang

    def cetak(self):
        super().cetak()
        print("Gelar \t\t :", self.gelar,
              "\nJabatan \t :", self.jabatan,
              "\nGaji \t\t :", self.gaji,
              "\n---------------------------------")
        
