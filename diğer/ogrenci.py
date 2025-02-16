class Ogrenci:
    Ad= "Atama yapılmamış"
    No= 0
print(Ogrenci)
print("------------------")
print(Ogrenci.Ad)

print("------------------")
ogrenci1=Ogrenci
ogrenci1.Ad="Ahmet"
print("Ogrenci1 adı:", ogrenci1.Ad)

print("-------------------")
ogrenci2= Ogrenci
ogrenci2.Ad= "Veli"
print("Ogrenci2 adı:", ogrenci2.Ad)


print("------------------")
print("Ogrenci1 adı:", ogrenci1.Ad)   #ikisini de ayrı ayrı tanımlamayıp aynı classın içerisinde işlem yaptığımız için ogrenci1=ogrenci 2 olur init kullanınca düzelir.

class Ogrenci():
    Ad= "Atama yapılmamış"
    No= 0
    def __init__(self,aa,bb):
        self.Ad= aa
        self.No= bb
ogrenci1= Ogrenci("Nurdan",3)
print(ogrenci1.Ad)

ogrenci2=Ogrenci("Tuğba", 4)
print(ogrenci2.Ad)
