#include <stdio.h>
#include <stdlib.h>
#define TAM 80

typedef struct _medidas
{
    float cintura;
    float quadril;
} Medidas;

typedef struct _cliente
{
    char nome[TAM];
    int identificacao;
    char genero;
    Medidas med;
} Cliente;

void read_txt(Cliente **vetor_clientes, int linhas);
// void write_bin(Cliente **vetor_clientes, int linhas);
// void read_bin(Cliente **vetor_clientes, int linhas);

int main(void)
{
    Cliente **vetor_clientes = NULL;
    int linhas = 0;

    read_txt(vetor_clientes, linhas);
    // write_bin(vetor_clientes, linhas);
    // read_bin(vetor_clientes, linhas);

    return 0;
}

void read_txt(Cliente **vetor_clientes, int linhas)
{
    int i;
    int linhas_final;
    FILE *txt_file, *bin_file;
    FILE *bin_finale;

    txt_file = fopen("clientes.txt", "r");
    bin_file = fopen("clientes.dat", "wb");

    fscanf(txt_file, "%d", &linhas);

    vetor_clientes = (Cliente **)malloc(sizeof(Cliente *) * linhas);

    for (i = 0; i < linhas; i++)
    {
        vetor_clientes[i] = (Cliente *)malloc(sizeof(Cliente));
    }

    for (i = 0; i < linhas; i++)
    {
        fscanf(txt_file, "%s %d %c %f %f", vetor_clientes[i]->nome, &vetor_clientes[i]->identificacao, &vetor_clientes[i]->genero, &vetor_clientes[i]->med.cintura, &vetor_clientes[i]->med.quadril);
    }

    // debug
    printf("vetor_clientes do txt: \n");
    for (i = 0; i < linhas; i++)
    {
        printf("vetor_clientes: %s %d %c %f %f\n", vetor_clientes[i]->nome, vetor_clientes[i]->identificacao, vetor_clientes[i]->genero, vetor_clientes[i]->med.cintura, vetor_clientes[i]->med.quadril);
    }
    // fim debug

    printf("\n\n");

    fwrite(vetor_clientes, sizeof(Cliente), linhas, bin_file);

    bin_finale = fopen("clientes.dat", "rb");

    fread(&linhas_final, sizeof(int), 1, bin_finale);

    fread(vetor_clientes, sizeof(Cliente), linhas, bin_finale);

    // debug
    printf("vetor_clientes do bin: \n");
    for (int i = 0; i < linhas; i++)
    {
        printf("vetor_clientes: %s %d %c %f %f\n", vetor_clientes[i]->nome, vetor_clientes[i]->identificacao, vetor_clientes[i]->genero, vetor_clientes[i]->med.cintura, vetor_clientes[i]->med.quadril);
    }
    // fim debug

    fclose(bin_file);
    fclose(txt_file);
    fclose(bin_finale);
}

// void write_bin(Cliente **vetor_clientes, int linhas);
// void read_bin(Cliente **vetor_clientes, int linhas);