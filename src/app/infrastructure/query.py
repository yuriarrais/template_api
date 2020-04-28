
def query_insert(table, attributes, parameters):
    parameterized = _make_param(attributes)
    var_attributes = _make_attrib_format(attributes)
    return f'INSERT INTO {table} ({var_attributes}) VALUES {parameterized}'


def query_search_all(table, attributes):
    var_attributes = _make_attrib_format(attributes)
    return f'SELECT {var_attributes} FROM {table} '


def _make_param(attributes):
    char = '?'                         # '?' sqlite3   ///  '%s' pgql
    length = len(attributes)
    var = ', '.join([char] * length)
    return f'({var})'


def _make_attrib_format(attributes):
    var = ', '.join(attributes)
    return var


def _make_parameters(parameters):
    tuples = tuple(parameters)
    return tuples
