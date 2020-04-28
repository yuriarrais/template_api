
def query_insert(table, attributes, parameters):
    attributes = _make_attrib_format(attributes)
    parameterized = _make_param(attributes)
    sql_statement = f'INSERT INTO {table} {attributes} VALUES {parameterized}'
    return sql_statement


def query_search_all(table, attributes):
    attributes = _make_attrib_format(attributes)
    sql_statement = f'SELECT {attributes} FROM {table} '
    return sql_statement


def _make_param(attributes):
    char = '?'                         # '?' sqlite3   ///  '%s' pgql
    length = len(attributes)
    var = ', '.join([char] * length)
    return f'({var})'


def _make_attrib_format(attributes):
    var = ', '.join(attributes)
    return f'({var})'


def _make_parameters(parameters):
    tuples = tuple(parameters)
    return tuples
