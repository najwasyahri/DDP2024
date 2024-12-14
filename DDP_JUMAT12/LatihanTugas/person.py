class person:
        def __init__(self, name, gender, umur):
                self.name = name
                self.gender = gender
                self.umur = umur
        def cetak(self):
                print("name \t\t :",self.name,
                      "\njenis Kelamin  \t :",self.gender,
                      "\nUmur \t\t :",self.umur)