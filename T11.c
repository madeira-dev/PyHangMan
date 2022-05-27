// 33C Juliana Pinheiro 2110516
#include <stdio.h>
#include <stdlib.h>
#define TAM 80

struct medidas
{
    float cintura;
    float quadril;
};
typedef struct medidas Medidas;

struct cliente
{
    char nome[TAM];
    int identificacao;
    char genero;
    Medidas med;
};
typedef struct cliente Cliente;

FILE *openfile(const char *file, const char *mode)
{
    FILE *arq;
    arq = fopen(file, mode);
    if (arq == NULL)
    {
        printf("Nao foi possivel abrir o arquivo");
        return NULL;
    }
    return arq;
}

void leGravaArquivo(Cliente *cli)
{
    Cliente *vetor_cli[5];
    int i, linhas;
    FILE *txt_file, *bin_file;

    for (i = 0; i < 5; i++)
    {
        vetor_cli[i] = (Cliente *)malloc(sizeof(Cliente));
    }

    txt_file = openfile("clientes.txt", "r");
    bin_file = openfile("clientes.dat", "wb");

    fscanf(txt_file, "%d", &linhas);

    cli = (Cliente *)malloc(sizeof(Cliente));
    if (cli == NULL)
    {
        printf("Memoria insuficiente");
        exit(1);
    }

    for (i = 0; i < linhas; i++)
    {
        fscanf(txt_file, "%s %d %c %f %f", cli->nome, &cli->identificacao, &cli->genero, &cli->med.cintura, &cli->med.quadril);
        fwrite(&linhas, sizeof(int), 1, bin_file);
        fwrite(vetor_cli[i]->nome, sizeof(char), TAM, bin_file);
        fwrite(&vetor_cli[i]->identificacao, sizeof(int), 1, bin_file);
        fwrite(&vetor_cli[i]->genero, sizeof(char), 1, bin_file);
        fwrite(&vetor_cli[i]->med.cintura, sizeof(float), 1, bin_file);
        fwrite(&vetor_cli[i]->med.quadril, sizeof(char), TAM, bin_file);
    }

    fread(&linhas, sizeof(int), 1, bin_file);

    for (i = 0; i < linhas; i++)
    {
        fread(cli->nome, sizeof(char), TAM, bin_file);
        fread(&cli->identificacao, sizeof(int), 1, bin_file);
        fread(&cli->genero, sizeof(char), 1, bin_file);
        fread(&cli->med.cintura, sizeof(float), 1, bin_file);
        fread(&cli->med.quadril, sizeof(char), TAM, bin_file);
        printf("%s %d %c %.2f %.2f\n", cli->nome, cli->identificacao, cli->genero, cli->med.cintura, cli->med.quadril);
    }

    fclose(txt_file);
    fclose(bin_file);
    free(cli);

    return;
}

int main(void)
{
    Cliente *cli;
    leGravaArquivo(cli);
    return 0;
}
