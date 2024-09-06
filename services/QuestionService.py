from models.menu import Menu
from models.question import Question

class QuestionService:

    questions = []

    def getQuestionById(self, id):
        return self.questions[id]
    
    def getQuestionByQuestion(self, search):
        for question in self.questions:
            if question.get_question() == search:
                return question
        
        return Question(
            response="Esta pregunta aún no tiene configurada una respuesta, lo sentimos"
        )
    
    def pushQuestions(self):

        self.questions = [
            Question(
                id=2,
                question="¿Cuál es tu nombre?",
                response="Mi nombre es IngeEduarBot",
                options=[
                    Question(
                        id=5,
                        question="Ere un puto bestia",
                        response="Lo sé mi rey",
                        options=[]
                    ),
                    Question(
                        id=6,
                        question="De mayor quiero ser un inge como tú",
                        response="Tú puede brother",
                        options=[]
                    ),
                    Question(
                        id=7,
                        question="¿Eres Dios?",
                        response="Yo tambien me lo pregunto hermano",
                        options=[
                            Question(
                                id=8,
                                question="Si que lo eres hemano",
                                response="Muchas gracias brother",
                                options=[]
                            ),
                        ]
                    ),
                ]
            ),
            Question(
                id=3,
                question="¿Cómo puedo contactarte?",
                response="Puedes escribirme por aquí.",
                options=[]
            ),
            Question(
                id=4,
                question="¿Cuál es el horario de atención?",
                response="Atendemos de lunes a viernes de 9 AM a 6 PM",
                options=[]
            ),
            Question(
                id=5,
                question="Ere un puto bestia",
                response="Lo sé mi rey",
                options=[]
            ),
            Question(
                id=6,
                question="De mayor quiero ser un inge como tú",
                response="Tú puede brother",
                options=[]
            ),
            Question(
                id=7,
                question="¿Eres Dios?",
                response="Yo tambien me lo pregunto hermano",
                options=[
                    Question(
                        id=8,
                        question="Si que lo eres hemano",
                        response="Muchas gracias brother",
                        options=[]
                    ),
                ]
            ),
            Question(
                id=8,
                question="Si que lo eres hemano",
                response="Muchas gracias brother",
                options=[]
            ),
        ]