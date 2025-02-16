import pandas as pd

print(pd.__version__)
Dataframe = {
  'arabalar': ["BMW", "Togg", "Honda"],
  'satış': [200, 10, 150]
}
dizi = pd.DataFrame(Dataframe)
dizi.index = dizi.index + 1
print(dizi)