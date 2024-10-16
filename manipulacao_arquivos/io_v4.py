#!/usr/local/bin/python3
# Nesse exemplo, vamos usar o try e finally para evitar erros, como o de esquecer de fechar o arquivo.

try:
    arquivo = open('pessoas.csv')

    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))
finally:
    arquivo.close()

