from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    password = db.Column(db.String(1000))
    email = db.Column(db.String(100))
    phone = db.Column(db.Integer)   
    admin = db.Column(db.Integer)  
    groupid = db.Column(db.Integer)   
    groupadm = db.Column(db.Integer)  

class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    
class Position(db.Model):
    groupid = db.Column(db.Integer, primary_key=True)
    posid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    groupid = db.Column(db.Integer)
    date = db.Column(db.Biginteger)    

class Attendance(db.Model):
    gameid = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Biginteger)
    checkin = db.Column(db.Biginteger)
    teamid = db.Column(db.Integer)
    
class Team(db.Model):
    groupid = db.Column(db.Integer, primary_key=True)
    teamid = db.Column(db.Integer, primary_key=True)
    
class Player(db.Model):
    userid = db.Column(db.Integer, primary_key=True)
    groupid = db.Column(db.Integer, primary_key=True)
    position = db.Column(db.String(1))
    admin = db.Column(db.Integer)


    
    
    
class Draworder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    groupid = db.Column(db.Integer)
    position = db.Column(db.Integer)