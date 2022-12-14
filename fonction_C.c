#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

/// Pour compiler en DLL : gcc  -s -shared -O2 -o functions.dll -fPIC fonction_C.c

void reception(int *delais_principal, int *stock_Principal, int *commande) // Fonction qui vérifie si une commande est arrivée et ajuste les stock en conséquence
{
    // printf("\nReception\n");
    if (*delais_principal == 0) // Vérifie si le délais de livraison est nul, cette condition est vérifier quand une commande viens d'arriver ou quand il n'y a pas de commande en cour
    {
        *stock_Principal += *commande; // incrémente le stock de la valeur de la commande
        *commande = 0;       // remet la valeur du stock à 0 pour éviter d'augmenter plusieurs fois le stock avec la même commande
    }
    // printf("Stock C :%d\n", *stock);
}
void passage_commande_compteur_mois(int *stock_principal, int *stock_annexe, int stock_max, int *delais_P, int *delais_A, int *commande, int *nombre_commande, int temp_commande_P,int temp_commande_A, int Vmoyenne, int seuil, float *cout_total, float prix, float prix_commande)
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
    
    
    
    if (*stock_principal <= seuil) // Vérifie si une commande est en cours
    {
        *delais_P -= 1; // Diminue le délais de livraison, simulant le passage d'un mois
    }
}

void vente_et_prix_stockage(int vente, int *stock_X, float *cout_stock, float prix, float prix_stockage, float *cout_total)
// Fonction qui diminue le stock du montant de la vente, vérifie si il y a rupture de stock et calcule le prix de stockage des produits restants
{
    // printf("vente et prix stockage\n");
    *stock_X -= vente; // diminue les stock
    // printf("Stock apres vente :%d\n", *stock);
    if (*stock_X < 0) // vérifie si il y a une rupture de stock
    {
        *cout_total += prix * 0.1 * abs(*stock_X); // Incrémente le coût total du coût de rupture
        *stock_X = 0;                              // Remet le stock à 0 car on ne peut pas avoir de stock négatif
        printf("RUPTURE DE STOCK\n");
    }
    *cout_stock += (*stock_X) * (prix_stockage); // Calcule le cout de stockage des produit restant dans l'entrepot
}

// void calcul(int *stock_X, int *stock_Y, int stock_max, int Vmoyenne, int seuil, int *nombre_de_commande, int *taille_commande, int temp_commande_P, int temp_commande_A, float prix, float prix_commande, float prix_stockage, float *cout_stock, float *cout_total)
// // Fonction générale executant le programme pour 12 mois et affiche les résultats
// {
//     printf("stock : %d\n", *stock_X);
//     printf("seuil : %d\n", seuil);
//     printf("prix : %.2f\n", prix);
//     printf("prix_commande : %.2f\n", prix_commande);
//     printf("temp_commande : %d\n\n", temp_commande_P);
//     printf("cout total : %.2f\n", *cout_total);

//     int vente = 0;
//     int commande = 0;
//     int nombre_commande = 0;
//     int delais = 0;
//     for (int i = 0; i < 12; i++)
//     {
//         // Les fonctions doivent être appelées dans le bon ordre afin de simuler le déroulement d'un mois. les fonction représentent les actions suivante :
//         // En début de mois, on vérifie si une commande est arrivé et on la prend en compte dans le stock
//         // On vérifie si le nouveau stock est suffisant, si non on passe une nouvelle commande
//         // On diminue le delais de livraison pour simuler le passage du mois
//         // On diminue les stocks du montant des ventes effectuées durant le mois
//         // On calcul le prix de stockage des produits restés dans l'entrepot pendant ce mois
//         reception(&delais, stock_X, &commande);
//         printf("donner les ventes pour ce mois si :\n");
//         scanf("%d", &vente);

//         passage_commande_compteur_mois(stock_X, stock_Y, &stock_max,  &delais, &commande, &nombre_commande, temp_commande_P,temp_commande_A, Vmoyenne, seuil, cout_total, prix, prix_commande);
//         vente_et_prix_stockage(vente, stock_X, cout_stock, prix, prix_stockage, cout_total);
//     }
//     reception(&delais, stock_X, &commande); // on vérifie une dernière fois si une commande est en cours. Cela correspond à une potentiel commande passé en décembre et qui n'arriverais que début janvier
//     // on affiche les différentes valeurs de cout et le stock maximal atteint pendant l'année
//     printf("voici la valeur de stock final : %d\n", *stock_X);
//     printf("voici la valeur du cout de stockage : %.2f\n", *cout_stock);
//     *cout_total += *cout_stock;
//     printf("voici le cout total : %.2f\n", *cout_total);

//     printf("\nFIN\n");
// }
