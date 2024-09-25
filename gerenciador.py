import csv
import os

campos = ['ID','nome', 'categoria','quantidade', 'valor']
file_name = 'arquivo.csv'

#funções para gerenciar e atualizar o csv

def criar_csv():
        with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=campos)
            writer.writeheader()

def carregar_produtos():
    if not os.path.exists(file_name):
        criar_csv()  # Cria o CSV se não existir
        return []
    with open(file_name, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        produtos = []
        for linha in reader:
            produto = {
                'ID': int(linha['ID']),
                'nome': linha['nome'],
                'categoria': linha['categoria'],
                'quantidade': int(linha['quantidade']),
                'valor': float(linha['valor'])
            }
            produtos.append(produto)
        return produtos  


def salvar_produtos(produtos):
    with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=campos)
        writer.writeheader()
        writer.writerows(produtos)


 
