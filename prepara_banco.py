import psycopg2
print('Conectando...')
conn = psycopg2.connect(
      host="localhost",
      database="classificaSerie",
      port="5432",
      user='admin',
      password='admin'
      )

# Descomente se quiser desfazer o banco...
conn.cursor().execute("DROP DATABASE `classificaSerie`;")
conn.commit()

criar_tabelas = '''SET NAMES utf8;
    CREATE DATABASE `classificaSerie` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_bin */;
    USE `classificaSerie`;
    CREATE TABLE `serie` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `nome` varchar(50) COLLATE utf8_bin NOT NULL,
      `categoria` varchar(40) COLLATE utf8_bin NOT NULL,
      `plataforma` varchar(20) NOT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
    CREATE TABLE `usuario` (
      `id` varchar(8) COLLATE utf8_bin NOT NULL,
      `nome` varchar(20) COLLATE utf8_bin NOT NULL,
      `senha` varchar(8) COLLATE utf8_bin NOT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;'''

conn.cursor().execute(criar_tabelas)

# inserindo usuarios
cursor = conn.cursor()
cursor.executemany(
      'INSERT INTO classificaSerie.usuario (id, nome, senha) VALUES (%s, %s, %s)',
      [
            ('luan', 'Luan Marques', 'flask'),
            ('nico', 'Nico', '7a1'),
            ('danilo', 'Danilo', 'vegas')
      ])

cursor.execute('select * from classificaSerie.usuario')
print(' -------------  Usuários:  -------------')
for user in cursor.fetchall():
    print(user[1])

# inserindo series
cursor.executemany(
      'INSERT INTO classificaSerie.serie (nome, categoria, plataforma) VALUES (%s, %s, %s)',
      [
            ('A casa do Dração', 'Fantasia', 'HBO'),
            ('Luis Miguel', 'Biografia', 'netflix'),
            ('The Witcher', 'Fantasia', 'Netflix'),
            ('Hanna', 'acao', 'Prime Video'),
            ('House, M.D.', 'Médica', 'Prime Video'),
            ('Greys Anatomy', 'Médica', 'Prime Video'),
      ])

cursor.execute('select * from classificaSerie.serie')
print(' -------------  series:  -------------')
for serie in cursor.fetchall():
    print(serie[1])

# commitando senão nada tem efeito
conn.commit()
cursor.close()
