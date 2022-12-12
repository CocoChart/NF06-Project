from ctypes import *
import pandas as pd
import statistics as st
import matplotlib as plt
from tkinter import * 

functions = CDLL("./functions.dll")
def lecture(tabX,tabY): #Fonction qui lit le tableau des ventes depuis un csv
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

calc_moy_X = int(st.mean(consoX) + 1)
calc_moy_y = int(st.mean(consoY) + 1)
print(calc_moy_X)

prix_commande = c_int(76)

vente_X = c_int(0)
prix_X = c_int(45)
stock_X = c_int (5)
moy_X = c_float(calc_moy_X)
seuil_X = c_int(15)
nombre_de_commande_X = c_int(0)
taille_commande_X =  c_int(0)
temps_livraison_X = c_int(1)
delais_X = c_int(0)
prix_stockage_X = c_float(0.75) # = 0,2 * prix_X / 12
cout_stock_X = c_float(0)
cout_total_X = c_float(0)   
print(cout_total_X.value)
i=0

for i in range (0,11+1) :
    vente_X=consoX[i]
    #print(vente_X)
    functions.reception(pointer(delais_X),pointer(stock_X),pointer(taille_commande_X))

    functions.passage_commande_compteur_mois(pointer(stock_X), pointer(delais_X), pointer(taille_commande_X), pointer(nombre_de_commande_X), temps_livraison_X,moy_X, seuil_X, pointer(cout_total_X), prix_X, prix_commande)

    functions.vente_et_prix_stockage(vente_X, pointer(stock_X), pointer(cout_stock_X), prix_X, prix_stockage_X, pointer(cout_total_X))
    print("Cout total Py : ", cout_total_X.value)


functions.reception(pointer(delais_X),pointer(stock_X),pointer(taille_commande_X))



print("voici la valeur de stock final :\n", stock_X.value)
print("voici la valeur du cout de stockage :\n", cout_stock_X.value)
cout_total_X.value += cout_stock_X.value
print("voici le cout total : \n", cout_total_X.value)
print("\nFIN\n")

#functions.calcul(pointer(stock_X), seuil_X, pointer(nombre_de_commande_X), pointer(taille_commande_X), temps_livraison_X, prix_X, prix_commande, prix_stockage_X,pointer(cout_stock_X), pointer(cout_total_X))


vente_Y = c_int(0)
stock_Y = c_int (0)
seuil_Y = c_int(0)
nombre_de_commande_Y = c_int(0)
taille_commande_Y =  c_int(0)
delais_Y = c_int(0)
prix_stock_Y = c_int(0)
cout_total_Y = c_int(0)