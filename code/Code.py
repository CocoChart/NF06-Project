from ctypes import *
import pandas as pd
import statistics as st
import matplotlib.pyplot as plt
from tkinter import * 

functions = CDLL("./functions.dll")
##Fonction qui lit le tableau des ventes depuis un csv
def lecture(tabX,tabY): 
    with open("./Conso.csv") as f :
        conso = pd.read_csv(f)
    print(conso)
    #Séparation des ventes des deux articles :
    tabX = conso["X"].to_list()
    tabY = conso["Y"].to_list()

    #print(tabX)
    #print(tabY)
    return(tabX,tabY)

consoX=[]
consoY=[]
consoX,consoY = lecture(consoX,consoY)
#print(consoX)
#print(consoY)

##Calcule les ventes moyennes sur l'année de X
calc_moy_X = int(st.mean(consoX) + 1)

#print(calc_moy_X)

##Prix d'une commande
prix_commande = c_int(76)

##Nombre de ventes de X
vente_X = c_int(0)
##Prix unitaire de X
prix_X = c_float(45)
##Nombre de produits en stock
stock_X = c_int (5)
##Valeur en format C de la moyenne des ventes
moy_X = c_int(calc_moy_X)
##Point de commande
seuil_X = c_int(15)
nombre_de_commande_X = c_int(0)
taille_commande_X =  c_int(0)
temps_livraison_X = c_int(1)
##Délai avant la prochaine livraison
delais_X = c_int(0)
prix_stockage_X = c_float(0.75) # = 0,2 * prix_X / 12
cout_stock_X = c_float(0)
cout_total_X = c_float(0)   
#print(cout_total_X.value)
i=0



# Pour pouvoir utiliser les nouvelles fonctions en c qui prennent en compte le stock total et évite de payer deux fois le prix de commande
# quand deux commande sont passé le même mois il faut déclarer X et Y avant d'utiliser les fonctions

##Calcule les ventes moyennes sur l'année de Y
calc_moy_Y = int(st.mean(consoY) + 1)


##Nombre de ventes de Y
vente_Y = c_int(0)
##Prix unitaire de Y
prix_Y = c_float(15)
##Nombre de produits en stock
stock_Y = c_int (65)
##Valeur en format C de la moyenne des ventes
moy_Y = c_int(calc_moy_Y)
##Point de commande
seuil_Y = c_int(90)
nombre_de_commande_Y = c_int(0)
taille_commande_Y =  c_int(0)
temps_livraison_Y = c_int(2)
##Délai avant la prochaine livraison
delais_Y = c_int(0)
prix_stockage_Y = c_float(0.25) # = 0,2 * prix_Y / 12
cout_stock_Y = c_float(0)
cout_total_Y = c_float(0)   

# je rajoute la veleur de stock max :
stock_max = c_int(150)




commandes_X=[]
reception_X=[]
sorties_X=[]
niveau_stock_X = []
stock_moy_X=[]

##Fonction permettant de simuler l'évolution sur un an 
for i in range (0,11+1) :
    vente_X=consoX[i]
    #print(vente_X)
    sorties_X.append(' ')
    sorties_X.append(vente_X)

    if delais_X.value==0 : reception_X.append(taille_commande_X.value)
    else : reception_X.append(0)
    reception_X.append(' ')
    functions.reception(pointer(delais_X),pointer(stock_X),pointer(taille_commande_X))
    niveau_stock_X.append(stock_X.value)
    

    functions.passage_commande_compteur_mois(pointer(stock_X),pointer(stock_Y),stock_max, pointer(delais_X), pointer(delais_Y), pointer(taille_commande_X), pointer(nombre_de_commande_X), temps_livraison_X ,temps_livraison_Y ,moy_X, seuil_X, pointer(cout_total_X), prix_X, prix_commande)
    commandes_X.append(taille_commande_X.value)
    commandes_X.append(' ')

    functions.vente_et_prix_stockage(vente_X, pointer(stock_X), pointer(cout_stock_X), prix_X, prix_stockage_X, pointer(cout_total_X))
    niveau_stock_X.append(stock_X.value)
    #print("Cout total Py : ", cout_total_X.value)


