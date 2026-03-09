import flet as ft

# 最小のユーザーページ　model を表示する　最初は
@ft.control
class User_page(ft.Column):
    def __init__(self,user):
        super().__init__()
        self.user = user
        self.controls = [
            ft.Text(value = self.user.username),
            ft.Text(value = f'連続ログインは{self.user.login_streak}'),
        ]