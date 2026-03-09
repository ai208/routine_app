import flet as ft
from .routine_item import RoutineItem
from models.user import UserModel
#RoutineList UIの箱 入力を受け取る　→　コントローラーに伝える 変更あり　userを使う
@ft.control
class RoutineView(ft.Column):
    def __init__(self,controller,user:UserModel):
        super().__init__()
        # self.controller = RoutineController() 作らない　受け取る　依存関係　アプリから受け取る
        self.controller = controller
        self.user = user # routine をもつ
        done = self.controller.service.count_done()
        total = self.controller.service.count_total_task()
        self.status = ft.Text(value= f'本日の完了タスク : {done} /{total}') # UIなので、ここに置く　計算はコントローラー
        self.new_routine = ft.TextField(hint_text="タスクを入力してください。")
        self.button = ft.FloatingActionButton(icon=ft.Icons.ADD,on_click=self._add_clicked)
        self.input_row = ft.Row(
            controls= [self.new_routine, self.button]
        )
        self.list = ft.Column()
        self.controls = [
            self.status,
            self.input_row,
            self.list,
        ]
        self.refresh() #一応やっておく
    def _add_clicked(self,e): # イベントは必ずe
        if self.new_routine.value.strip()!="":
            self.controller.add_item(self.new_routine.value)
            self.new_routine.value = ""
            self.refresh()
    def refresh(self):
        self.list.controls.clear()
        for r in self.user.routines: # values は? dict のkey:value こっちを取る
            item = RoutineItem(
                routine= r,
                on_delete= self.on_delete,
                on_toggle= self.on_toggle

            )
            self.list.controls.append(item)
        done = self.controller.service.count_done()
        total = self.controller.service.count_total_task()
        self.status.value = f'本日の完了タスク : {done} /{total}' #こうしないと更新されない
    #コントローラーを変化する
    def on_delete(self,routine):
        # del self.controller.routines[routine.id] 消去はcontrollerでする
        self.controller.delete_item(routine.id)
        self.refresh()
    def on_toggle(self,routine,done):
        self.controller.toggle_change(routine.id,done)
        self.refresh()