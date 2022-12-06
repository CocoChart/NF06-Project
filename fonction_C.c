#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

void calcul_seuil(int *tableau_vente, int *seuil, int nombre_de_mois, int temp_commande)
{
    int temp = 0;
    for (int i = 0; i < nombre_de_mois; i++)
    {
        temp += tableau_vente[i];
    }
    temp /= nombre_de_mois;
    *seuil = temp_commande * temp;
}

void reception(int* delais, int *stock, int *commande)
{
    printf("\nfonction reception\n");
    if (*delais == 0)
    { // reception commande
        printf("reception commande\n");
        *stock += *commande;
        *commande = 0;
    }
    printf("delais : %d ; commande : %d\n", *delais, *commande );
}

void passage_commande_compteur_mois(int *stock, int *delais, int *commande, int *nombre_commande, int temp_commande, int seuil, float *cout_total, float prix, float prix_commande)
{
    printf("SALUT le prix prix : %.2f\n", prix);
    printf("\nfonction passage_commande_compteur_mois\n");
    if (*stock <= seuil && *delais == 0)
    { // passage commande
        printf("passage commande\n");
        printf("prix : %.2f\n", prix);
        printf("prix_commande : %.2f\n", prix_commande);
        printf("cout_total : %.2f\n", *cout_total);
        *delais = temp_commande;
        *commande = (30 * (temp_commande+1) ) + (seuil - *stock);
        *nombre_commande += 1;
        *cout_total = *cout_total + ((*commande * prix) + prix_commande);
        printf("cout_total : %.2f\n", *cout_total);
        printf("commande : %d\n", *commande);
        printf("nombre de commande : %d\n", *nombre_commande);
    }
    if (*stock <= seuil)
    { // compteur mois
        printf("compteur mois\n");
        *delais -= 1;
    }
}

void vente_et_prix_stockage(int vente, int *stock, float *cout_stock, float prix_stockage)
{
    printf("\nfonction vente et cout stockage\n");
    *stock -= vente;
    *cout_stock += (*stock) * (prix_stockage);
}

// void testUnitaire(int stock)
// {
//     printf("bien rentré dans le fichier functions.dll\n");
//     printf("stock : %d\n", stock);
// }


void calcul(int *stock, int seuil, int *nombre_de_commande,int *taille_commande, int temp_commande, float prix, float prix_commande, float prix_stockage,float *cout_stock, float *cout_total)
{
    // test
    printf("dans functions_C\n");
    printf("stock : %d\n", *stock);
    printf("seuil : %d\n", seuil);
    printf("prix : %.2f\n", prix);
    printf("prix_commande : %.2f\n", prix_commande);
    printf("temp_commande : %d\n\n", temp_commande);
    printf("cout total : %.2f", *cout_total);

    int vente =0 ; 
    int commande = 0;
    int nombre_commande = 0;
    int delais = 0;
    for (int i = 0; i < 12; i++)
    {
        reception(&delais,stock,&commande);

        printf("stock : %d\n", *stock);
        printf("donner les ventes pour ce mois si :\n");
        scanf("%d", &vente);

        passage_commande_compteur_mois(stock, &delais, &commande, &nombre_commande, temp_commande, seuil, cout_total, prix, prix_commande);
        vente_et_prix_stockage(vente,stock, cout_stock, prix_stockage);
    }
    reception(&delais,stock,&commande);
    printf("voici la valeur de stock final : %d\n" ,*stock);
    printf("voici la valeur du cout de stockage : %.2f", *cout_stock );
    *cout_total += *cout_stock;
    printf("voici le cout total : %.2f\n", *cout_total);

    printf("\nFIN\n");

}





/*int oui(){

    printf("bonjour\n");
    int vente = 0;
    int stock = 0;
    int seuil = 90;
    int nombre_de_commande;
    int taille_commande;
    int delais;
    float prix_stock;
    float cout_total;
    float prix = 15;
    float prix_commande = 76;
    int commande;

    calcul(&stock,&seuil,&nombre_de_commande,&taille_commande,&delais,prix,prix_commande,&prix_stock,&cout_total);

}*/

// gcc  -s -shared -O2 -o fonction.dll -fPIC fonction_C.c
// gcc -fPIC -shared -o fonction.dll fonction_C.c   