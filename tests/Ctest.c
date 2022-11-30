#include <stdio.h>

void sum(int nombre1, int nombre2, int* final)
{
    printf("je suis dans le fichier\n");
    *final = nombre1 + nombre2;
   // printf("id_final %d", final);
   // printf("*final %d", final);
}

// gcc -fPIC -shared -o libsum.so Ctest.c
