#!/usr/local/bin/python3
# Nesta versão, não precisamos abrir o arquivo ler e depois fechar, como foi no primeiro
arquivo = open('pessoas.csv')

for registro in arquivo:
    print('Nome: {}, Idade: {}'.format(*(registro.split(','))))
arquivo.close()
