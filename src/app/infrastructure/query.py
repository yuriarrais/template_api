

def query_insert(table, attributes, parameters):
    prefix = f'INSERT INTO {table} '
    var_attributes = _make_attributes(attributes)
    var_param = _make_param(attributes)
    sql_statement = prefix + var_attributes + var_param

    return sql_statement


def query_search_all(table, attributes):
    var_attributes = _make_attributes(attributes)[1:-8]
    sql_statement = f'SELECT {var_attributes} FROM {table} '
    return sql_statement


def _make_param(attributes):
    char = '?'                                  # '?' sqlite3   ///  '%s' pgql
    length = len(attributes)
    var = ', '.join([char] * length)
    return f'({var})'


def _make_attributes(attributes):
    var = ', '.join(attributes)
    return f'({var}) VALUES '


def _make_parameters(parameters):
    tuples = tuple(parameters)
    return tuples
