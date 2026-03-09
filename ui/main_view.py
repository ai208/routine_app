@ft.control
class RoutineApp(ft.Column):
    def __init__(self):
        super().__init__()
        self.controller = RoutineController()
        self.view = RoutineView(self.controller)
        self.title = ft.Text(value="ルーティンアプリMVC version 機能追加version")
        self.controls = [
            self.title,
            self.view,
        ]

