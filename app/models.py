from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class userFavs(db.Model):
	username = db.Column(db.String, primary_key=True)
	place = db.Column(db.String)
	food = db.Column(db.String)

	def __int__(self, username, place, food):
		self.username = username
		self.place = place
		self.food = food

	def __repr__(self):
		return f'<User-Place-Food : {self.username}-{self.place}-{self.food}'