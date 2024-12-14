from dosen import Dosen

d1 = Dosen('Reza Maulana', 'Pria', 25, 'S.SI, M.Kom', 'LPPM')
d2 = Dosen('Siti Nurhaliza', 'Wanita', 30, 'S.Si, M.Si', 'LTSI')

d1.setGaji(19000000)
d2.setGaji(20000000)

print("Data Dosen 1:")
d1.cetak()

print("Data Dosen 2:")
d2.cetak()    

from mahasiswa import Mahasiswa

m1 = Mahasiswa('Najwa Putri', 'Wanita', 19, 'Sistem Informasi', 1)
m2 = Mahasiswa('Mahbub', 'Pria', 20, 'Teknik Informatika', 3)

print("Data Mahasiswa 1:")
m1.cetak()
print("\nData Mahasiswa 2:")
m2.cetak()

