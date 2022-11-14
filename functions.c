#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

void calcul(int *stock,int *nombre_de_commande,int *seuil,int *vente,int *delais,int *commande,float *prix_stock,float *cout_total){

for (int i = 0; i<12; i++){
    
   
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

int main(){
int stock = 0;
int nombre_de_commande = 0;
int seuil = 0;
int vente = 0;
int delais = 0;
int commande = 0;
float prix_stock = 0;
float cout_total = 0;


    calcul( &stock, &nombre_de_commande, &seuil, &vente, &delais, &commande, &prix_stock,&cout_total);
    return 0;

}