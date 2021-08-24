from db_connect import db

class user(db.Model):    
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True) 
    email = db.Column(db.String(255), nullable=False,
    unique = True)
    password = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(45), nullable = False)
    description = db.Column(db.String(255))
    image = db.Column(db.String(255))
    

    def __init__(self, email, password, name):
        self.email = email
        self.password = password
        self.name = name
    