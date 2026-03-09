from models.user import UserModel
from services.user_service import User_Service
# user コントローラーも必要になる 一つのモデルに一つ 作成と更新
class UserController: # 操作をする
    def __init__(self,app_model,service:User_Service): #モデルから受け取ってサービスに渡す
        super().__init__()
        self.app = app_model
        self.service = service
    def create_user(self,username):
        self.app.user = UserModel(username=username)
    # def update_login(self): # サービスに送る
    #     today = date.today()
    #     user = self.app.user
    #     if user.last_login != today:
    #         user.login_streak += 1
    #     user.last_login = today
    def update_login(self):
        self.service.update_login(self.app.user)
