import os
from gerenciador import salvar_produtos, carregar_produtos
# produto = ['ID','nome', 'categoria','quantidade', 'valor']

produtos = carregar_produtos()
#função para cadastrar o produto
def cadastrar_produto():
    try:
        id = int(input('Digite o ID do Produto: '))
        nome = input('Digite o nome do produto: ')
        categoria = input('Informe a Categoria que o produto se adequa: ')
        quantidade  = int(input('Informe a quantidade de produto disponível: '))
        valor = float(input('Informe o valor do produto R$: '))
    
        #verifica se a quantidade e o valor são não negativos
        if quantidade<0 or valor<0:
            print('Erro! Quantidade e valor devem ser não negativos.')
            return 0

        #verifica se o nome ou categoria não estão vazio
        if not nome or not categoria:
            print('Erro! Nome e categoria não podem estar vazio')
            return 0

        #verifica se o produto já existe
        for produto in produtos:
            if produto['ID'] == id:
                print(f'Produto de cód:{id} já cadastrado!')
                res = input('Deseja incrementar na quantidade do produto? [S]/[N]: ').lower()
                if res == 's':
                    produto['quantidade'] += quantidade
                    salvar_produtos(produtos)
                    print('Quantidade incrementada com sucesso!')
                else:
                    print('quantidade não foi alterada.')
                return 1



        #se o produto não existe, cria o dicionário do produto
        novo_produto = {'ID': id, 'nome': nome,'quantidade':quantidade, 'categoria':categoria, 'valor':valor}
        #adiciona o produto a lista de produtos global
        produtos.append(novo_produto)
        salvar_produtos(produtos)
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Produto cadastrado com sucesso!')
        return 1 #retorna 1 sempre que o produto é adicionado
    
    except ValueError:
        print('Erro! Entrada inválida. certifique-se de digitar números para ID, quantidade e valor.')
        return 0 

#Função para listar produtos com filtros
def listar_produto():
    
    if len(produtos) == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Erro! A lista encontra-se vazia.')
        print('Adicione um produto a lista e tente novamente!')
        return
    
    while True:
        print('[T] - Listar todos itens')
        print('[I] - Listar pelo ID')
        print('[C] - Listar pela categoria')
        print('[V] - listar pelo Valor')
        res = input('Digite a opção [*] desejada: ').upper()

        if res in ['I', 'C', 'V', 'T']:
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Opção invalida! Tente com a opção correta.')
            continue
        
    # listar todos os produtos da lista
    if res == 'T':
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{'ID':<10}{'Nome':<25}{'Quantidade':<15}{'Categoria':<20}{'Valor (R$)':>15}")
        print('-' * 85)
        for produto in produtos: 
                print(f"{produto['ID']:<10}{produto['nome']:<25}{produto['quantidade']:<15}{produto['categoria']:<20}{produto['valor']:>15.2f}")

    # listar pelo ID do produto.
    elif res == 'I':
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            id = int(input('Informe o id do produto que deseja procurar: '))
        except ValueError:
            print('Erro! ID inválido. Certifique-se de digitar um número.')
            return
        
        print(f"{'ID':<10}{'Nome':<25}{'Quantidade':<15}{'Categoria':<20}{'Valor (R$)':>15}")
        print('-' * 85)
        encontrado = False
        for produto in produtos: 
            if produto['ID'] == id:
                print(f"{produto['ID']:<10}{produto['nome']:<25}{produto['quantidade']:<15}{produto['categoria']:<20}{produto['valor']:>15.2f}")
                encontrado = True
                break
        if not encontrado:
            print(f'Erro! Produto com o {id} não Cadastrado')

    # listar pela categoria
    elif res == 'C':
        os.system('cls' if os.name == 'nt' else 'clear')
        categoria = input('Informe a categoria do produto a ser listada: ')
        print(f"{'ID':<10}{'Nome':<25}{'Quantidade':<15}{'Categoria':<20}{'Valor (R$)':>15}")
        print('-' * 85)
        encontrados = False
        for produto in produtos:
            if produto['categoria'].lower() == categoria.lower():
                print(f"{produto['ID']:<10}{produto['nome']:<25}{produto['quantidade']:<15}{produto['categoria']:<20}{produto['valor']:>15.2f}")
                encontrados = True
        if not encontrados:
            print(f'Erro! Não existe produto cadastrado na categoria {categoria}')
    
    # listar pelo valor
    elif res == 'V':
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            valor_max = float(input('Informe o valor maximo dos produtos a serem listado: '))
        except ValueError:
            print('Erro! Valor inválido. Certifique-se de digitar um número.')
            return
        
        print()
        print(f"{'ID':<10}{'Nome':<25}{'Quantidade':<15}{'Categoria':<20}{'Valor (R$)':>15}")
        print('-' * 85)
        encontrados = False
        for produto in produtos:
            if produto['valor'] <= valor_max:
                print(f"{produto['ID']:<10}{produto['nome']:<25}{produto['quantidade']:<15}{produto['categoria']:<20}{produto['valor']:>15.2f}")
                encontrados = True
        if not encontrados:
            print(f'Erro! Nenhum produto a ser listado com valor até R$ {valor_max:.2f}')

