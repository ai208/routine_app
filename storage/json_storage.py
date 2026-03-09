import json
from datetime import date
from models.user import UserModel
from models.routine import RoutineModel
#データの保存専門
class JsonStorage:
    def __init__(self,filename :str):
        self.filename = filename
    def save(self,user):
        data = self.user_to_dict(user)
        with open(self.filename,"w",encoding="utf-8") as f:
            json.dump(data,f,ensure_ascii=False,ident = 2)
    def load(self):
        try:
            with open(self.filename,"r", encoding="utf-8") as f:
                data = json.load(f)
                return self.dict_to_user(data)
        except FileNotFoundError:
            return None
    # モデルをdict(json) に変換しないといけない data は　str に変換する必要がある
    def user_to_dict(self,user):
        routines = []
        for r in user.routines:
            routines.append({
                "id":r.id,
                "name":r.name,
                "done":r.done,
                "total_done":r.total_done,
                "last_done_date":r.last_done_date.isoformat() if r.last_done_date else None # dat をstr にしてjson にできるようにした。
            })
        return {
            "username" : user.username,
            "login_streak":user.login_streak,
            "last_login":user.last_login.isoformat() if user.last_login else None,
            "routines":routines
        }
    def dict_to_user(self,data): #読み取り dict にしたものをclassに変換する
        routines = []
        for r in data["routines"]:
            routines.append(
                RoutineModel(
                    id = r["id"],
                    name = r["name"],
                    dne = r["name"],
                    total_done= r["total_done"],
                    last_done_date= date.fromisoformat(r["last_done_date"]) if r["last_done_date"] else None
                )
            )
        return UserModel(
            username=data["username"],
            login_streak=data["login_streak"],
            last_login=date.fromisoformat(data["last_login"]) if data["last_login"] else None,
            routines= routines
        )
