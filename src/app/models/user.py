from src.app.infrastructure.query import execute
from hashlib import md5


class User:
    def __init__(self, f_name, l_name, email, pwd, uid=None):
        self.uid = uid
        self.f_name = f_name
        self.l_name = l_name
        self.email = email
        self.pwd = pwd

    @property
    def full_name(self):
        return f'{self.f_name} {self.l_name}'

    @staticmethod
    def search_uid(uid):
        sql = ['search_one', 'users', ['*'], 'uid']
        parameters = (uid,)
        rows = execute(sql, parameters)
        return list(map(_row_2_obj, rows))[0] if rows else None

    @staticmethod
    def search_all():
        sql = ['search_all', 'users', ['*']]
        rows = execute(sql)
        return list(map(_row_2_obj, rows)) if rows else None

    def save(self):
        if self.uid:
            sql = ['update', 'users', ['f_name', 'l_name', 'email', 'pwd'], 'uid']
            parameters = (self.f_name, self.l_name, self.email, _hash(self.pwd), self.uid)
        else:
            sql = ['insert', 'users', ['f_name', 'l_name', 'email', 'pwd']]
            parameters = (self.f_name, self.l_name, self.email, _hash(self.pwd))
        last_row_id = execute(sql, parameters)
        return User(self.f_name, self.l_name, self.email, _hash(self.pwd), last_row_id if last_row_id else self.uid)

    @staticmethod
    def delete(uid):
        sql = ['delete', 'users', 'uid']
        parameters = (uid,)
        sql_response = User.search_uid(uid)
        if sql_response:
            execute(sql, parameters)
        return sql_response

    def to_json(self):
        return {
            'uid': self.uid,
            'f_name': self.f_name,
            'l_name': self.l_name,
            'email': self.email,
            'pwd': self.pwd
        }

    @staticmethod
    def json_2_obj(user_json):
        return User(
            user_json["f_name"],
            user_json["l_name"],
            user_json["email"],
            user_json["pwd"],
            user_json["uid"] if 'uid' in user_json else None
        )


def _hash(pwd):
    return md5(str(pwd).encode('utf-8')).hexdigest()


def _row_2_obj(row):
    return User(row[1], row[2], row[3], row[4], row[0])
