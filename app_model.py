#アプリの状態 のみにする
class AppModel:
    def __init__(self,repository): # dataclass で引数を取る方法
        # self.filename = filename storageに渡す
        # self.storage = storage # こっちにデータの保存を任せる　   repository に渡す
        self.repository = repository
        self.user : UserModel | None = None
    # user_model : class
    # # routines_model : class # userが持つ
    # all_data : list # は　userに入っている
    # filename : str
    def save(self): # アプリは状態のみ　データの保存
        # with open(self.filename,"w",encoding="utf-8") as f: しない　storage に送る
        #     json.dump(self.all_data,f,ensure_ascii = False,indent = 2)
        # self.storage.save(self.user)
        self.repository.save(self.user)

    def load(self):
        # try:storage に任せる 引っ張てくる
        #     with open(self.filename,"r",encoding="utf-8") as f:
        #         self.all_data =json.load(f)
        # except FileNotFoundError:
        #     self.all_data = []
        # self.user = self.storage.load() storageをしない
        self.repository.load()