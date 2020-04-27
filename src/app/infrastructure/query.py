from src.app.models import database as db


def query_insert(table, attributes, parameters):
    prefix = f'INSERT INTO {table} '
    var_attributes = _make_attributes(attributes)
    var_param = _make_param(attributes)
    sql_statement = prefix + var_attributes + var_param

    return sql_statement


def _make_param(attributes):
    var = '('
    for i in range(len(attributes)):
        if i == len(attributes)-1:
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
