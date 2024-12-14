from animal import Animal

class ikan(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak,corak, bentuk_tubuh):
      super().__init__(name, makanan, hidup, berkembang_biak),
      self.corak = corak
      self.bentuk_tubuh = bentuk_tubuh
      
    def info_ikan(self):
      super().info_animal(),
      print("corak \t\t\t : ",self.corak,
           "\nbentuk tubuh \t\t :",self.bentuk_tubuh)
      
ikan_mujair = ikan("mujair","pelet","air tawar","bertelur","abu hitam","pipih")
ikan_mujair.info_ikan() 
print("================================================") 

ikan_paus = ikan("paus","ikan kecil","air laut","beranak","biru abu","besar")
ikan_paus.info_ikan()
print("=================================================")

ikan_lele = ikan("lele","pelet","air tawar","bertelur","coklat abu","lonjong")
ikan_lele.info_ikan()