from src.app.models import database as db


def query_insert(atrib, param, table):
    prefix = f'INSERT INTO {table} '
    var_param = _make_param(atrib)
    var_attribute = _make_attributes(atrib)
    sql = prefix + var_attribute + var_param
    return sql


def _make_param(atrib):
    var = '('
    for i in range(len(atrib)):
        if i == len(atrib)-1:
            var += '?)'
        else:
            var += '?, '
    return var


def _make_attributes(attributes):
    var = '('
    count = 0
    for i in attributes:
        if count == len(attributes)-1:
            var += i + ') VALUES '
        else:
            var += i + ', '
        count += 1
    return var
