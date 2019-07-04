import os

from flask import Flask,redirect,url_for,session,render_template, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models import *

app = Flask(__name__)


if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


#engine = create_engine(os.getenv("DATABASE_URL"))
#db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return render_template("index.html",message="")

@app.route("/newpaper",methods=['POST','GET'])
def newpaper():
    return render_template("newform.html")


@app.route("/oldpaper",methods=['POST','GET'])
def oldpaper():
    papers=Paper.query.all()
    return render_template("oldpaper.html",papers=papers)

@app.route("/paper/<int:paper_id>",methods=['POST','GET'])
def paper(paper_id):
    currentPaper=Paper.query.filter_by(paper_id=paper_id).first()
    return render_template("question.html",paper=currentPaper)

@app.route("/questionadd/<int:paper_id>",methods=['POST'])
def questionadd(paper_id):
    currentPaper=Paper.query.filter_by(paper_id=paper_id).first()
    current_question=request.form.get("question")
    option_a=request.form.get("option_a")
    option_b=request.form.get("option_b")
    option_c=request.form.get("option_c")
    option_d=request.form.get("option_d")
    right_option=request.form.get("right_option")
    difflevel=int(request.form.get("difflevel"))
    explanation=request.form.get("explanation")
    #return render_template("error.html",message=demostr)
    question=Question(paper_id=paper_id,question=current_question,option_a=option_a,option_b=option_b,option_c=option_c,option_d=option_d,right_option=right_option,difflevel=difflevel,explanation=explanation)
    db.session.add(question)
    db.session.commit()
    return render_template("question.html",paper=currentPaper,message="Question Added successfully.")


@app.route("/paperadd",methods=['POST','GET'])
def paperadd():
    examName = request.form.get("exam_name")
    subject=request.form.get("subject")
    series=request.form.get("series")
    examBody=request.form.get("exambody")
    examdate=request.form.get("examdate")
    if len(series)>1:
            return render_template("error.html",message="Series must be in single charactor.(Like A,B,C,D)")
    paper=Paper(examname=examName,subject=subject,series=series,exambody=examBody,examdate=examdate)
    db.session.add(paper)
    db.session.commit()
    paperstr="Paper "+examName+" "+subject+" "+series+" "+examBody+" "+examdate+" successfully added."
    return render_template("index.html",message=paperstr)


if __name__ == '__main__':
    app.debug = True
    app.secret_key = "9+3as4jj+nnqlu16xu49xag0i4-x(=6e$ljzsdcctkej1nil94"
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
