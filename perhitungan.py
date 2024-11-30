import math

def tambah(bill1, bill2):
    hasil = bill1 + bill2
    print("hasil tambah dari",bill1,"+",bill2,"=",hasil)
    
def kurang(bill1, bill2):
    hasil = bill1 - bill2
    print("hasil kurang dari",bill1,"-",bill2,"=",hasil)   
    
def kali(bill1, bill2):
    hasil = bill1 * bill2
    print("hasil kali dari",bill1,"*",bill2,"=",hasil)  
    
def bagi(bill1, bill2):
    hasil = bill1 / bill2
    print("hasil bagi dari",bill1,"/",bill2,"=",hasil) 
    
def pangkat(bill1, bill2):
    hasil = math.pow (bill1,bill2)
    print("hasil pangkat dari",bill1,"^",bill2,"=",hasil)             