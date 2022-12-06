/*for (int numero_mois = 0; numero_mois < 12; numero_mois++)
    {

            if (*delais == 0)
        { // reception commande
            *stock += *taille_commande;
            *taille_commande = 0;
        }
        if (*stock <= *seuil && *delais == 0)
        { // passage commande
            *delais = 1;
            *taille_commande = (5 * 3) + (*seuil - *stock);
            *nombre_de_commande++;
            *cout_total += *taille_commande * 45 + 76;
        }
        printf("commande : %d\n", *taille_commande);
        if (*stock <= *seuil)
        { // compteur mois
            *delais--;
        }
        printf("delais : %d\n", *delais);

        printf("donner le nombre de vente de ce mois ci\n"); // vente
        scanf("%d", vente);
        *stock -= *vente;

        // calcul prix stockage
        *prix_stock += *stock * 0.75;

        printf("valeur du stock : %d\n", *stock);
        printf("nombre de commande : %d\n", *nombre_de_commande);
        printf("prix du stockage : %.2f\n\n", *prix_stock);
    }
    *cout_total += *prix_stock;
    if (*delais == 0)
    { // reception commande
        *stock += *taille_commande;
        *taille_commande = 0;
    }*/