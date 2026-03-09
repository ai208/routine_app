from  dataclasses import dataclass,field
from datetime import date
from .routine import RoutineModel
@dataclass
class UserModel:
    username :str
    login_streak : int
    # total_done : int　完了は　ルーチンモデルの方が持つべき
    last_login : date | None = None
    routines : list[RoutineModel] = field(default_factory = list) # pythonの罠の回避
