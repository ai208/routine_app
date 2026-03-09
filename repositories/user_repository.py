class User_Repository:
    def __init__(self,storage):
        self.storage = storage
    def save_user(self,user):
        self.storage.save(user)
    def load_user(self):
        return self.storage.load()
