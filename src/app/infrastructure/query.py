def query_insert(table, attributes, parameters):
    prefix = f'INSERT INTO {table} '
    var_attributes = _make_attributes(attributes)
    var_param = _make_param(attributes)
    sql_statement = prefix + var_attributes + var_param

    return sql_statement


def _make_param(attributes):
    #char = '?, ' * length
    #var = f'({char[:-2]})'
    char = '?'                                  # '?' sqlite3   ///  '%s' pgql
    length = len(attributes)
    var = ', '.join([char] * length).join(["(", ")"])
    return var


def _make_attributes(attributes):
    var = ', '.join(attributes).join(["(", ") VALUES "])
    return var
