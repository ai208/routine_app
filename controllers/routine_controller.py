import uuid
from models.routine import RoutineModel
from services.routine_service import Routine_Service
# データを保存しておく　データの中身の変更はしない　更新するだけ
class RoutineController: #操作だけをする　Service に送る
    def __init__(self,app_model,service:Routine_Service): # model とサービスにつながっている
        super().__init__()
        self.app = app_model
        self.service = service
        # self.routines = {} #modelをリストで管理 二重管理になる コントローラーは操作をするだけ
    #追加
    def add_item(self,name):
        id = str(uuid.uuid4()) #関数にしないと消える
        routine = RoutineModel(id,name)
        self.app.user.routines.append(routine)
    def delete_item(self,id):
        # del self.routines[id]
        self.app.user.routines = [
            r for r in self.app.user.routines
            if r.id != id
        ] # このロジックが不明
    #変わったものを更新するだけ　変更は別のところがする
    # def toggle_change(self,id,done): サービスに送る
    #     # self.routines[id].done = done
    #     for r in self.app.user.routines:
    #         if r.id == id:
    #             r.done = done
    def toggle_change(self,routine:RoutineModel,done :bool):
        if done:
            self.service.complete_routine(routine)
        else:
            self.service.undo_routine(routine)

    #これは？ 取り出し　viewから直接触らないようにするlistの方がいい？
    def get_routines(self):
        # return self.routines.values()
        # return list(self.routines.values())
        return self.app.user.routines

    #完了を数える values とは？ dict の　valueを取り出す サービスに送る
    # def count_done(self):
    #     return sum(r.done for r in self.app.user.routines)

    #全タスク数のカウント サービスへ
    # def count_total_task(self):
    #     return len(self.app.user.routines)