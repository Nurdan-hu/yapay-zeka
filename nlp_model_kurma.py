from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer

text_clf= Pipeline([
    ('tfidf' , TfidfVectorizer()),
    ('clf' , MultinomialNB())
])

veriler = ["Bu fırsatı kaçırmayın!" , "Merhaba, nasılsınız?" , "Hemen tıkla ve kazan!"]
etiketler = [1,0,1] #1 spam , 0 normal

text_clf.fit(veriler,etiketler)
yeni_metin = ["Ahmet iyi misin?"]
tahmin = text_clf.predict(yeni_metin)
print(tahmin) #spam olarak işaretliyor.