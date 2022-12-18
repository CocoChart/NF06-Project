from ctypes import *
import pandas as pd
import statistics as st
import matplotlib.pyplot as plt
from tkinter import * 

##
# @file Code.py
# @brief Fichier contenant le code python permettant de simuler l'évolution du stock sur un an
# @author Corentin CHARTIER & Maël JAVER KALA

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
prix_commande = c_float(76)

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
seuil_max_X = c_int(25)
nombre_de_commande_X = c_int(0)
taille_commande_X =  c_int(0)
temps_livraison_X = c_int(1)
cycle_X = c_int(3)
##Délai avant la prochaine livraison
delais_X = c_int(0)
prix_stockage_X = c_float(0.75) # = 0,2 * prix_X / 12
cout_stock_X = c_float(0)
cout_rupture_X = c_float(0)
cout_total_X = c_float(0)   
#print(cout_total_X.value)
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
seuil_max_Y = c_int(130)
nombre_de_commande_Y = c_int(0)
taille_commande_Y =  c_int(0)
temps_livraison_Y = c_int(2)
cycle_Y = c_int(4)
##Délai avant la prochaine livraison
delais_Y = c_int(0)
prix_stockage_Y = c_float(0.25) # = 0,2 * prix_Y / 12
cout_stock_Y = c_float(0)
cout_rupture_Y = c_float(0)
cout_total_Y = c_float(0)   

## Valeur de stock max, les deux produits comptent :
stock_max = c_int(150)

# ------------------------------------------------- Gestion à point de commande X ---------------------------------------------------------

commandes_X=[]
reception_X=[]
sorties_X=[]
niveau_stock_X = []
stock_moy_X=[]

##Fonction permettant de simuler l'évolution sur un an 
compteur_mois = c_int(0)
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
    
    functions.passage_commande_PC(pointer(stock_X),pointer(stock_Y),stock_max, pointer(delais_X), pointer(delais_Y), pointer(taille_commande_X), pointer(nombre_de_commande_X), temps_livraison_X ,temps_livraison_Y ,moy_X, seuil_X, pointer(cout_total_X), prix_X, prix_commande)
    commandes_X.append(taille_commande_X.value)
    commandes_X.append(' ')

    functions.passage_de_mois(pointer(stock_X), pointer(stock_Y), seuil_X, seuil_Y, pointer(compteur_mois), pointer(delais_X), pointer(delais_Y))
    functions.vente_et_prix_stockage(vente_X, pointer(stock_X), pointer(cout_stock_X), prix_X, prix_stockage_X,pointer(cout_rupture_X), pointer(cout_total_X))
    niveau_stock_X.append(stock_X.value)
    #print("Cout total Py : ", cout_total_X.value)


functions.reception(pointer(delais_X),pointer(stock_X),pointer(taille_commande_X))



print("voici la valeur de stock final de X en point de commande :\n", stock_X.value)
print("voici la valeur du cout de stockage de X en point de commande:\n", cout_stock_X.value)
print("voici la valeur du cout de rupture :\n", cout_rupture_X.value)
cout_total_X.value += cout_stock_X.value + cout_rupture_X.value
print("voici le cout total pour X en point de commande : \n", cout_total_X.value)

for i in range (int(len(niveau_stock_X)/2)) :
    stock_moy_X.append(' ')
    stock_moy_X.append((niveau_stock_X[i]+niveau_stock_X[i+1])/2)
    

'''print(commandes_X)
print(reception_X)
print(sorties_X)
print(niveau_stock_X)
print(stock_moy_X)'''


#-------------------------------------------- Gestion à point de commande Y -------------------------------------------------------------

commandes_Y=[]
reception_Y=[]
sorties_Y=[]
niveau_stock_Y = []
stock_moy_Y=[]

