"""
This is a reST style.

:param param1: this is a first param
:param param2: this is a second param
:returns: this is a description of what is returned
:raises keyError: raises an exception
"""
from time import sleep
import os


colors = {
    'default': '\033[m',
    'white': '\033[37m',
    'red': '\033[31m',
    'green': '\033[32m',
    'black': '\033[39m'
}

background = {
    'white': '\033[40m',
    'red': '\033[41m',
    'green': '\033[42m',
    'blue': '\033[44m'
}

produtos = list()
usuários = list()

def linhas(cor, tipo, tamanho):
    """
    Função para printar linhas na tela.

    :param cor: Define a cor que a linha sera impressa (utilizar aspas duplas).
    :param tipo: Define o tipo de texto que a função ira utilizar como linha (utilizar aspas simples).
    :param tamanho: Define o tamanho da linha multiplicando o caracter inserido no parametro <tipo>.
    :returns: Sem return
    """
    print(f'{colors[cor]}# ', end='')
    print(f'{tipo}' * tamanho, end='')
    print(f' #{colors["default"]}')


def titulo_da_area(texto):
    print(f'\n{texto:^100}')


def carregamento_falso():
    """
    Função para criar uma sensação de falso carregamento no progama.

    :param ?: Não há params 
    :returns: Sem return
    """
    print('CARREGANDO', end='')
    for index in range(1, 4):
        sleep(0.5)
        print(f'.', end='')
        sleep(0.5)


def controle_de_estoque():
    while True:

        def painel_de_entrada(titulo_area):
            print('')
            linhas("red", '~~', 50)

            titulo_do_programa = 'OCG SISTEMAS - CONTROLE DE ESTOQUE'
            print(f'{colors["red"]}{titulo_do_programa:^100}{colors["default"]}')

            linhas("red", '~~', 50)

            titulo_da_area(titulo_area)
            linhas("white", '-', 100)
        painel_de_entrada('')

        def navegação():
            print(f'\n1 - CADASTRAR PRODUTOS'
                f'\n2 - VERIFICAR ESTOQUE'
                f'\n3 - EXCLUIR PRODUTO'
                f'\n4 - LISTA DE PEDIDOS'
                f'\n5 - CADASTRAR USUÁRIOS'
                f'\n6 - LISTA DE USUÁRIOS'
                f'\n7 - SAIR')
        navegação()
        
        while True:
            seleção = str(input('Selecione uma opção: '))
            continuar = ''

            if seleção == '1':
                os.system('cls')
                
                while True:
                    os.system('cls')
                    sleep(0.5)

                    # APAGAR ESTA LINHA APÓS IMPLEMENTAÇÃO ↓
                    # INCLUIR DATA DE CADASTRO, ALÉM DA HORA E MINUTO
                    painel_de_entrada('CADASTRAR PRODUTOS')
                    nome_produto = str(input(f'\n{"PRODUTO":.<16}: '))
                    código_produto = int(input(f'{"CÓDIGO":.<16}: '))
                    quantidade_produto = int(input(f'{"QUANTIDADE":.<16}: '))
                    data_entrega_produto = str(input(f'{"DATA DA ENTREGA":.<16}: '))
                    nota_fiscal_produto = int(input(f'{"NOTA FISCAL":.<16}: '))

                    produtos.append([{'produto': nome_produto}, 
                                     {'código': código_produto}, 
                                     {'quantidade': quantidade_produto}, 
                                     {'data de entrega': data_entrega_produto}, 
                                     {'nota fiscal': nota_fiscal_produto}])

                    print(produtos)
                    print(f'\n{colors["green"]}PRODUTO CADASTRADO COM SUCESSO!{colors["default"]}\n')

                    # 
                    #
                    # 
                    continuar = str(input('Cadastrar novo produto? [S/N]: ').upper().strip()[0])
                    
                    if continuar == 'N':
                        break
                    elif continuar == 'S':
                        continue
                    else:
                        while True:
                            print(f'{colors["red"]}OPÇÃO INVÁLIDA{colors["default"]}\n')
                            continuar = str(input('Cadastrar novo produto? [S/N]: ').upper().strip()[0])
                            if continuar not in 'SN':  # Continua no laço ELSE acima enquanto a resposta não for S ou N.
                                continue
                            elif continuar == 'S':  # Sai do laço do ELSE acima.
                                break
                            elif continuar == 'N':  # Sai do laço do ELSE acima.
                                break
                            break  # Não faço ideia, mas funcionou

                    # Sai do laço de cadastrar produtos.
                    if continuar == 'N':
                        break

                # Limpa o Terminal e quebra o laço de cadastro de produtos e faz o programa reiniciar.
                os.system('cls')
                break
                

            elif seleção == '2':
                os.system('cls')
                
