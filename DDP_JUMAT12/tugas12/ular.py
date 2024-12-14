from animal import Animal

class ular(Animal):
    def __init__(self, name,makanan,hidup,berkembang_biak,warna_sisik,berbisa):
      super().__init__(name,makanan,hidup,berkembang_biak),
      self.warna_sisik = warna_sisik
      self.berbisa =berbisa
      
    def info_ular(self):
      super().info_animal(),
      print("warna sisik \t\t : ",self.warna_sisik,
           "\nberbisa \t\t :",self.berbisa)
      
ular_kobra = ular("kobra","daging","darat","bertelur","belang belang","berbisa")
ular_kobra.info_ular()
print("===================================================")

ular_sanca = ular("sanca","tikus","darat","bertelur","hijau","tidak berbisa")
ular_sanca.info_ular()
print("===================================================")

ular_weling = ular("weling","kodok","darat","bertelur","hitam putih","berbisa")
ular_weling.info_ular()