from app.data.models.question import Question

class Menu:
    def __init__(self, id=0, question=None):
        self._id = id
        self._question = question

    def set_id(self, id):
        self._id = id

    def get_id(self):
        return self._id

    def set_question(self, question):
        if isinstance(question, Question):
            self._question = question
        else:
            raise ValueError("El argumento debe ser una instancia de Question.")

    def get_question(self):
        return self._question

