from .operations import builder_sql as _builder_sql
from .database import DBConnect


def execute(sql, parameters=None):
    string_sql = _builder_sql(*sql)
    db = DBConnect().cursor
    db.execute(string_sql, parameters) if parameters else db.execute(string_sql)
    sql_response = 'O peração realizada com sucesso.' if sql[0] != 'search_one' and sql[0] != 'search_all' \
        else db.fetchone() if sql[0] == 'search_one' else db.fetchall()
    db.close()
    return sql_response

# Falta implementar para que os metodos sejam devolvidos como objetos e a msg seja do arquivo de strings
