# import matplotlib.pyplot as plt
# plt.plot(["1.Sınav","2.Sınav","3.Sınav"], [80,70,90]) #çizgi grafiği
# plt.show() 

# import matplotlib.pyplot as plt
# plt.bar(["1.Sınav","2.Sınav","3.Sınav"], [80,70,90]) #sütun grafiği
# plt.show()

import matplotlib.pyplot as plt
plt.title('Öğrencilerin Sınav Başarıları')
# X ve Y eksenlerine etiketler ekleme
plt.xlabel('Sınavlar')
plt.ylabel('Puanlar')
plt.plot(["1.Sınav","2.Sınav","3.Sınav"], [80,70,90]) #sütun grafiği

plt.show()
