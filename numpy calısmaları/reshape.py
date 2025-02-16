# import numpy as np
# ee = np.eye(5)
# print(ee)

# aralikDizisi= np.arange(50,100,5) #pythondaki range ile aynı işlev
# print(aralikDizisi)


import numpy as np

arr1 = np.arange(1,11)
arr1 = arr1.reshape(5,2) #mevcut veriyi desteklemeli yani 2x5= 10 ve 11-1=10

tersi = arr1[::-1]
print("Dizi :\n",arr1)
print("Tersi:\n",tersi) 
