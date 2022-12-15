#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
/**
 * \file fonction_C.c
 * \brief Pour compiler en DLL : gcc  -s -shared -O2 -o functions.dll -fPIC fonction_C.c
 * \author Corentin CHARTIER & Maël JAVER KALA
 */
void reception(int *delais_principal, int *stock_Principal, int *commande) /// Fonction qui vérifie si une commande est arrivée et ajuste les stock en conséquence
{
    // printf("\nReception\n");
    if (*delais_principal == 0) ///- Vérifie si le délais de livraison est nul, cette condition est vérifier quand une commande viens d'arriver ou quand il n'y a pas de commande en cour
    {
        *stock_Principal += *commande; ///- Incrémente le stock de la valeur de la commande
        *commande = 0;                 ///- Remet la valeur du stock à 0 pour éviter d'augmenter plusieurs fois le stock avec la même commande
    }
    // printf("Stock C :%d\n", *stock_Principal);
}


    
void passage_de_mois( int *stock_principal,int *stock_annexe, int seuil_P, int seuil_A, int *compteur_mois, int* delais_P, int* delais_A)
{
    // printf("delais %d\n", *delais_P);
    // if (*stock_principal <= seuil_P) ///- Vérifie si une commande est en cours pour le produit traité
    
        *delais_P -= 1;
         // Diminue le délais de livraison, simulant le passage d'un mois
    
     ///- Vérifie si une commande est en cours pour l'autre produit
    
        *delais_A -= 1; ///- Diminue les délais de livraison, simulant le passage d'un mois
    
    *compteur_mois += 1;
    // printf("\ncompteur mois : %d\n", *compteur_mois);
}

void vente_et_prix_stockage(int vente, int *stock_P, float *cout_stock, float prix, float prix_stockage, float *cout_rupture, float *cout_total)
/// Fonction qui diminue le stock du montant de la vente, vérifie si il y a rupture de stock et calcule le prix de stockage des produits restants
{
    // printf("vente et prix stockage\n");
    *stock_P -= vente; //- Diminue les stock
    // printf("Stock apres vente :%d\n", *stock_P);
    if (*stock_P < 0) //- */érifie si il y a une rupture de stock
    {
        printf("      Cout de RUPTURE  : %.2f\n", prix * 0.1 * abs(*stock_P) );
        *cout_rupture += prix * 0.1 * abs(*stock_P); ///- Incrémente le coût total du coût de rupture
        *stock_P = 0;                              ///- Remet le stock à 0 car on ne peut pas avoir de stock négatif
        printf("      RUPTURE DE STOCK\n");
    }
    *cout_stock += (*stock_P) * (prix_stockage); ///- Calcule le cout de stockage des produit restant dans l'entrepot
}

//----------------------------------------------------------------------- Gestion à point de commande -----------------------------------------------------------------------------------


void passage_commande_PC(int *stock_principal, int *stock_annexe, int stock_max, int *delais_P, int *delais_A, int *commande, int *nombre_commande, int temp_commande_P,int temp_commande_A, int Vmoyenne, int seuil, float *cout_total, float prix, float prix_commande)
{ // Fonction qui vérifie les stocks, passe une commande si besoin et actualise le delais de livraison
    // printf("passage de commande et compteur mois\n");
    if (*stock_principal <= seuil && *commande == 0) // vériie si les stock sont en dessous du seuil et qu'aucune commande n'est déjà en cours. si ces conditions sont vérifié alors on passe une nouvlle commande
    {
        *commande = (Vmoyenne * (temp_commande_P + 2)) + (seuil - *stock_principal);  // passe commande du nombre de produit déterminé par calcul pour limiter les stock et éviter les ruptures
        *nombre_commande += 1;
        if (*stock_principal + *commande + *stock_annexe > stock_max) 
        {
            int surplut;
            surplut = (*stock_principal + *commande + *stock_annexe) - stock_max;
            *commande -= surplut;
        }
        if (*delais_A == temp_commande_A)
        {
            *cout_total += *commande * prix;
        } 
        else
        {
            
            *cout_total +=(*commande * prix) + prix_commande; // incrémente les cout totaux du prix de la commande
        }
        *delais_P = temp_commande_P;      // incrémente le delais de livraison du temp de livraison determiné par le produit concerné
    }
}
// ---------------------------------------------------------------- Gestion Périodique --------------------------------------------------------------------------------


void passage_commande_P(int *stock_principal, int *stock_annexe, int stock_max,int compteur_mois, int cycle, int *delais_P, int *delais_A, int *commande, int *nombre_commande, int temp_commande_P,int temp_commande_A, int seuil_max, float *cout_total, float prix, float prix_commande)
 {  
    //  printf("compteur mois  : %d\n", compteur_mois+1);
    // printf("cycle : %d\n", cycle);
    // printf("*compteur_mois modulo temp_actualisation == %d\n",(compteur_mois % cycle) );
    if (compteur_mois % cycle == 0 && *stock_principal < seuil_max)
    {
        // printf("seuil max : %d\n", seuil_max);
        // printf("stock : %d\n", *stock_principal);
        *commande = seuil_max - *stock_principal ;
        // printf("commande : %d\n", *commande);
    
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
            *cout_total +=(*commande * prix) + prix_commande; // incrémente les cout totaux du prix de la commande
        }
        *delais_P = temp_commande_P;
    }
}