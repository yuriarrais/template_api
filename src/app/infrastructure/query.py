from .operations import builder_sql as _builder_sql
from .database import DBConnect


function_type = ['search_one', 'search_all']


def execute(sql, parameters=''):
    string_sql = _builder_sql(*sql)
    db = DBConnect().cursor
    db.execute(string_sql, parameters)
    sql_response = db.fetchall() if sql[0] in function_type else db.lastrowid
    db.close()
    return sql_response
