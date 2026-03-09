#Routine item UIの最小単位
@ft.control
class RoutineItem(ft.Row):
    # 名前と完了　(それを変更するコールバック関数)
    def __init__(self,routine,on_delete,on_toggle):
        super().__init__()
        # self.name = name
        # self.done = done
        self.routine = routine #routine objectを受け取る
        self.on_delete = on_delete
        self.on_toggle = on_toggle
        self.checkbox = ft.Checkbox(
            label = routine.name,
            value = routine.done,
            on_change= self._on_toggle,
        )
        self.controls = [
            self.checkbox,
            ft.IconButton(icon=ft.Icons.DELETE,on_click=self._on_delete),
        ]
    def _on_delete(self,e):
        self.on_delete(self.routine) #変更対象
    def _on_toggle(self,e):
        self.on_toggle(self.routine,self.checkbox.value) #まだ伝わっていない