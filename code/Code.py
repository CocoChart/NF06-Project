
import matplotlib as plt
import numpy as np
import pandas as pd
from math import *
from ctypes import *
from tkinter import * 

functions = CDLL("./fonction.dll")

# with open("./Conso.csv") as f :
#     print("la bite")
#     conso = pd.read_csv(f)
# print(conso)

# print(conso["X"])
# test = [1, 2, 3]
# tab = ( c_int * len(conso))(*conso)

# print("oui\n" ,*tab)
# article = c_char(input("Entrer l'article concerné (X ou Y)"))
vente = c_int(0)
delais = c_int(0)
stock = c_int (5)
seuil = c_int(15)
nombre_de_commande = c_int(0)
taille_commande =  c_int(0)
cout_stock = c_float(0)
cout_total = c_float(0)
prix = c_float(45)
prix_commande = c_float(76)
commande = c_int(0)
temp_commande = c_int(1)
prix_stockage = c_float(0.75)
# functions.reception(pointer(delais), pointer(stock),pointer(commande))
# functions.passage_commande_compteur_mois(pointer(stock), pointer(delais), pointer(commande), pointer(nombre_de_commande),temp_commande,seuil, pointer(cout_total), prix, prix_commande )
# functions.vente_et_prix_stockage(vente,pointer(stock),pointer(cout_stock),prix,prix_stockage,pointer(cout_total))
# functions.calcul(pointer(stock), seuil, pointer(nombre_de_commande),pointer(taille_commande), temp_commande, prix, prix_commande,prix_stockage,pointer(cout_stock), pointer(cout_total))