import re
xxx = "Ahmet al renkli bir şal aldı."
b = (re.search("al", xxx))
print(b)
print(b.span())
print(b.start())
print(b.end())
