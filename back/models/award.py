from db_connect import db

class award(db.Model):

    __tablename__ = 'award'

    award_id = db.Column(db.Integer, primary_key=True, autoincrement=True) 
    name = db.Column(db.String(45), nullable = False)
    description = db.Column(db.String(45), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)

    def __init__(self, name, description):
        self.name = name
        self.description = description