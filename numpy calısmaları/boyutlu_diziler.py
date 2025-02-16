gıdalar= []
meyveler= ["muz", "elma" , "dut" , "nar"]
corbalar= ["Şehriye" , "Tarhana"]
icecekler= ["ayran" , "hoşaf" , "cola" , "fanta" , "su"]

print(meyveler)
print(meyveler[1]) #meyvelerin 1. indexini ekrana yazdırıyoruz.

print(gıdalar)
gıdalar.append(meyveler)  #meyveler listesini gıdalar listesine ekleyerek çok boyutlu dizi elde ediyoruz.
gıdalar.append(corbalar)  #corbalar listeisni gıdalar listesine eklemiş oluyoruz.
print(gıdalar)