#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

void reception(int* delais, int *stock, int *commande) // Fonction qui vérifie si une commande est arrivé et ajuste les stock en conséquence
{
    printf("\nrecepetion\n");
    if (*delais == 0) // Vérifie si le délais de livraison est nul, cette condition est vérifier quand une commande viens d'arriver ou quand il n'y a pas de commande en cour 
    { 
        *stock += *commande; // incrémente le stock de la valeur de la commande
        *commande = 0; // remet la valeur du stock à 0 pour éviter d'augmenter plusieurs fois le stock avec la même commande
    }
    
}
void passage_commande_compteur_mois(int *stock, int *delais, int *commande, int *nombre_commande, int temp_commande, int seuil, float *cout_total, float prix, float prix_commande)
{ // Fonction qui vérifie les stocks, passe une commande si besoin et actualise le delais de livraison 
    printf("passage de commande et compteur mois\n");
    if (*stock <= seuil && *delais == 0) // vériie si les stock sont en dessous du seuil et qu'aucune commande n'est déjà en cours. si ces conditions sont vérifié alors on passe une nouvlle commande
    { 
        *delais = temp_commande; // incrémente le delais de livraison du temp de livraison determiné par le produit concerné
        *commande = ( 7 * 2 ) + (seuil - *stock); // passe commande du nombre de produit déterminé par calcul pour limiter les stock et éviter les ruptures
        *nombre_commande += 1; // garde une trace du nombre de commande effectué 
        *cout_total = *cout_total + ((*commande * prix) + prix_commande); // incrémente les cout totaux du prix de la commande
    }
    if (*stock <= seuil) // vérifie si une commande est en cours
    { 
        *delais -= 1; // diminue le delais de livraison, simulant le passage d'un mois
    }
}

void vente_et_prix_stockage(int vente, int *stock, float *cout_stock, float prix, float prix_stockage, float* cout_total)
// Fonction qui diminue le stock du montant de la vente, vérifie si il y a rupture de stock et calcul le prix de stockage des produits restants
{
    printf("vente et prix stockage\n");
    *stock -= vente; // diminue les stock 
    if (*stock < 0 ) // vérifie si il y a une rupture de stock
    {
        *cout_total += prix * 0.1 * abs(*stock); // incrémente le cout total du cout de rupture
        *stock = 0; // remet le stock à 0 car on ne peut pas avoir de stock négatif 
    }
    *cout_stock += (*stock) * (prix_stockage); // calcul le cout de stockage des produit restant dans l'entrepot
}


void calcul(int *stock, int seuil, int *nombre_de_commande,int *taille_commande, int temp_commande, float prix, float prix_commande, float prix_stockage,float *cout_stock, float *cout_total)
// fonction général executant le programme pour 12 mois et affiche les résultats
{
    printf("stock : %d\n", *stock);
    printf("seuil : %d\n", seuil);
    printf("prix : %.2f\n", prix);
    printf("prix_commande : %.2f\n", prix_commande);
    printf("temp_commande : %d\n\n", temp_commande);
    printf("cout total : %.2f\n", *cout_total);

    int vente =0 ; 
    int commande = 0;
    int nombre_commande = 0;
    int delais = 0;
    for (int i = 0; i < 12; i++)
    {
        // les fonctions doivent être appelées dans le bon ordre afin de simuler le déroulement d'un mois. les fonction représentent les actions suivante :
            // en début de mois, on vérifie si une commande est arrivé et on la prend en compte dans le stock
            // On vérifie si le nouveau stock est suffisant, si non on passe une nouvelle commande
            // On diminue le delais de livraison pour simuler le passage du mois
            // On diminue les stocks du montant des ventes effectuées durant le mois
            // On calcul le prix de stockage des produits restés dans l'entrepot pendant ce mois 
        reception(&delais,stock,&commande);
        printf("donner les ventes pour ce mois si :\n");
        scanf("%d", &vente);

        passage_commande_compteur_mois(stock, &delais, &commande, &nombre_commande, temp_commande, seuil, cout_total, prix, prix_commande);
        vente_et_prix_stockage(vente,stock, cout_stock,prix, prix_stockage, cout_total);
    }
    reception(&delais,stock,&commande); // on vérifie une dernière fois si une commande est en cours. Cela correspond à une potentiel commande passé en décembre et qui n'arriverais que début janvier
    // on affiche les différentes valeurs de cout et le stock maximal atteint pendant l'année
    printf("voici la valeur de stock final : %d\n" ,*stock);
    printf("voici la valeur du cout de stockage : %.2f\n", *cout_stock );
    *cout_total += *cout_stock;
    printf("voici le cout total : %.2f\n", *cout_total);

    printf("\nFIN\n");

}
