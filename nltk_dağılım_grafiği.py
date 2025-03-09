# pip install matplotlib

import nltk
# nltk.download("book") # uzun
nltk.download('gutenberg') # kısa
from nltk.book import *
import matplotlib.pyplot as plt

# İlanlardaki (text8) bazı kelimelerin kullanım sıklığı.
text8.dispersion_plot(
    ["woman", "lady", "girl", "gal", "man", "gentleman", "boy", "guy"]
)
plt.show() 
