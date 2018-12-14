"""
This is a reST style.

:param param1: this is a first param
:param param2: this is a second param
:returns: this is a description of what is returned
:raises keyError: raises an exception
"""

# IMPLEMENTAR QUE, CASO 'ESC' SEJA PRESSIONADO, VOLTAR AO MENU PRINCIPAL DE SELEÇÃO.
# IMPLEMENTAR NO "DATA ENTREGA" QUE APÓS DIGITAR DOIS NÚMEROS ELE AUTOMATICAMENTE INSERE UMA BARRA.
# IMPLEMENTAR MÁXIMO DE CARACTERES EM CADA INPUT TANTO DE <PRODUTOS>, QUANTO DE <USUARIOS>.
# IMPLEMENTAR TRY & EXCEPT EM TODAS PARTES PASSIVEIS DE ERRO DO USUÁRIO NA EXECUÇÃO.
# MUDAR OS QUERIES DO BANCO DE DADOS QUE ESTÃO TODOS EM ~~VARCHAR~~ no <gerar_databse.py>.
# APÓS ESTIVER TUDO PRONTO, FAZER COM QUE O GERAMENTO DO BANCO DE DADOS FUNCIONE DENTRO DESTE ARQUIVO, E NÃO EM UM SEPARADO.
# IMPLEMENTAR NO 'ID' DE DELETAR PRODUTOS QUE ELE TAMBÉM FUNCIONE DE FATO COM O CÓDIGO DO PRODUTO, AMBOS JUNTOS NO MESMO INPUT.

from time import sleep
from datetime import datetime

import os
import keyboard
import psycopg2

'''Atribui os comandos de conexão para a variável <connection> ↓
    host='' É o host da database, neste caso é localhost (local). 
    database='' É o nome que daremos para o banco de dados, no caso, 'produtos'.
    user='' É o usuário responsável pela aquela database.
    password='' É a senha do user='' para acessar a database.'''

connection_produtos = psycopg2.connect(host='localhost', 
                                       database='produtos', 
                                       user='postgres', 
                                       password='')
connection_usuarios = psycopg2.connect(host='localhost', 
                                       database='usuarios', 
                                       user='postgres', 
                                       password='')

'''Não sei'''
cursor_produtos = connection_produtos.cursor()
cursor_usuarios = connection_usuarios.cursor()

