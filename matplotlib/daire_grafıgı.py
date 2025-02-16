import matplotlib.pyplot as plt
sınavlar = ["1.Sınav","2.Sınav","3.Sınav"]
notlar = [80,70,90]

plt.title('Sınavlar Notlarının Dağılımı')
plt.pie(notlar,labels=sınavlar, autopct='%1.1f%%')  #yüzde gösteriyor
plt.show()