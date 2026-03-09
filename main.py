import flet as ft
from ui.main_view import RoutineApp
from storage.json_storage import JsonStorage
from repositories.user_repository import User_Repository
from services.user_service import User_Service
from services.routine_service import Routine_Service
from models.app_model import AppModel
from controllers.routine_controller import RoutineController
from controllers.user_controller import UserController
def main(page:ft.Page):
    # page.add(ft.Text(value = "Hello"))
    storage = JsonStorage("user_data.json")
    repository = User_Repository(storage)
    user_service =User_Service()
    routine_service = Routine_Service()
    app_model = AppModel(repository)
    routine_controller = RoutineController(app_model,routine_service)
    user_controller = UserController(app_model,user_service)

    app = RoutineApp(app_model,routine_service,user_service)
    page.add(app)


if __name__ =="__main__":
    ft.run(main)

# 1. The application encountered an error: RoutineView.__init__() missing 1 required positional argument: 'user