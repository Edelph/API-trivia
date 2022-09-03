import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    '''
  @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
  '''

    '''
  @TODO: Use the after_request decorator to set Access-Control-Allow
  '''


@app.after_request
def after_request(response):
    response.header.add('Access-Control-Allow-Headers',
                        'Content-Type, Authorization')
    response.header.add('Access-Control-Allow-Methods',
                        'GET, POST, PATCH, DELETE, OPTIONS')
    return response

    '''
      @TODO:
      Create an endpoint to handle GET requests
      for all available categories.
      '''


@app.route('/categories')
def getAllCategories():
    categories = Category.query.all()
    return categories.format()

    '''
          @TODO:
          Create an endpoint to handle GET requests for questions,
          including pagination (every 10 questions).
          This endpoint should return a list of questions,
          number of total questions, current category, categories.

          TEST: At this point, when you start the application
          you should see questions and categories generated,
          ten questions per page and pagination at the bottom of the screen for three pages.
          Clicking on the page numbers should update the questions.
          '''


@app.route('/questions')
def getAllQuestions():
    page = request.args.get('page', 1, type=int)
    questions = Question.query.limit(10).offset(page-1*10).all()

    return data

    '''

         @TODO:
         Create an endpoint to DELETE question using a question ID.

         TEST: When you click the trash icon next to a question, the question will be removed.
         This removal will persist in the database and when you refresh the page.
         '''


@app.route("/questions/<int question_id>", methods=["DELETE"])
def deleteQuestion(question_id):
    Question.query.get(question_id)
    Question.delete()

    '''
  @TODO: 
  Create an endpoint to POST a new question, 
  which will require the question and answer text, 
  category, and difficulty score.

  TEST: When you submit a question on the "Add" tab, 
  the form will clear and the question will appear at the end of the last page
  of the questions list in the "List" tab.  
  '''

    '''
  @TODO: 
  Create a POST endpoint to get questions based on a search term. 
  It should return any questions for whom the search term 
  is a substring of the question. 

  TEST: Search by any phrase. The questions list will update to include 
  only question that include that string within their question. 
  Try using the word "title" to start. 
  '''

    '''
  @TODO: 
  Create a GET endpoint to get questions based on category. 

  TEST: In the "List" tab / main screen, clicking on one of the 
  categories in the left column will cause only questions of that 
  category to be shown. 
  '''


@app.route("/categories/<int:categoty_id>/questions")
def questionsCategory(category_id):
    questions = Question.query.filter(Question.category == category_id).all()
    data = {
        'questions': [questions],
        'totalQuestions': Question.query.count(),
        'currentCategory': Category.query.get(category_id)
    }
    return data

    '''
  @TODO: 
  Create a POST endpoint to get questions to play the quiz. 
  This endpoint should take category and previous question parameters 
  and return a random questions within the given category, 
  if provided, and that is not one of the previous questions. 

  TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not. 
  '''

    '''
  @TODO: 
  Create error handlers for all expected errors 
  including 404 and 422. 
  '''


@app.errorhandler(422)
def error422():
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    })


@app.errorhandler(404)
def error404():
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
    })