
from datetime import datetime

from flask_login import current_user, login_required

from app.blueprints.main.forms import BasicForm
from . import main
from flask import flash, redirect, render_template, request, url_for
import requests
from app.models import Course, Question, Score, Topic, User, db



@main.route('/home')
def home():
   return render_template('home.html')


@main.route('/qnafeed')
def qnafeed():
   questions = Question.query.all()
   scores = Score.query.all()
   courses = Course.query.all()
   topics = Topic.query.all()
   
   deetails = db.session.query(Course,Question, Score ).\
               select_from(Course).\
               join(Question, Course.id == Question.course_id).\
               join(Score, Score.id == Question.score_id).all()

   return render_template('q&afeed.html', questions=questions)

@main.route('/quiz')
def quiz():
   course_id = 1
   questions = Question.query.filter_by(course_id=course_id).all()

   return render_template('quiz.html', questions=questions)
  




# @main.route('/report')
# @login_required
# def report():
#    form = ReportForm()
#    if request.method == 'POST' and form.validate_on_submit:
#       report_message = form.report_message.data
#           # report_date = datetime.utcnow() # do not need date in route. it will log based on db logging
#       question_id = currentquestionID # should read the current question_id
#       user_id = current_user.id



# def score():
#    tot_score = 0
#    question_score = 0
#    tot_percentage = 0

#    while(!submit):
#          score = question.score_id.score_points
#          question_score += score
#          on Click Next Button : 
         
#          if user.answer == question.answer:
#             tot_score += score

#          tot_percentage = tot_score / question_score * 100


         

# ######################################################################################

# @main.route("/search",methods =['POST','GET'])
# def main():
#     form = BasicForm()
#     return render_template("index.html",form = form)