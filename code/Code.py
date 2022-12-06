
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
article = c_char(input("Entrer l'article concerné (X ou Y)"))
vente = c_int(0)
delais = c_int(0)
stock = c_int (65)
seuil = c_int(90)
nombre_de_commande = c_int(0)
taille_commande =  c_int(0)
cout_stock = c_float(0)
cout_total = c_float(0)
prix = c_float(15)
prix_commande = c_float(76)
commande = c_int(0)
temp_commande = c_int(2)
prix_stockage = c_float(0.25)
# functions.reception(delais, pointer(stock),pointer(commande))
# functions.testUnitaire(stock)
functions.calcul(pointer(stock), seuil, pointer(nombre_de_commande),pointer(taille_commande), temp_commande, prix, prix_commande,prix_stockage,pointer(cout_stock), pointer(cout_total))

