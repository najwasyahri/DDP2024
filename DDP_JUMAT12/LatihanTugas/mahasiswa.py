from person import person
class Mahasiswa(person):
 def __init__(self, nama, gender, umur, prodi, smester):
     super().__init__(nama,gender,umur)
     self.prodi = prodi
     self.smester = smester
     
 def cetak(self):
     super().cetak()
     print("prodi \t\t :",self.prodi,
           "\nsmester \t :",self.smester)   
    

