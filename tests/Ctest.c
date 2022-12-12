#include <stdio.h>

void sum(int nombre1, int nombre2, int *final)
{
    printf("je suis dans le fichier\n");
    *final = nombre1 + nombre2;
    // printf("id_final %d", final);
    // printf("*final %d", final);
}
void liste(int *list)
{
    printf("oui");
    // int i;
    // list[3] = 123;
    printf("modifié");
}
// gcc  -s -shared -O2 -o tests.dll -fPIC Ctest.c
