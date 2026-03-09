from  dataclasses import dataclass,field
@dataclass
class RoutineModel:
    id :str
    name : str
    done : bool = False
    total_done : int = 0 # Routein に関連することはこっちがもつ
    last_done_date : date | None = None # 最初　と　チェックをも出した時はNoneが入る 完了したら　=date.today() とする # dataはjson で持てないからstrにする