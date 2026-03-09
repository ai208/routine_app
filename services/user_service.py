class User_Service:
    def __init__(self):
        pass
    def update_login(self,user): # userのロジックなので、userがいる
        today = date.today()
        if user.last_login != today:
            user.login_streak +=1
        user.last_login = today