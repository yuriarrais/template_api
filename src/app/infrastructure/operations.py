from src.config.parameters import db_char


def _search_one(table, attributes, identifier):
    var_attributes = _make_attrib_format(attributes)
    return f'SELECT {var_attributes} FROM {table} WHERE {identifier}={db_char};'


def _search_all(table, attributes):
    var_attributes = _make_attrib_format(attributes)
    return f'SELECT {var_attributes} FROM {table};'


def _insert(table, attributes):
    parameterized = ', '.join([db_char] * len(attributes))
    var_attributes = _make_attrib_format(attributes)
    return f'INSERT INTO {table} ({var_attributes}) VALUES ({parameterized});'


def _update(table, attributes, identifier):
    values = f'={db_char}, '.join(attributes)
    return f'UPDATE {table} SET {values}={db_char} WHERE {identifier}={db_char};'


def _delete(table, identifier):
    return f'DELETE FROM {table} WHERE {identifier}={db_char};'


def _make_attrib_format(attributes):
    return ', '.join(attributes)


function_type = {
    'search_one': _search_one,
    'search_all': _search_all,
    'insert': _insert,
    'update': _update,
    'delete': _delete
}


def builder_sql(sql_type, table, attributes, identifier=''):
    return function_type[sql_type](table, attributes, identifier) \
        if identifier else function_type[sql_type](table, attributes)
