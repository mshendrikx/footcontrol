from flask_login import UserMixin
from . import db

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

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    password = db.Column(db.String(1000))
    email = db.Column(db.String(100))
    phone = db.Column(db.Biginteger)   
    admin = db.Column(db.Integer)  
    groupid = db.Column(db.Integer)   
    groupadm = db.Column(db.Integer)  

class Player(db.Model):
    groupid = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, primary_key=True)
    posid = db.Column(db.Integer)
    admin = db.Column(db.Integer)
    fixed = db.Column(db.Integer)
    
class Skill(db.Model):
    groupid = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, primary_key=True)
    posid = db.Column(db.Integer)
    value = db.Column(db.Integer)
    
class Vote(db.Model):
    groupid = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, primary_key=True)
    playerid = db.Column(db.Integer, primary_key=True)
    posid = db.Column(db.Integer)
    value = db.Column(db.Integer)
    
class Attendance(db.Model):
    gameid = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Biginteger)
    checkin = db.Column(db.Biginteger)
    
class Team(db.Model):
    gameid = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, primary_key=True)
    teamid = db.Column(db.Integer)
    