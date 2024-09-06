from app.data.connections.database import get_db_connection
from app.data.models.question import Question

class QuestionRepository:
    def __init__(self):
        self.connection = get_db_connection()
        self.cursor = self.connection.cursor()

    def getQuestions(self):
        questionsResponse = []
        try:
            self.cursor.execute("SELECT id, question, response FROM questions;")
            questions = self.cursor.fetchall()
            
            for question in questions:
                questionsResponse.append(
                    self._build_question_with_options(question)
                )
            return questionsResponse

        except Exception as e:
            print(f"Error fetching questions: {e}")
            return []

    def getQuestionById(self, id):
        try:
            self.cursor.execute("SELECT id, question, response FROM questions WHERE id = %s;", (id,))
            question = self.cursor.fetchone()

            if question:
                return self._build_question_with_options(question)
            else:
                return Question()
        except Exception as e:
            print(f"Error fetching question by ID: {e}")
            return Question()

    def _build_question_with_options(self, question_data):
        """Helper function to build a Question object with its options (subquestions) using the question_options table."""
        question_id, question_text, response = question_data

        question = Question(
            id=question_id,
            question=question_text,
            response=response
        )

        self.cursor.execute("""
            SELECT q.id, q.question, q.response 
            FROM questions q 
            INNER JOIN question_options qo ON q.id = qo.option_id 
            WHERE qo.question_id = %s;
        """, (question_id,))
        
        options = self.cursor.fetchall()

        for option_data in options:
            option = Question(
                id=option_data[0],
                question=option_data[1],
                response=option_data[2]
            )
            question.set_option(option)

        return question

    def close(self):
        self.cursor.close()
        self.connection.close()