##Fonction permettant de simuler l'évolution sur un an 
compteur_mois = c_int(0)
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
    

    functions.passage_commande_PC(pointer(stock_Y),pointer(stock_X),stock_max, pointer(delais_Y), pointer(delais_X), pointer(taille_commande_Y), pointer(nombre_de_commande_Y), temps_livraison_Y,temps_livraison_X, moy_Y, seuil_Y, pointer(cout_total_Y), prix_Y, prix_commande)
    commandes_Y.append(taille_commande_Y.value)
    commandes_Y.append(' ')

    functions.passage_de_mois(pointer(stock_Y), pointer(stock_X), seuil_Y, seuil_X,pointer(compteur_mois), pointer(delais_Y), pointer(delais_X))
    
    functions.vente_et_prix_stockage(vente_Y, pointer(stock_Y), pointer(cout_stock_Y), prix_Y, prix_stockage_Y,pointer(cout_rupture_Y), pointer(cout_total_Y))
    niveau_stock_Y.append(stock_Y.value)
    #print("Cout total Py : ", cout_total_Y.value)


functions.reception(pointer(delais_Y),pointer(stock_Y),pointer(taille_commande_Y))



print("voici la valeur de stock final de Y en point de commande :\n", stock_Y.value)
print("voici la valeur du cout de stockage de Y en point de commande :\n", cout_stock_Y.value)
print("voici la valeur du cout de rupture :\n", cout_rupture_Y.value)
cout_total_Y.value += cout_stock_Y.value + cout_rupture_Y.value
print("voici le cout total pour Y en point de commande: \n", cout_total_Y.value)

for i in range (int(len(niveau_stock_Y)/2)) :
    stock_moy_Y.append(' ')
    stock_moy_Y.append((niveau_stock_Y[i]+niveau_stock_Y[i+1])/2)


# ------------------------------------------------------ Gestion Périodique X ---------------------------------------------------------------

commandes_X_period=[]
reception_X_period=[]
sorties_X_period=[]
niveau_stock_X_period = []
stock_moy_X_period =[]

##Fonction permettant de simuler l'évolution sur un an 
print("\n\n")
commandes_X_total = c_int(0)
stock_X.value = 5
stock_Y.value = 65
compteur_mois.value = 0
nombre_de_commande_X.value = 0
cout_stock_X.value = 0
cout_rupture_X.value = 0
cout_total_X.value = 0
for i in range (0,11+1) :
    vente_X=consoX[i]
    #print(vente_X)
    sorties_X_period.append(' ')
    sorties_X_period.append(vente_X)

    if delais_X.value==0 : reception_X_period.append(taille_commande_X.value)
    else : reception_X_period.append(0)
    reception_X_period.append(' ')
    functions.reception(pointer(delais_X),pointer(stock_X),pointer(taille_commande_X))
    niveau_stock_X_period.append(stock_X.value)
    
    functions.passage_commande_P(pointer(stock_X),pointer(stock_Y),stock_max,compteur_mois, cycle_X, pointer(delais_X), pointer(delais_Y), pointer(taille_commande_X), pointer(nombre_de_commande_X), temps_livraison_X ,temps_livraison_Y , seuil_max_X, pointer(cout_total_X), prix_X, prix_commande)
    commandes_X_period.append(taille_commande_X.value)
    commandes_X_period.append(' ')
    commandes_X_total.value += taille_commande_X.value  
    functions.passage_de_mois(pointer(stock_X), pointer(stock_Y), seuil_X, seuil_Y,pointer(compteur_mois), pointer(delais_X), pointer(delais_Y))
     
   
    functions.vente_et_prix_stockage(vente_X, pointer(stock_X), pointer(cout_stock_X), prix_X, prix_stockage_X,pointer(cout_rupture_X), pointer(cout_total_X))
    niveau_stock_X_period.append(stock_X.value)
    #print("Cout total Py : ", cout_total_X.value)


functions.reception(pointer(delais_X),pointer(stock_X),pointer(taille_commande_X))



print("voici la valeur de stock final de X en Périodique :\n", stock_X.value)
print("voici la valeur du cout de stockage de X en Périodique :\n", cout_stock_X.value)
print("voici le nombre de commande : \n", nombre_de_commande_X.value)
print("voici le nombre de produit commandé  : \n", commandes_X_total.value)
print("voici la valeur du cout de rupture :\n", cout_rupture_X.value)
cout_total_X.value += cout_stock_X.value +cout_rupture_X.value
print("voici le cout total pour X en Périodique : \n", cout_total_X.value)

