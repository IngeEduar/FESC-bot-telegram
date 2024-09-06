from app.data.connections.database import get_db_connection
from app.data.repository.questionRepository import QuestionRepository
from app.data.models.menu import Menu

class MenuRepository:
    def __init__(self):
        self.connection = get_db_connection()
        self.cursor = self.connection.cursor()
        self.questionRepository = QuestionRepository()

    def getMenus(self):
        menusResponse = []
        try:
            self.cursor.execute("SELECT id, question FROM menu;")
            menus = self.cursor.fetchall()
            
            for menu in menus:
                menusResponse.append(
                    Menu(
                        id=menu[0],
                        question=self.questionRepository.getQuestionById(menu[1]),
                    )
                )
            return menusResponse

        except Exception as e:
            print(f"Error fetching menus: {e}")
            return []

    def getMenuById(self, id):
        try:
            self.cursor.execute("SELECT id, question FROM menu WHERE id = %s;", (id,))
            menu = self.cursor.fetchone() 

            if menu:
                return Menu(
                    id=menu[0],
                    question=self.questionRepository.getQuestionById(menu[1]),
                )
            else:
                return Menu()
        except Exception as e:
            print(f"Error fetching menu by ID: {e}")
            return Menu()

    def close(self):
        self.cursor.close()
        self.connection.close()