#                while True:
                os.system('cls')
                sleep(0.5)

                painel_de_entrada('ESTOQUE')


            elif seleção == '3':
                print('u')
            elif seleção == '4':
                print('u')

            elif seleção == '5':
                os.system('cls')
                
                while True:
                    os.system('cls')
                    sleep(0.5)

                    # Definição destas variáveis logo aqui antes mesmo do input para que na hora do .append() tudo funcione corretamente. Apenas não será necessário mostrar na parte gráfica caso não contenha um valor diferente de '0'.
                    cpf_usuario = 0
                    cnpj_usuario = 0
                    # APAGAR ESTA LINHA APÓS IMPLEMENTAÇÃO ↓
                    # INCLUIR DATA DE CADASTRO, ALÉM DA HORA E MINUTO
                    painel_de_entrada('CADASTRAR USUÁRIO')
                    nome_usuario = str(input(f'\n{"NOME":.<16}: '))
                    código_usuario = int(input(f'{"CÓDIGO":.<16}: '))
                    tipo_de_usuario = str(input('Físico (CPF) ou Jurídico (CNPJ)? [F/J]: ').upper().strip()[0])

                    if tipo_de_usuario == 'F':
                        cpf_usuario =  str(input(f'{"CPF":.<16}: '))
                    elif tipo_de_usuario == 'J':
                        cnpj_usuario =  str(input(f'{"CNPJ":.<16}: '))
                    else:
                        while tipo_de_usuario not in 'FJ':
                            print(f'{colors["red"]}OPÇÃO INVÁLIDA{colors["default"]}\n')
                            tipo_de_usuario = str(input('Físico (CPF) ou Jurídico (CNPJ)? [F/J]: ').upper().strip()[0])

                        if tipo_de_usuario == 'F':
                            cpf_usuario =  str(input(f'{"CPF":.<16}: '))
                        elif tipo_de_usuario == 'J':
                            cnpj_usuario =  str(input(f'{"CNPJ":.<16}: '))

                    # CRIAR NESTA LINHA E ABAIXO UM VALIDADOR DE CPF. COLOCAR VÁRIAS ALTERNATIVAS, ELE SENDO APENAS NÚMEROS, CONTENDO PONTOS, HÍFEN, ETC. Fazer o mesmo após para CNPJ.

                    usuários.append([{'nome': nome_usuario}, 
                                     {'código': código_usuario}, 
                                     {'tipo': tipo_de_usuario}, 
                                     {'cpf': cpf_usuario}, 
                                     {'cnpj': cnpj_usuario}])

                    print(usuários)
                    print(f'\n{colors["green"]}USUÁRIO CADASTRADO COM SUCESSO!{colors["default"]}\n')
                    
                    # 
                    #
                    #
                    continuar = str(input('Cadastrar novo usuário? [S/N]: ').upper().strip()[0])
                    
                    if continuar == 'N':
                        break
                    elif continuar == 'S':
                        continue
                    else:
                        while True:
                            print(f'{colors["red"]}OPÇÃO INVÁLIDA{colors["default"]}\n')
                            continuar = str(input('Cadastrar novo usuário? [S/N]: ').upper().strip()[0])
                            if continuar not in 'SN':  # Continua no laço ELSE acima enquanto a resposta não for S ou N.
                                continue
                            elif continuar == 'S':  # Sai do laço do ELSE acima.
                                break
                            elif continuar == 'N':  # Sai do laço do ELSE acima.
                                break
                            break  # Não faço ideia, mas funcionou

                    # Sai do laço de cadastrar usuários.
                    if continuar == 'N':
                        break

                # Limpa o Terminal e quebra o laço de cadastro de usuários e faz o programa reiniciar.
                os.system('cls')
                break
                

            elif seleção == '6':
                print('u')

            elif seleção == '7':
                break
            else:
                print(f'{colors["red"]}OPÇÃO INVÁLIDA{colors["default"]}\n')

if __name__ == '__main__':

    os.system('cls')
    # Nome auto-explicativo. Utilizável para para dar um ar de maior complexidade, completo bullshit.
    carregamento_falso()
    # Limpa a tela após a execução do carregamento falso acima, para facilitar a utilização.
    os.system('cls')
    # Chamada do programa principal
    controle_de_estoque()
    # Limpa a tela após fim de execução do programa
    os.system('cls')