for i in range (int(len(niveau_stock_X_period)/2)) :
    stock_moy_X_period.append(' ')
    stock_moy_X_period.append((niveau_stock_X[i]+niveau_stock_X[i+1])/2)
    

'''print(commandes_X)
print(reception_X)
print(sorties_X)
print(niveau_stock_X)
print(stock_moy_X)'''



# ------------------------------------------------------------------ Gestion Périodique Y -----------------------------------------------------------------------


commandes_Y_period=[]
reception_Y_period=[]
sorties_Y_period=[]
niveau_stock_Y_period = []
stock_moy_Y_period =[]

##Fonction permettant de simuler l'évolution sur un an 
print("\n")
commandes_Y_total = c_int(0)
stock_X.value = 5
stock_Y.value = 65
compteur_mois.value = 0
nombre_de_commande_Y.value = 0
cout_stock_Y.value = 0
cout_rupture_Y.value = 0
cout_total_Y.value = 0
for i in range (0,11+1) :
    vente_Y=consoX[i]
    #print(vente_X)
    sorties_Y_period.append(' ')
    sorties_Y_period.append(vente_Y)

    if delais_X.value==0 : reception_Y_period.append(taille_commande_Y.value)
    else : reception_Y_period.append(0)
    reception_Y_period.append(' ')
    functions.reception(pointer(delais_Y),pointer(stock_Y),pointer(taille_commande_Y))
    niveau_stock_Y_period.append(stock_Y.value)
    
    functions.passage_commande_P(pointer(stock_Y),pointer(stock_X),stock_max,compteur_mois, cycle_Y , pointer(delais_Y), pointer(delais_X), pointer(taille_commande_Y), pointer(nombre_de_commande_Y), temps_livraison_Y ,temps_livraison_X , seuil_max_Y, pointer(cout_total_Y), prix_Y, prix_commande)
    commandes_Y_period.append(taille_commande_Y.value)
    commandes_Y_period.append(' ')
    if delais_Y.value == temps_livraison_Y.value :
        # print("taille commande :", taille_commande_Y.value)
        commandes_Y_total.value += taille_commande_Y.value 
    
    functions.passage_de_mois(pointer(stock_Y), pointer(stock_X), seuil_Y, seuil_X,pointer(compteur_mois), pointer(delais_Y), pointer(delais_X))
    # print("delais : ", delais_Y.value)
    # print("print temps livraison : ", temps_livraison_Y.value)
     
   
    functions.vente_et_prix_stockage(vente_Y, pointer(stock_Y), pointer(cout_stock_Y), prix_Y, prix_stockage_Y, pointer(cout_rupture_Y), pointer(cout_total_Y))
    niveau_stock_Y_period.append(stock_Y.value)
    #print("Cout total Py : ", cout_total_X.value)


functions.reception(pointer(delais_Y),pointer(stock_Y),pointer(taille_commande_Y))



print("voici la valeur de stock final de Y en Périodique :\n", stock_Y.value)
print("voici la valeur du cout de stockage de Y en Périodique :\n", cout_stock_Y.value)
print("voici le nombre de commande : \n", nombre_de_commande_Y.value)
print("voici le nombre de produit commandé  : \n", commandes_Y_total.value)
print("voici la valeur du cout de rupture :\n", cout_rupture_Y.value)
cout_total_Y.value += cout_stock_Y.value + cout_rupture_Y.value
print("voici le cout total pour Y en Périodique : \n", cout_total_Y.value)

for i in range (int(len(niveau_stock_Y_period)/2)) :
    stock_moy_Y_period.append(' ')
    stock_moy_Y_period.append((niveau_stock_X[i]+niveau_stock_X[i+1])/2)
    

'''print(commandes_X)
print(reception_X)
print(sorties_X)
print(niveau_stock_X)
print(stock_moy_X)'''




# ------------------------------------------------------------------ Interface Graphique ------------------------------------------------------------------------
##\cond


