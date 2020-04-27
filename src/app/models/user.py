from hashlib import md5


class User:
    def __init__(self, f_name, l_name, email, pwd, uid=None):
        self.uid = uid
        self.f_name = f_name
        self.l_name = l_name
        self.email = email
        self.pwd = pwd

    def to_json(self):
        return {
            'uid': self.uid,
            'f_name': self.f_name,
            'l_name': self.l_name,
            'email': self.email,
            'pwd': self.pwd
        }

    def json2obj(user_json):
        return User(
            user_json["f_name"],
            user_json["l_name"],
            user_json["email"],
            user_json["pwd"],
            user_json["uid"]
        )

    def search_all_users(self):
        pass

    def search_uid_user(self, uid):
        pass

    def save_user(self, obj_user):
        pass

    def delete_user(self, uid):
        pass


def hash_(pwd):
    return md5(str(pwd).encode('utf-8')).hexdigest()
