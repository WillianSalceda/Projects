import psycopg2

    
'''Atribui os comandos de conexão para a variável <connection> ↓
host='' É o host da database, neste caso é localhost (local). 
database='' É o nome que daremos para o banco de dados, no caso, 'produtos'.
user='' É o usuário responsável pela aquela database.
password='' É a senha do user='' para acessar a database.'''
connection_produtos = psycopg2.connect(host='localhost', database='produtos', user='postgres', password='')
connection_usuarios = psycopg2.connect(host='localhost', database='usuarios', user='postgres', password='')

'''Não sei'''
cursor_produtos = connection_produtos.cursor()
cursor_usuarios = connection_usuarios.cursor()


'''Dentro da variável sql armazenamos entre aspas simples o comando de query/queries que queremos passar para a database (que no caso é produtos).
O que esta em letra maiúscula antes dos parenteses são comandos específicos de query, o resto são nomes. No caso.(CRIAR TABELA cidade).
id serial primary key = dado chamado id é atribuído como serial, que a cada inserção cresce em 1, e também chave primária, então nunca poderá haver algum id igual (1 e 1, ou 5 e 5).'''

sql_produtos = 'CREATE TABLE estoque (id serial primary key, produto varchar(100), codigo varchar(50), quantidade varchar(5), data_de_entrega varchar(20), data_cadastro varchar(100), nota_fiscal varchar(50))'

sql_usuarios = 'CREATE TABLE usuario (id serial primary key, nome varchar(100), telefone varchar(20), codigo varchar(20), cpf varchar(20), cnpj varchar(20), data_cadastro varchar(50))'

'''Executa dentro do PostgreSQL a variável <sql_produtos> e <sql_usuarios> que armazena os dados acima ↑'''
cursor_produtos.execute(sql_produtos)
cursor_usuarios.execute(sql_usuarios)

'''Pelo que aparenta, ele faz tudo que foi feito acima, entrar em vigor no banco de dados'''
connection_produtos.commit()
connection_usuarios.commit()