liste_mois = ["Début Janvier", "Fin Janvier", "Début Février", "Fin Février", "Début Mars", "Fin Mars", "Début Avril", "Fin Avril", "Début Mai", "Fin Mai", "Début Juin", "Fin Juin", "Début Juillet", "Fin Juillet", "Début Août", "Fin Août", "Début Septembre", "Fin Septembre", "Début Octobre", "Fin Octobre", "Début Novembre", "Fin Novembre", "Début Décembre", "Fin Décembre"]
noms_colonnes = ["Mois", "Commande", "Réception", "Sorties", "Niveau Stock", "Stock Moyen"]

fenetre_PC=Tk()
fenetre_PC.title("Gestion à point de commande")
#Tableau pour X en point de commande
Button(fenetre_PC, text="Produit X en point de commande", borderwidth=1,width=15*6,state=DISABLED,disabledforeground='black').grid(row=0, column=0, columnspan=6)
#Création des colonnes
for i in range(6):
    Button(fenetre_PC, text=noms_colonnes[i], borderwidth=1,width=15,state=DISABLED,disabledforeground='black').grid(row=1, column=i)
#Remplissage du tableau ligne par ligne
for ligne in range(24):
    Button(fenetre_PC, text=liste_mois[ligne], borderwidth=1,width=15,state=DISABLED,disabledforeground='black').grid(row=ligne+2, column=0)
    Button(fenetre_PC, text=commandes_X[ligne], borderwidth=1,width=15,state=DISABLED,disabledforeground='black').grid(row=ligne+2, column=1)
    Button(fenetre_PC, text=reception_X[ligne], borderwidth=1,width=15,state=DISABLED,disabledforeground='black').grid(row=ligne+2, column=2)
    Button(fenetre_PC, text=sorties_X[ligne], borderwidth=1,width=15,state=DISABLED,disabledforeground='black').grid(row=ligne+2, column=3)
    Button(fenetre_PC, text=niveau_stock_X[ligne], borderwidth=1,width=15,state=DISABLED,disabledforeground='black').grid(row=ligne+2, column=4)
    Button(fenetre_PC, text=stock_moy_X[ligne], borderwidth=1,width=15,state=DISABLED,disabledforeground='black').grid(row=ligne+2, column=5)

for ligne in range(24):
    Button(fenetre_PC, text=' ', borderwidth=1,width=15,state=DISABLED,disabledforeground='black').grid(row=ligne+1, column=6)




#Tableau pour Y en point de commande
Button(fenetre_PC, text="Produit Y en point de commande", borderwidth=1,width=15*6,state=DISABLED,disabledforeground='black').grid(row=0, column=7, columnspan=6)

#Création des colonnes
for i in range(7,13):
    Button(fenetre_PC, text=noms_colonnes[i-7], borderwidth=1,width=15,state=DISABLED,disabledforeground='black').grid(row=1, column=i)
#Remplissage du tableau ligne par ligne
for ligne in range(24):
    Button(fenetre_PC, text=liste_mois[ligne], borderwidth=1,width=15,state=DISABLED,disabledforeground='black').grid(row=ligne+2, column=7)
    Button(fenetre_PC, text=commandes_Y[ligne], borderwidth=1,width=15,state=DISABLED,disabledforeground='black').grid(row=ligne+2, column=8)
    Button(fenetre_PC, text=reception_Y[ligne], borderwidth=1,width=15,state=DISABLED,disabledforeground='black').grid(row=ligne+2, column=9)
    Button(fenetre_PC, text=sorties_Y[ligne], borderwidth=1,width=15,state=DISABLED,disabledforeground='black').grid(row=ligne+2, column=10)
    Button(fenetre_PC, text=niveau_stock_Y[ligne], borderwidth=1,width=15,state=DISABLED,disabledforeground='black').grid(row=ligne+2, column=11)
    Button(fenetre_PC, text=stock_moy_Y[ligne], borderwidth=1,width=15,state=DISABLED,disabledforeground='black').grid(row=ligne+2, column=12)

#------------------------------------Tableaux gestion périodique--------------------------------------------------------------------
fenetre_Period=Tk()
fenetre_Period.title("Gestion périodique")

