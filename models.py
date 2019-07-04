from flask_sqlalchemy import SQLAlchemy
#from datetime import datetime
from sqlalchemy import Column, Integer,DateTime,String,ForeignKey
db = SQLAlchemy()

class Paper(db.Model):
    __tablename__ = "paper"
    paper_id = db.Column(db.Integer, primary_key=True)
    examname = db.Column(db.String, nullable=False)
    subject = db.Column(db.String, nullable=False)
    series = db.Column(db.String)
    exambody = db.Column(db.Integer, nullable=False)
    examdate=db.Column(db.DateTime, nullable=False) #default=datetime.datetime.utcnow)

class Question(db.Model):
    __tablename__ = "question"
    paper_id = Column(Integer,ForeignKey("paper.paper_id"), nullable=False)
    question_id = Column(Integer, primary_key=True)
    question = Column(String, nullable=False)
    option_a = Column(String, nullable=False)
    option_b = Column(String, nullable=False)
    option_c = Column(String, nullable=False)
    option_d = Column(String, nullable=False)
    right_option=Column(String,nullable=False)
    difflevel=Column(db.SMALLINT)
    explanation = Column(String)
