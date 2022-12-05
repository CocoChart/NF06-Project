
import matplotlib as plt
import numpy as np
import pandas as pd
from math import *
from ctypes import *
from tkinter import * 

functions = CDLL("./functions.dll")

with open("./Conso.csv") as f :
    print("la bite")
    conso = pd.read_csv(f)
print(conso)

print(conso["X"])
test = [1, 2, 3]
tab = ( c_int * len(conso))(*conso)

print("oui\n" ,*tab)
vente = c_int(0)
stock = c_int (0)
seuil = c_int(0)
nombre_de_commande = c_int(0)
taille_commande =  c_int(0)
delais = c_int(0)
prix_stock = c_int(0)
cout_total = c_int(0)

#functions.calcul(pointer(vente), pointer(stock), pointer(seuil), pointer(nombre_de_commande), pointer(taille_commande), pointer(delais), pointer(prix_stock), pointer(cout_total))