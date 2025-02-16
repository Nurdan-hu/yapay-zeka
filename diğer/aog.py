print("Askeri okula mülakat puanı 85 ve üzeri, sabıka kaydı olmayan erkek öğrenciler katılabilir.")
puan = int(input ("Mülakat puanın kaç? "))
c = input ("Cinsiyetin nedir? ")
sk = input ("Sabıka kaydın var mı? ")
liste1 = ["var", "Var", "evet","Evet","E"]
cinsiyet = ["Erkek","erkek","e","E"]
if sk not in liste1:  
    if puan < 0 or puan > 100 :
        print("Yanlış giriş")
    else :
        if puan > 85 : print ("Puanın çok güzel")
        elif puan > 70 : print ("Puanın iyi")
        elif puan > 50 : print ("Geçmişsin")
        else : print ("Kalmışsın dostum.")

    if puan>=85 and c in cinsiyet:
        print("Askeri okula girebilirsin")
    else : print("Bu okula giremezsin")