functions.reception(pointer(delais_X),pointer(stock_X),pointer(taille_commande_X))



print("voici la valeur de stock final de X :\n", stock_X.value)
print("voici la valeur du cout de stockage de X:\n", cout_stock_X.value)
cout_total_X.value += cout_stock_X.value
print("voici le cout total pour X: \n", cout_total_X.value)

for i in range (int(len(niveau_stock_X)/2)) :
    stock_moy_X.append(' ')
    stock_moy_X.append((niveau_stock_X[i]+niveau_stock_X[i+1])/2)
    

'''print(commandes_X)
print(reception_X)
print(sorties_X)
print(niveau_stock_X)
print(stock_moy_X)'''

#functions.calcul(pointer(stock_X), seuil_X, pointer(nombre_de_commande_X), pointer(taille_commande_X), temps_livraison_X, prix_X, prix_commande, prix_stockage_X,pointer(cout_stock_X), pointer(cout_total_X))


#--------------------------------------------Article Y-------------------------------------------------------------

# ##Calcule les ventes moyennes sur l'année de Y
# calc_moy_Y = int(st.mean(consoY) + 1)


# ##Nombre de ventes de Y
# vente_Y = c_int(0)
# ##Prix unitaire de Y
# prix_Y = c_float(15)
# ##Nombre de produits en stock
# stock_Y = c_int (65)
# ##Valeur en format C de la moyenne des ventes
# moy_Y = c_int(calc_moy_Y)
# ##Point de commande
# seuil_Y = c_int(90)
# nombre_de_commande_Y = c_int(0)
# taille_commande_Y =  c_int(0)
# temps_livraison_Y = c_int(2)
# ##Délai avant la prochaine livraison
# delais_Y = c_int(0)
# prix_stockage_Y = c_float(0.25) # = 0,2 * prix_Y / 12
# cout_stock_Y = c_float(0)
# cout_total_Y = c_float(0)   
#print(cout_total_Y.value)
i=0


commandes_Y=[]
reception_Y=[]
sorties_Y=[]
niveau_stock_Y = []
stock_moy_Y=[]

##Fonction permettant de simuler l'évolution sur un an 
for i in range (0,11+1) :
    vente_Y=consoY[i]
    #print(vente_Y)
    sorties_Y.append(' ')
    sorties_Y.append(vente_Y)

    if delais_Y.value==0 : reception_Y.append(taille_commande_Y.value)
    else : reception_Y.append(0)
    reception_Y.append(' ')
    functions.reception(pointer(delais_Y),pointer(stock_Y),pointer(taille_commande_Y))
    niveau_stock_Y.append(stock_Y.value)
    

    functions.passage_commande_compteur_mois(pointer(stock_Y),pointer(stock_X),stock_max, pointer(delais_Y), pointer(delais_X), pointer(taille_commande_Y), pointer(nombre_de_commande_Y), temps_livraison_Y,temps_livraison_X, moy_Y, seuil_Y, pointer(cout_total_Y), prix_Y, prix_commande)
    commandes_Y.append(taille_commande_Y.value)
    commandes_Y.append(' ')

    functions.vente_et_prix_stockage(vente_Y, pointer(stock_Y), pointer(cout_stock_Y), prix_Y, prix_stockage_Y, pointer(cout_total_Y))
    niveau_stock_Y.append(stock_Y.value)
    #print("Cout total Py : ", cout_total_Y.value)


functions.reception(pointer(delais_Y),pointer(stock_Y),pointer(taille_commande_Y))



print("voici la valeur de stock final de Y :\n", stock_Y.value)
print("voici la valeur du cout de stockage de Y:\n", cout_stock_Y.value)
cout_total_Y.value += cout_stock_Y.value
print("voici le cout total pour Y: \n", cout_total_Y.value)

