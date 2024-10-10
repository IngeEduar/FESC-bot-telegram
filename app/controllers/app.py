from app.data.models.question import Question
from app.services.MenuService import MenuService
from app.services.QuestionService import QuestionService
from flask import Flask, render_template, jsonify, request, redirect, url_for
from tornado.escape import json_encode
import os

project_root = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(project_root, 'templates')
app = Flask(__name__, template_folder=templates_dir)

@app.route('/livez', methods=['GET'])
def livez():
    return json_encode({"status": "running"})


### Menu

menuService = MenuService()
questionService = QuestionService()

@app.route('/menus', methods=['GET'])
def get_menus():
    menus = menuService.get_menus()

    return render_template('menu/list.html', menus=menus)

### Question

@app.route('/questions', methods=['GET'])
def get_questions():
    questions = questionService.get_questions()
    return render_template('question/list.html', questions=questions)


@app.route('/question/<int:question_id>', methods=['GET'])
def get_question(question_id):
    question = questionService.getQuestionById(question_id)
    if not question:
        return jsonify({'error': 'Pregunta no encontrada'}), 404
    return render_template('question/detail.html', question=question)

@app.route('/question/add/<int:parent>', methods=['GET'])
def create_question_get(parent):
    return render_template('question/add.html', parent=parent)

@app.route('/question/add/<int:parent>', methods=['POST'])
def create_question_post(parent):
    question = request.form.get('question')
    response = request.form.get('response')

    new_question = Question(
        question=question,
        response=response,
        options=[]
    )

    new_question.set_id(len(questionService.get_questions()))

    questionService.add_question(new_question, parent)

    return redirect(url_for('get_questions'))
