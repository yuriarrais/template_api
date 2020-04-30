from .operations import builder_sql as _builder_sql
from .database import DBConnect


def execute(sql, parameters=None):
    string_sql = _builder_sql(sql[0], sql[1], sql[2], sql[3]) \
        if len(sql) == 4 else _builder_sql(sql[0], sql[1], sql[2])
    db = DBConnect().cursor
    db.execute(string_sql, parameters) if parameters else db.execute(string_sql)
    return 'O peração realizada com sucesso.' if sql[0] != 'search_one' and sql[0] != 'search_all' \
        else db.fetchone() if sql[0] == 'search_one' else db.fetchall()

# Falta implementar para que os metodos sejam devolvidos como objetos e a msg seja do arquivo de strings