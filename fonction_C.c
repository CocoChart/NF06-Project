#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

void calcul(int *stock,int *nombre_de_commande,int *seuil,int *vente,int *delais,int *commande,float *prix_stock,float *cout_total){

for (int numero_mois = 0; numero_mois<12; numero_mois++){
    
   
    if (*delais == 0){ //reception commande
        *stock += *commande;
        *commande = 0 ;}
     if (*stock <= *seuil && *delais == 0){ //passage commande
         *delais = 1;
         *commande = (5*3) + (*seuil - *stock);
         *nombre_de_commande ++;
         *cout_total += *commande*45 + 76;

    }
    printf("commande : %d\n", *commande);
    if (*stock <= *seuil ){ //compteur mois
     *delais --;
    }
    printf("delais : %d\n", *delais);

    printf("donner le nombre de vente de ce mois ci\n"); //vente 
    scanf("%d", vente);
    *stock -= *vente;

     //calcul prix stockage
        *prix_stock += *stock * 0.75;
    
    printf("valeur du stock : %d\n", *stock);
    printf ("nombre de commande : %d\n", *nombre_de_commande);
    printf("prix du stockage : %.2f\n\n", *prix_stock);

}
*cout_total += *prix_stock;
if (*delais == 0){ //reception commande
        *stock += *commande;
        *commande = 0 ;}

 printf("valeur du stock final : %d\n", *stock);
printf("cout total : %.2f\n", *cout_total);


}

void calcul_seuil(int* tableau_vente, int* seuil, int nombre_de_mois, int temp_commande){
    int temp = 0;
    for (int i = 0; i < nombre_de_mois; i++)
    {
        temp += tableau_vente[i];
    }
    temp /= nombre_de_mois ;
    *seuil = temp_commande*temp ;
}

void reception(int delais, int* stock, int* commande){
    printf("fonction reception\n");
    if (delais == 0){ //reception commande
        *stock += *commande;
        *commande = 0 ;}
}

void passage_commande_compteur_mois(int* stock, int *delais, int* commande,int* nombre_commande, int temp_commande, int seuil, float* cout_total, float prix, float prix_commande){
     printf("fonction passage_commande_compteru_mois\n");
    if (*stock <= seuil && *delais == 0){ //passage commande
         *delais = temp_commande;
         *commande = (5*3) + (seuil - *stock);
         *nombre_commande ++;
         *cout_total += *commande*prix + prix_commande;

        printf("commande : %d\n", *commande);
    }
    if (*stock <= seuil ){ //compteur mois
     *delais --;
    }
}

void vente_et_prix_stockage(int vente, int* stock, float* prix_stock, float* prix_stockage){
     printf("fonction vente et cout stockage\n");
    *stock -= vente;
    *prix_stock += (*stock) * (*prix_stockage);
}

// gcc -fPIC -shared -o fonction_C.so fonction.c