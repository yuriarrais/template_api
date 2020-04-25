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