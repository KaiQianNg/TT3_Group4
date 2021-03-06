from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class USER(db.Model,UserMixin):
	__tablename__ = 'USER'
	User_ID = db.Column(db.Integer, primary_key=True)
	Name = db.Column(db.String(50), nullable=False)
	Age = db.Column(db.Integer, nullable=False)
	Birthday = db.Column(db.DateTime, nullable=False)
	Email = db.Column(db.String(50), nullable=False)
	Phone = db.Column(db.String(50), nullable=False)
	City = db.Column(db.String(50), nullable=False)
	Country = db.Column(db.String(50), nullable=False)
	Password = db.Column(db.String(100), nullable=False)
	def get_id(self):
		return self.User_ID
class LIKED_POST(db.Model):
	__tablename__ = 'LIKED_POST'
	Ref_Num = db.Column(db.Integer, primary_key=True)
	User_ID  = db.Column(db.Integer, nullable=False)
	Post_ID  = db.Column(db.Integer, nullable=False)
class POST(db.Model):
	__tablename__ = 'POST'
	Post_ID  = db.Column(db.Integer, nullable=False, primary_key=True)
	User_ID  = db.Column(db.Integer, nullable=False)
	Post_Title = db.Column(db.String(50), nullable=False)
	Post_Description = db.Column(db.String(200), nullable=False)
	Post_image = db.Column(db.String(300), nullable=False)
class POST_COMMENT(db.Model):
	__tablename__ = 'POST_COMMENT'
	Comment_ID = db.Column(db.Integer, primary_key=True)
	User_ID  = db.Column(db.Integer, nullable=False)
	Post_ID  = db.Column(db.Integer, nullable=False)
	Comment = db.Column(db.Text, primary_key=True)