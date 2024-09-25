from funcoes import os
import funcoes
from gerenciador import carregar_produtos


produtos = []

def menu ():
    try:
        
        print('[1] - Adicionar Produto')
        print('[2] - Listar Produto')
        print('[3] - Remover Produto')
        print('[4] - Alterar Produto')
        print('[5] - Procutar Produto')
        print('[6] - Tamanho')
        print('[0] - Sair')
        opcao = int(input('Digite a opção desejada: '))
        if opcao < 0 or opcao > 6:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Erro! Digite um valor válido.')
            return None
        return opcao
    except ValueError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Erro! Entrada inválida. Certifique-se de digitar um número.')
        return None

opcao = 1

while opcao != 0:
    opcao = menu()

    if opcao is None:
        continue

    if opcao == 1:
        funcoes.cadastrar_produto()
    elif opcao == 2:
        funcoes.listar_produto()
    elif opcao == 3:
        funcoes.remover_produto()
    elif opcao == 4:
        funcoes.alterar_produto()
    elif opcao == 5:
        funcoes.procurar_produto()
    elif opcao == 6:
        funcoes.tamanho()
    elif opcao == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Obrigado! Saindo do sistema...')
        break
    
    

    
    
    
    
