import random
liste=[1,2,3,4,5,6,7,8,9]
tutulan=[]
tahmin_liste=[]
tahmin=-1
bayrak_x=0
bayrak_y=0
for i in range(1,5):
    sayi=random.choice(liste)
    liste.remove(sayi)
    tutulan.append(sayi)

while (tahmin!=0):
    tahmin=int(input("Tahminin gir...:"))
    tahmin_liste=[int(x) for x in str(tahmin)]
    # print(tutulan,tahmin_liste)

    for x in range(len(tutulan)):
        for i in range(len(tahmin_liste)):
            if (tutulan[x]==tahmin_liste[i] and x==i):
                bayrak_x = bayrak_x + 1
            if (tutulan[x]==tahmin_liste[i] and x!=i):
                bayrak_y=bayrak_y-1
    print("__Tahmin____       Doğru      Yanlış")
    print(tahmin_liste,"     ",bayrak_x,"        ",bayrak_y)
    bayrak_x=bayrak_y=0
    if tutulan == tahmin_liste:
        print(tutulan,"Tahmin Doğru")
        break
            
                
                