sql_produtos = ''
sql_usuarios = ''

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
    seleção = ''
    while True:
        os.system('cls')

        def painel_de_entrada(titulo_area):
            print('')
            linhas("red", '~', 140)

            titulo_do_programa = 'OCG SISTEMAS - CONTROLE DE ESTOQUE'
            print(f'{colors["red"]}{titulo_do_programa:^140}{colors["default"]}')

            linhas("red", '~', 140)

            titulo_da_area(f'{titulo_area:^140}')
            linhas("white", '-', 140)

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
        print('')

        if seleção == '7':
            break

        while True:
            seleção = str(input('Selecione uma opção: '))
            continuar = ''

            if seleção == '1':
                os.system('cls')
                id_produto = 0

                while True:
                    os.system('cls')
                    sleep(0.5)

                    painel_de_entrada('CADASTRAR PRODUTOS')

                    nome_produto = str(input(f'\n{"PRODUTO":.<16}: '))
                    codigo_produto = int(input(f'{"CÓDIGO":.<16}: '))
                    quantidade_produto = int(input(f'{"QUANTIDADE":.<16}: '))
                    data_entrega_produto = str(input(f'{"DATA DA ENTREGA":.<16}: '))
                    nota_fiscal_produto = int(input(f'{"NOTA FISCAL":.<16}: '))

                    data_cadastro = datetime.now().replace(microsecond=0)

                    '''Executa dentro do PostgreSQL a variável <sql_produtos> e <sql_usuarios> que armazena os dados acima      ↑'''
                    sql_produtos = f"INSERT INTO estoque VALUES (default, '{nome_produto}', '{codigo_produto}', '{quantidade_produto}', '{data_entrega_produto}', '{data_cadastro}', '{nota_fiscal_produto}')"

                    cursor_produtos.execute(sql_produtos)
                    # Save the changes
                    connection_produtos.commit()

                    print(f'\n{colors["green"]}PRODUTO CADASTRADO COM SUCESSO!{colors["default"]}\n')

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
                sleep(0.5)

                painel_de_entrada('ESTOQUE')
                print('')

                print(f'{"ID":^6} {"PRODUTO":^40} {"CÓDIGO":^9} {"QTD":^16} {"DATA ENTREGA":^17} {"DATA CADASTRO":^27} {"NOTA FISCAL":^17}')
                print('-' * 6, end='    '), print('-' * 32, end='    ')  # ID & PRODUTO
                print('-' * 12, end='    '), print('-' * 8, end='    ')  # CÓDIGO & QTD
                print('-' * 18, end='    '), print('-' * 21, end='    ')  # DATA ENTREGA & DATA CADASTRO
                print('-' * 19, end='\n')  # NOTA FISCAL

                # Mesma merda que o cur.execute(sql_produto), porém aqui estamos executando diretamente no parâmetro, ao invés de antes definir em uma variável.
                cursor_produtos.execute('SELECT * FROM estoque')

                # Só deus sabe, mas provavelmente recebe todos os dados do comando acima, ~cur.execute('SELECT * FROM cidade')~.
                recset = cursor_produtos.fetchall()

                # PARA CADA rec EM recset:
                # IMPRIMIR (rec)
                for row in recset:
                    print(row[0], end=' | ')  # ID
                    print(row[1], end=' | ')  # PRODUTO
                    print(row[2], end=' | ')  # CÓDIGO
                    print(row[3], end=' | ')  # QTD
                    print(row[4], end=' | ')  # DATA ENTREGA
                    print(row[5], end=' | ')  # DATA CADASTRO
                    print(f'{row[6]:^27}', end='\n')  # NOTA FISCAL

                print(f'\n{colors["default"]}')

                print(f'\n{colors["red"]}{"APERTE A TECLA <ESC> PARA SAIR!":^140}{colors["default"]}')
                keyboard.wait('esc')

                os.system('cls')
                sleep(0.5)

                break

            elif seleção == '3':

                os.system('cls')
                sleep(0.5)

                painel_de_entrada('EXCLUIR UM PRODUTO')
                print('')

                # ID ↓
                codigo_produto_excluir = int(input(f'ID/CÓDIGO: '))
                # Adicionar no ID ↑ que também funcione com de fato o CÓDIGO do produto. Ambos juntos, no mesmo input.

                print(f'\n{"ID":^6} {"PRODUTO":^40} {"CÓDIGO":^9} {"QTD":^16} {"DATA ENTREGA":^17} {"DATA CADASTRO":^27} {"NOTA FISCAL":^17}')
                print('-' * 6, end='    '), print('-' * 32, end='    ')  # ID & PRODUTO
                print('-' * 12, end='    '), print('-' * 8, end='    ')  # CÓDIGO & QTD
                print('-' * 18, end='    '), print('-' * 21, end='    ')  # DATA ENTREGA & DATA CADASTRO
                print('-' * 19, end='\n')  # NOTA FISCAL

                print(f'{colors["green"]}')

                try:
                    cursor_produtos.execute(f"SELECT * FROM estoque WHERE id = {codigo_produto_excluir}")

                    # Recebe os dados de produtos (comando acima).
                    recset = cursor_produtos.fetchall()

                    # PARA CADA rec EM recset:
                    # IMPRIMIR (rec)
                    for row in recset:
                        print(row[0], end=' | ')  # ID
                        print(row[1], end=' | ')  # PRODUTO
                        print(row[2], end=' | ')  # CÓDIGO
                        print(row[3], end=' | ')  # QTD
                        print(row[4], end=' | ')  # DATA ENTREGA
                        print(row[5], end=' | ')  # DATA CADASTRO
                        print(f'{row[6]:^27}', end='\n')  # NOTA FISCAL

                    print(f'\n{colors["default"]}')

                    # ARRUMAR ↓
                    confirmação_excluir = str(input(f'{colors["red"]}DESEJA EXCLUIR ESTE PRODUTO? [S/N]{colors["default"]}: ').strip().upper())
                    if confirmação_excluir == 'S':
                        try:
                            sql_produtos = f'DELETE FROM estoque WHERE id = {codigo_produto_excluir}'
                            # Executa a variável acima como um query
                            cursor_produtos.execute(sql_produtos)
                            # Save the changes
                            connection_produtos.commit()

                            print(f'{colors["green"]}PRODUTO EXCLUÍDO COM SUCESSO!')
                        except:
                            print(f'{colors["red"]}NÃO FOI POSSÍVEL REALIZAR A OPERAÇÃO')

                    elif confirmação_excluir == 'N':
                        break
                except:
                    print(f'{colors["red"]}ID INEXISTENTE{colors["default"]}')

                print(f'\n{colors["red"]}{"APERTE A TECLA <ESC> PARA SAIR!":^140}{colors["default"]}')
                keyboard.wait('esc')

                os.system('cls')
                sleep(0.5)

                break

            elif seleção == '4':
                print('u')

            elif seleção == '5':
                os.system('cls')
                id_usuario = 0

                while True:
                    os.system('cls')
                    sleep(0.5)

                    # Definição destas variáveis logo aqui antes mesmo do input para que na hora do .append() tudo funcione corretamente. Apenas não será necessário mostrar na parte gráfica caso não contenha um valor diferente de '0'.
                    cpf_usuario = 0
                    cnpj_usuario = 0

                    painel_de_entrada('CADASTRAR USUÁRIO')

                    nome_usuario = str(input(f'\n{"NOME":.<16}: ').strip())
                    telefone_usuario = str(input(f'{"TELEFONE":.<16}: ').strip())
                    codigo_usuario = int(input(f'{"CÓDIGO":.<16}: ').strip())
                    tipo_de_usuario = str(input('Físico (CPF) ou Jurídico (CNPJ)? [F/J]: ').upper().strip()[0])

                    data_cadastro = datetime.now().replace(microsecond=0)

                    if tipo_de_usuario == 'F':
                        cpf_usuario = str(input(f'{"CPF":.<16}: ').strip())
                    elif tipo_de_usuario == 'J':
                        cnpj_usuario = str(input(f'{"CNPJ":.<16}: ').strip())
                    else:
                        while tipo_de_usuario not in 'FJ':
                            print(f'{colors["red"]}OPÇÃO INVÁLIDA{colors["default"]}\n')
                            tipo_de_usuario = str(input('Físico (CPF) ou Jurídico (CNPJ)? [F/J]: ').upper().strip()[0])

                        if tipo_de_usuario == 'F':
                            cpf_usuario = str(input(f'{"CPF":.<16}: ').strip())
                        elif tipo_de_usuario == 'J':
                            cnpj_usuario = str(input(f'{"CNPJ":.<16}: ').strip())

                    # CRIAR NESTA LINHA E ABAIXO UM VALIDADOR DE CPF. COLOCAR VÁRIAS ALTERNATIVAS, ELE SENDO APENAS NÚMEROS, CONTENDO PONTOS, HÍFEN, ETC. Fazer o mesmo após para CNPJ.

                    '''Executa dentro do PostgreSQL a variável <sql_produtos> e <sql_usuarios> que armazena os dados acima      ↑'''
                    sql_usuarios = f"INSERT INTO usuario VALUES (default, '{nome_usuario}', '{telefone_usuario}', '{codigo_usuario}', '{cpf_usuario}', '{cnpj_usuario}', '{data_cadastro}')"

                    cursor_usuarios.execute(sql_usuarios)

                    '''Pelo que aparenta, ele faz tudo que foi feito acima, entrar em vigor no banco de dados'''
                    connection_usuarios.commit()

                    print(sql_usuarios)

                    print(usuários)
                    print(f'\n{colors["green"]}USUÁRIO CADASTRADO COM SUCESSO!{colors["default"]}\n')

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

                os.system('cls')
                sleep(0.5)

                painel_de_entrada('ESTOQUE')
                print('')

                print(f'{"ID":^6} {"NOME":^40} {"TELEFONE":^16} {"CÓDIGO":^17} {"CPF":^18} {"CNPJ":^29} {"DATA CADASTRO":^29}')
                print('-' * 6, end='    '), print('-' * 32, end='    ')  # ID & NOME
                print('-' * 18, end='    '), print('-' * 10, end='    ')  # TELEFONE & CÓDIGO
                print('-' * 18, end='    '), print('-' * 25, end='    ')  # CPF & CNPJ
                print('-' * 26, end='\n')  # DATA CADASTRO

                # Mesma merda que o cur.execute(sql_produto), porém aqui estamos executando diretamente no parâmetro, ao invés de antes definir em uma variável.
                cursor_usuarios.execute('SELECT * FROM usuario')

                # Só deus sabe, mas provavelmente recebe todos os dados do comando acima, ~cur.execute('SELECT * FROM cidade')~.
                recset = cursor_usuarios.fetchall()

                # PARA CADA rec EM recset:
                # IMPRIMIR (rec)
                for row in recset:
                    print(f'{row[0]:^6}', end='  ')  # ID
                    print(f'{row[1]:^34}', end='   ')  # NOME
                    print(f'{row[2]:^20}', end='   ')  # TELEFONE
                    print(f'{row[3]:^12}', end='   ')  # CÓDIGO
                    print(f'{row[4]:^20}', end='   ')  # CPF
                    print(f'{row[5]:^27}', end='   ')  # CNPJ
                    print(f'{row[6]:^28}', end='\n')  # DATA CADASTRO

                print(f'\n{colors["default"]}')

                print(f'\n{colors["red"]}{"APERTE A TECLA <ESC> PARA SAIR!":^140}{colors["default"]}')
                keyboard.wait('esc')

                os.system('cls')
                sleep(0.5)

                break

            elif seleção == '7':
                break

            else:
                print(f'{colors["red"]}OPÇÃO INVÁLIDA{colors["default"]}\n')

if __name__ == '__main__':

    os.system('cls')
    '''Chamada da função do banco de dados para realizar sua criação'''

    '''Nome auto-explicativo. Utilizável para para dar um ar de maior complexidade, completo bullshit.'''
#    carregamento_falso()
    '''Limpa a tela após a execução do carregamento falso acima, para facilitar a utilização.'''
    os.system('cls')
    '''Chamada do programa principal'''
    controle_de_estoque()
    '''Limpa a tela após fim de execução do programa'''
    os.system('cls')