for i in range (int(len(niveau_stock_Y)/2)) :
    stock_moy_Y.append(' ')
    stock_moy_Y.append((niveau_stock_Y[i]+niveau_stock_Y[i+1])/2)
    




#Interface Graphique

liste_mois = ["Début Janvier", "Fin Janvier", "Début Février", "Fin Février", "Début Mars", "Fin Mars", "Début Avril", "Fin Avril", "Début Mai", "Fin Mai", "Début Juin", "Fin Juin", "Début Juillet", "Fin Juillet", "Début Août", "Fin Août", "Début Septembre", "Fin Septembre", "Début Octobre", "Fin Octobre", "Début Novembre", "Fin Novembre", "Début Décembre", "Fin Décembre"]
noms_colonnes = ["Mois", "Commande", "Réception", "Sorties", "Niveau Stock", "Stock Moyen"]

fenetre=Tk()

##Création des colonnes
for i in range(6):
    Button(fenetre, text=noms_colonnes[i], borderwidth=1,width=15,state=DISABLED,disabledforeground='black').grid(row=0, column=i)
##Remplissage du tableau ligne par ligne
for ligne in range(24):
    Button(fenetre, text=liste_mois[ligne], borderwidth=1,width=15,state=DISABLED,disabledforeground='black').grid(row=ligne+1, column=0)
    Button(fenetre, text=commandes_X[ligne], borderwidth=1,width=15,state=DISABLED,disabledforeground='black').grid(row=ligne+1, column=1)
    Button(fenetre, text=reception_X[ligne], borderwidth=1,width=15,state=DISABLED,disabledforeground='black').grid(row=ligne+1, column=2)
    Button(fenetre, text=sorties_X[ligne], borderwidth=1,width=15,state=DISABLED,disabledforeground='black').grid(row=ligne+1, column=3)
    Button(fenetre, text=niveau_stock_X[ligne], borderwidth=1,width=15,state=DISABLED,disabledforeground='black').grid(row=ligne+1, column=4)
    Button(fenetre, text=stock_moy_X[ligne], borderwidth=1,width=15,state=DISABLED,disabledforeground='black').grid(row=ligne+1, column=5)

for ligne in range(24):
    Button(fenetre, text=' ', borderwidth=1,width=15,state=DISABLED,disabledforeground='black').grid(row=ligne+1, column=6)

##Création des colonnes
for i in range(7,13):
    Button(fenetre, text=noms_colonnes[i-7], borderwidth=1,width=15,state=DISABLED,disabledforeground='black').grid(row=0, column=i)
##Remplissage du tableau ligne par ligne
for ligne in range(24):
    Button(fenetre, text=liste_mois[ligne], borderwidth=1,width=15,state=DISABLED,disabledforeground='black').grid(row=ligne+1, column=7)
    Button(fenetre, text=commandes_Y[ligne], borderwidth=1,width=15,state=DISABLED,disabledforeground='black').grid(row=ligne+1, column=8)
    Button(fenetre, text=reception_Y[ligne], borderwidth=1,width=15,state=DISABLED,disabledforeground='black').grid(row=ligne+1, column=9)
    Button(fenetre, text=sorties_Y[ligne], borderwidth=1,width=15,state=DISABLED,disabledforeground='black').grid(row=ligne+1, column=10)
    Button(fenetre, text=niveau_stock_Y[ligne], borderwidth=1,width=15,state=DISABLED,disabledforeground='black').grid(row=ligne+1, column=11)
    Button(fenetre, text=stock_moy_Y[ligne], borderwidth=1,width=15,state=DISABLED,disabledforeground='black').grid(row=ligne+1, column=12)

##Affiche le tableau sans bloquer le programme, ce qui permet d'afficher le graphique en même temps
async def affichage():
    fenetre.mainloop()
affichage()

plt.plot(niveau_stock_X, label="Stock de X",marker='o',markersize=3)
plt.plot(niveau_stock_Y, label="Stock de Y", marker='o',markersize=3)
plt.legend()
plt.show()