#Tableau pour X en périodique
Button(fenetre_Period, text="Produit X en périodique", borderwidth=1,width=15*6,state=DISABLED,disabledforeground='black').grid(row=0, column=0, columnspan=6)
#Création des colonnes
for i in range(6):
    Button(fenetre_Period, text=noms_colonnes[i], borderwidth=1,width=15,state=DISABLED,disabledforeground='black').grid(row=1, column=i)
#Remplissage du tableau ligne par ligne
for ligne in range(24):
    Button(fenetre_Period, text=liste_mois[ligne], borderwidth=1,width=15,state=DISABLED,disabledforeground='black').grid(row=ligne+2, column=0)
    Button(fenetre_Period, text=commandes_X_period[ligne], borderwidth=1,width=15,state=DISABLED,disabledforeground='black').grid(row=ligne+2, column=1)
    Button(fenetre_Period, text=reception_X_period[ligne], borderwidth=1,width=15,state=DISABLED,disabledforeground='black').grid(row=ligne+2, column=2)
    Button(fenetre_Period, text=sorties_X_period[ligne], borderwidth=1,width=15,state=DISABLED,disabledforeground='black').grid(row=ligne+2, column=3)
    Button(fenetre_Period, text=niveau_stock_X_period[ligne], borderwidth=1,width=15,state=DISABLED,disabledforeground='black').grid(row=ligne+2, column=4)
    Button(fenetre_Period, text=stock_moy_X_period[ligne], borderwidth=1,width=15,state=DISABLED,disabledforeground='black').grid(row=ligne+2, column=5)

for ligne in range(24):
    Button(fenetre_Period, text=' ', borderwidth=1,width=15,state=DISABLED,disabledforeground='black').grid(row=ligne+1, column=6)



#Tableau pour Y en périodique
Button(fenetre_Period, text="Produit Y en périodique", borderwidth=1,width=15*6,state=DISABLED,disabledforeground='black').grid(row=0, column=7, columnspan=6)

#Création des colonnes
for i in range(7,13):
    Button(fenetre_Period, text=noms_colonnes[i-7], borderwidth=1,width=15,state=DISABLED,disabledforeground='black').grid(row=1, column=i)
#Remplissage du tableau ligne par ligne
for ligne in range(24):
    Button(fenetre_Period, text=liste_mois[ligne], borderwidth=1,width=15,state=DISABLED,disabledforeground='black').grid(row=ligne+2, column=7)
    Button(fenetre_Period, text=commandes_Y_period[ligne], borderwidth=1,width=15,state=DISABLED,disabledforeground='black').grid(row=ligne+2, column=8)
    Button(fenetre_Period, text=reception_Y_period[ligne], borderwidth=1,width=15,state=DISABLED,disabledforeground='black').grid(row=ligne+2, column=9)
    Button(fenetre_Period, text=sorties_Y_period[ligne], borderwidth=1,width=15,state=DISABLED,disabledforeground='black').grid(row=ligne+2, column=10)
    Button(fenetre_Period, text=niveau_stock_Y_period[ligne], borderwidth=1,width=15,state=DISABLED,disabledforeground='black').grid(row=ligne+2, column=11)
    Button(fenetre_Period, text=stock_moy_Y_period[ligne], borderwidth=1,width=15,state=DISABLED,disabledforeground='black').grid(row=ligne+2, column=12)



##Affiche le tableau de gestion des stocks sans bloquer le programme, ce qui permet d'afficher le graphique en même temps
async def affichage():
    fenetre_PC.mainloop()
    fenetre_Period.mainloop()
affichage()

fig, (pc,per) = plt.subplots(2, sharex=True)


#Graphique Pour la gestion à PC

pc.plot(niveau_stock_X, label="Stock de X",marker='o',markersize=3)
pc.plot(niveau_stock_Y, label="Stock de Y", marker='o',markersize=3)
pc.legend()
pc.set_title("Gestion à point de commande")

#Graphique pour la gestion périodique

per.plot(niveau_stock_X_period, label="Stock de X",marker='o',markersize=3)
per.plot(niveau_stock_Y_period, label="Stock de Y", marker='o',markersize=3)
per.legend()
per.set_title("Gestion périodique")


plt.show()

print("FIN")
##\endcond