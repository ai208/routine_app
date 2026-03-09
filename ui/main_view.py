import flet as ft
from controllers.routine_controller import RoutineController
from .routine_list import RoutineView
from .user_info import User_page
from models.user import UserModel
@ft.control
class RoutineApp(ft.Column):
    def __init__(self,app_model,routine_service,user_service):
        super().__init__()
        self.routine_controller = RoutineController(app_model,routine_service) # ここに変数が必要になっている。 model_app と　serviceが必要になっている。
        user = UserModel(username="ゲスト",login_streak=0)
        self.routine_view = RoutineView(self.routine_controller,user)
        self.user_page_view = User_page(app_model.username) # 簡単なページ
        self.title = ft.Text(value="ルーティンアプリMVC version 機能追加version")
        self.controls = [
            self.title,
            self.user_page_view,
            self.routine_view,
        ]

