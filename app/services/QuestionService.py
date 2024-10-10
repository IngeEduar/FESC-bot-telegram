from app.data.models.question import Question

class QuestionService:

    questions = [
        Question(
            id=0,
            question="/start",
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
        ),
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

    def getQuestionById(self, id):
        return self.questions[id]


    def get_questions(self):
        return self.questions

    
    def getQuestionByQuestion(self, search):
        for question in self.questions:
            if question.get_question() == search:
                return question
        
        return Question(
            response="Esta pregunta aún no tiene configurada una respuesta, lo sentimos"
        )

    def add_question(self, question, parentId):
        self.questions.append(question)

        for questionParent in self.questions:
            if parentId == questionParent.get_id():
                newOptions = questionParent.get_options()
                newOptions.append(question)
                questionParent.set_options(newOptions)

                self.questions[parentId] = questionParent

    
    def pushQuestions(self):

        self.questions = self.questions