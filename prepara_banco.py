import mysql.connector
from mysql.connector import errorcode

print("Conectando...")
try:
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='root'
    )
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Existe algo errado no nome de usuário ou senha')
    else:
        print(err)

cursor = conn.cursor()
cursor.execute("DROP DATABASE IF EXISTS `classificaSeries`")
cursor.execute("CREATE DATABASE `classificaSeries`")
cursor.execute("USE `classificaSeries`")


# Criando tabelas
TABLES = {}
TABLES['Series'] = ('''
    CREATE TABLE `series` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `nome` varchar(50) NOT NULL,
    `categoria` varchar(40) NOT NULL,
    `plataforma` varchar(20) NOT NULL,
    PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Usuarios'] = ('''
    CREATE TABLE `usuarios` (
    `nome` varchar(20) NOT NULL,
    `nickname` varchar(8) NOT NULL,
    `senha` varchar(100) NOT NULL,
    PRIMARY KEY (`nickname`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

for tabela_nome in TABLES:
    tabela_sql = TABLES[tabela_nome]
    try:
        print(f'Criando tabela {tabela_nome}', end=' ')
        cursor.execute(tabela_sql)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print('Já existe')
        else:
            print(err.msg)
    else:
        print('OK')

# Inserindo usuários
usuario_sql = 'INSERT INTO usuarios (nome, nickname, senha) VALUES (%s, %s, %s)'
usuarios = [
    ("Bruno Divino", "DB", "alohomora"),
    ("Camila Ferreira", "Mila", "paozinho"),
    ("Guilherme Louro", "cake", "python_eh_vida")
]
cursor.executemany(usuario_sql, usuarios)

cursor.execute('select * from classificaSeries.usuarios')
print(' ----------  Usuários  ---------- ')
for user in cursor.fetchall():
    print(user[1])

# Inserindo series
series_sql = 'INSERT INTO series (nome, categoria, plataforma) VALUES (%s, %s, %s)'
series = [
    ('A casa do Dração', 'Fantasia', 'HBO'),
    ('Luis Miguel', 'Biografia', 'netflix'),
    ('The Witcher', 'Fantasia', 'Netflix'),
    ('Hanna', 'acao', 'Prime Video'),
    ('House, M.D.', 'Médica', 'Prime Video'),
    ('Greys Anatomy', 'Médica', 'Prime Video'),
]

cursor.executemany(series_sql, series)

cursor.execute('select * from classificaSeries.series')
print(' ----------  Series  ---------- ')
for serie in cursor.fetchall():
    print(serie[1])

# Commitando se não nada tem efeito
conn.commit()
cursor.close()
