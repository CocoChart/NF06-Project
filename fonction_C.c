#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
/**
 * \file fonction_C.c
 * \brief Pour compiler en DLL : gcc  -s -shared -O2 -o functions.dll -fPIC fonction_C.c
 * \author Corentin CHARTIER & Maël JAVER KALA
 */

/*! 
Fonction qui vérifie si une commande est arrivée en vérifiant si le délai de l'objet est nul (signifiant que ce dernier est bien arrivé),
ensuite la fonction incrémente le stock en conséquence et met la valeur de la commande à zéro.
*/
void reception(int *delais_principal, int *stock_Principal, int *commande) 
{
    
    if (*delais_principal == 0) 
    {
        *stock_Principal += *commande; 
        *commande = 0;                 
    }

}

/*!
Fonction qui simule le passage d'un mois en diminuant le délai de livraisons des deux produits et incrémente le compteur de mois
*/
void passage_de_mois( int *compteur_mois, int *delais_P, int *delais_A)
{
    
    *delais_P -= 1;
    *delais_A -= 1; 
    *compteur_mois += 1;
    
}

/*!
ui diminue le stock du montant de la vente, représentant les ventes qui ont eu lieu durant le mois. Ensuite, la fonction
vérifie si le nouveau stock est négatif, si c'est le cas alors il y a rupture de stock et le programme calcule le cout de rupture avant
de passer la valeur de stock à zéro (car il ne peut pas y avoir de stock négatif).
Enfin, la fonction calcule le cout de stockage mensuel des produits restants 
*/
void vente_et_prix_stockage(int vente, int *stock_P, float *cout_stock, float prix, float prix_stockage, float *cout_rupture, float *cout_total)
{

    *stock_P -= vente; 
    if (*stock_P < 0) 
    {
        printf("      Cout de RUPTURE  : %.2f\n", prix * 0.1 * abs(*stock_P));
        *cout_rupture += prix * 0.1 * abs(*stock_P); 
        *stock_P = 0;                                
        printf("      RUPTURE DE STOCK\n");
    }
    *cout_stock += (*stock_P) * (prix_stockage); 

}

//----------------------------------------------------------------------- Gestion à point de commande -----------------------------------------------------------------------------------

/*!
Cette fonction permet de passer des commandes en utilisant la méthode de la gestion à point de commande.
Pour cela, on vérifie, dans un premier temps, si le stock du produit principal est inférieur au stock de sécurité et qu'il n'y a pas de commande déjà en cour.
Si cette condition est vérifiée alors on passe une commande dont la taille correspond aux ventes moyenne de l'année multipliée
par le temps de livraison auquel on rajoute deux mois de sécurité. 
Dans un second temps, après avoir incrémenté le nombre de commandes passé on vérifie si la somme des stocks, après commande, des deux produits sont supérieure
au stock max que peut accueillir l'entrepôt. Si cette valeur excède le stockage max alors on diminue la commande pour ne pas dépasser cette limite. 
Dans un troisième temps, on va venir calculer le prix de la commande en vérifiant en amont si une commande n'a pas déjà été passée ce mois-ci avec le second produit
dans le but de ne pas payer deux fois le prix de passage de commande. 
Enfin on remet le délai à la valeur du temps de livraison. 
*/
void passage_commande_PC(int *stock_principal, int *stock_annexe, int stock_max, int *delais_P, int *delais_A, int *commande, int *nombre_commande, int temp_commande_P, int temp_commande_A, int Vmoyenne, int seuil, float *cout_total, float prix, float prix_commande)
{ 
    
    if (*stock_principal <= seuil && *commande == 0) 
    {
        *commande = (Vmoyenne * (temp_commande_P + 2)) + (seuil - *stock_principal); 
        *nombre_commande += 1;
        if (*stock_principal + *commande + *stock_annexe > stock_max)
        {
            int surplut;
            surplut = (*stock_principal + *commande + *stock_annexe) - stock_max; /// on calcul le nombre de produit sur numéraire avant de les soustraire de la commande
            *commande -= surplut;
        }
        if (*delais_A == temp_commande_A)
        {
            *cout_total += *commande * prix;
        }
        else
        {

            *cout_total += (*commande * prix) + prix_commande; 
        }
        *delais_P = temp_commande_P; 
    }
}
// ---------------------------------------------------------------- Gestion Périodique --------------------------------------------------------------------------------


/*!
Cette fonction permet de passer des commandes en utilisant la méthode de la gestion périodique.
Dans un premier temps, on va venir vérifier si le mois en cour est un multiple du cycle d'actualisation des stocks. Si cette condition 
est vérifiée, on passe commande de telle sorte à atteindre de nouveau le seuil max et incrémente le nombre de commandes. 
Ensuite, on réduit la commande si nécessaire pour ne pas dépasser le stock max et on calcule le cout de cette dernière en vérifiant si une commande 
n'a pas déjà été passée. 
Enfin, on remet le délai à la valeur du temps de livraison. 
*/
void passage_commande_P(int *stock_principal, int *stock_annexe, int stock_max, int compteur_mois, int cycle, int *delais_P, int *delais_A, int *commande, int *nombre_commande, int temp_commande_P, int temp_commande_A, int seuil_max, float *cout_total, float prix, float prix_commande)
{
    
    if (compteur_mois % cycle == 0 && *stock_principal < seuil_max)
    {
    
        *commande = seuil_max - *stock_principal;
        *nombre_commande += 1;
        if (*stock_principal + *commande + *stock_annexe > stock_max)
        {
            int surplus;
            surplus = (*stock_principal + *commande + *stock_annexe) - stock_max;
            *commande -= surplus;
        }
        if (*delais_A == temp_commande_A)
        {
            *cout_total += *commande * prix;
        }
        else
        {
            *cout_total += (*commande * prix) + prix_commande; 
        }
        *delais_P = temp_commande_P;

    }
}