#!/usr/local/bin/python3
arquivo = open('pessoas.csv')


for registro in arquivo:
    print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))
    # Adicionando a função strip, para a remoção dos espaços e pulo de linha
arquivo.close()

