from app.data.models.menu import Menu
from app.data.models.question import Question

class MenuService:

    menus = []

    def getMenuById(self, id):
        return self.menus[id]

    def get_menus(self):
        return self.menus

    
    def pushMenu(self):
        initialMenu = Menu(
            id=0, 
            question=Question(
                id=0,
                question="",
                response="¡Hola! Soy tu asistente virtual. Elige una de las siguientes preguntas para obtener una respuesta.",
                options=[
                    Question(
                        id=1,
                        question="¿Cuál es tu nombre?",
                        response="Mi nombre es IngeEduarBot",
                        options=[]
                    ),
                    Question(
                        id=2,
                        question="¿Cómo puedo contactarte?",
                        response="Puedes escribirme por aquí.",
                        options=[]
                    ),
                    Question(
                        id=3,
                        question="¿Cuál es el horario de atención?",
                        response="Atendemos de lunes a viernes de 9 AM a 6 PM",
                        options=[]
                    )
                ]
            )
        )

        self.menus.append(initialMenu)