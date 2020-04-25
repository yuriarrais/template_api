class User:
    def __init__(self, json):
        self.name = json.name
        self.email = json.email

    def search_user(self, uid):
        pass

    def search_all_users(self):
        pass

    def del_user(self, uid):
        pass

    def save_user(self, obj_user):
        pass
