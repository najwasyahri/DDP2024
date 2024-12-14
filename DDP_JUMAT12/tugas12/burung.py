#Buat class animal sebagai parent class. class animal mempunyai properti 4 properti (name, makanan, hidup, berkembang biak)
#buat minimal 3 class child (burung, ikan, ular, dll) setiap class child itu memiliki 2 properti dan method 
#buat minimal 2 objek untuk setiap class childnya.

from animal import Animal

class burung(Animal):
  def __init__(self, name, makanan, hidup, berkembang_biak, paruh, warna_bulu):
      super().__init__(name, makanan, hidup, berkembang_biak),
      self.paruh = paruh
      self.warna_bulu = warna_bulu
      
  def info_burung(self):
     super().info_animal(),
     print("paruh \t\t\t : ",self.paruh,
           "\nWarna Bulu \t\t :",self.warna_bulu)
     
burung_beo = burung("beo","jagung","darat","bertelur","melengkung","warna warni")
burung_beo.info_burung() 
print("================================================") 

burung_merpati = burung("merpati","beras","darat","bertelur","lurus","putih")
burung_merpati.info_burung()
print("================================================")

burung_kakatua = burung("kakatua","biji bijian","bertelur","melengkung","melengkung","kuning")
burung_kakatua.info_burung()
      