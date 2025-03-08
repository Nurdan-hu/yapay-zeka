import re
xxx = "Ahmet al renkli bir şal aldı."
print(re.findall("a|A", xxx)) #| veya anlamına gelir
print(re.findall("^A", xxx))  #cümle başında demek