# Função para remover produto da lista
def remover_produto():
    
    if len(produtos) == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Erro! A lista encontra-se vazia.')
        print('Adicione um produto a lista e tente novamente!')
        return
    
    try:
        remover = int(input('Escreva o ID do produto a ser removido: '))
    except ValueError:
        print('Erro! Entrada inválida. Certifique-se de digitar um número para o ID')
    
    encontrados = False
    for produto in produtos:
        if produto['ID'] == remover:
            produtos.remove(produto)
            os.system('cls' if os.name == 'nt' else 'clear')
            salvar_produtos(produtos)
            print(f'Produto "{produto['nome']}" (ID: {remover}) removido com sucesso!')
            encontrados = True
            break
        
    if not encontrados:
        print(f'Erro! Produto "{remover}" não cadastrado')
        return 0

    return 1

# Função para alterar o poduto
def alterar_produto():
    
    if len(produtos) == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Erro! A lista encontra-se vazia.')
        print('Adicione um produto a lista e tente novamente!')
        return
    
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        mudar = int(input('Informe o ID do produto a ser alterado: '))
    except ValueError:
        print('Erro! ID inválido. Certifique-se de digitar um número.')
        return
        
    encontrado = False
    for produto in produtos:
        if produto['ID'] == mudar:
            while True:
                print('O que deseja alterar?',
                    '[1] - Nome',
                    '[2] - Categoria',
                    '[3] - Quantidade',
                    '[4] - Valor',
                    '[0] - Cancelar', sep= '\n'
                    )
                opcao = input('Informe a opção desejada: ')
                if opcao in ['1', '2', '3', '4','0']:
                    break
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('Opção invalida! Tente com a opção correta.')
                    continue

            if opcao == '1':
                novo_nome = input('Informe o novo Nome do produto: ')
                produto['nome'] = novo_nome
                print(f'Nome alterado para: {novo_nome}')
            elif opcao == '2':
                nova_categoria = input('Informe a nova Categoria do produto: ')
                produto['categoria'] = nova_categoria
                print(f'Categoria alterada para: {nova_categoria}')
            elif opcao == '3':
                try:
                    nova_qtd = int(input('Informe a nova quantidade do produto: '))
                    if nova_qtd <0:
                        print('Erro! O valor não pode ser negativo.')
                        return
                    produto['quantidade'] = nova_qtd
                    print(f'Quantidade alterada para: {nova_qtd}')
                except ValueError:
                    print('Erro! ID inválido. Certifique-se de digitar um número.')
                    return
                
            elif opcao == '4':
                try:    
                    novo_valor=float(input('Informe o novo valor R$ do produto: '))
                    if novo_valor<0:
                        print('Erro! O valor não pode ser negativo.')
                        return
                    produto['valor'] = novo_valor
                    print(f'Valor alterado para: R$ {novo_valor:.2f}')
                except ValueError:
                    print('Erro! ID inválido. Certifique-se de digitar um número.')
                    return
            elif opcao == '0':
                print('Opção cancelada.')
                return
            
            salvar_produtos(produtos)
            encontrado = True

    if not encontrado:
        print(f'Erro! Produto com ID {mudar} não cadastrado.')

#função para procurar a posição do produto na lista
def procurar_produto():
    if len(produtos) == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Erro! A lista encontra-se vazia.')
        print('Adicione um produto a lista e tente novamente!')
        return -1
    try:    
        procurar = int(input('Informe o ID do produto a ser procurado: '))
    except ValueError:
        print('Erro! ID inválido. Certifique-se de digitar um numero.')
        return -1
    
    encontrado = False
    for produto in produtos:
        if produto['ID'] == procurar:
            posicao = (produtos.index(produto)+1)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'O produto "{produto["nome"]}" (ID: {procurar}) está na posição {posicao} da lista.')
            encontrado = True
            return(posicao)
    
    if not encontrado:
        print(f'Erro! produto com ID {procurar} não encontrado')
        return -1

def tamanho():
    if len(produtos) == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Ainda não há produtos cadastados.')
    else:
        print(f'O número total de produtos é: {len(produtos)}')
    return len(produtos)
    

