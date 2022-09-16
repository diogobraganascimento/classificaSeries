from models import Serie, Usuario

SQL_DELETA_SERIE = 'delete from serie where id = %s'
SQL_SERIE_POR_ID = 'SELECT id, nome, categoria, plataforma from serie where id = %s'
SQL_USUARIO_POR_ID = 'SELECT id, nome, senha from usuario where id = %s'
SQL_ATUALIZA_SERIE = 'UPDATE serie SET nome=%s, categoria=%s, plataforma=%s where id = %s'
SQL_BUSCA_SERIE = 'SELECT id, nome, categoria, plataforma from serie'
SQL_CRIA_SERIE = 'INSERT into serie (nome, categoria, plataforma) values (%s, %s, %s)'


class SerieDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, serie):
        cursor = self.__db.connection.cursor()

        if (serie.id):
            cursor.execute(SQL_ATUALIZA_SERIE, (serie.nome, serie.categoria, serie.plataforma, serie.id))
        else:
            cursor.execute(SQL_CRIA_SERIE, (serie.nome, serie.categoria, serie.plataforma))
            serie.id = cursor.lastrowid
        self.__db.connection.commit()
        return serie

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_SERIE)
        series = traduz_series(cursor.fetchall())
        return series

    def busca_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_SERIE_POR_ID, (id,))
        tupla = cursor.fetchone()
        return Serie(tupla[1], tupla[2], tupla[3], id=tupla[0])

    def deletar(self, id):
        self.__db.connection.cursor().execute(SQL_DELETA_SERIE, (id, ))
        self.__db.connection.commit()


class UsuarioDao:
    def __init__(self, db):
        self.__db = db

    def buscar_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_USUARIO_POR_ID, (id,))
        dados = cursor.fetchone()
        usuario = traduz_usuario(dados) if dados else None
        return usuario


def traduz_series(series):
    def cria_serie_com_tupla(tupla):
        return Serie(tupla[1], tupla[2], tupla[3], id=tupla[0])
    return list(map(cria_serie_com_tupla, series))


def traduz_usuario(tupla):
    return Usuario(tupla[0], tupla[1], tupla[2])
