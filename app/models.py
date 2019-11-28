from . import db
from werkzeug.security import generate_password_hash,check_password_hash

class Quote:
    '''
    Quote class to define the quote objects
    '''
    def __init__(self,id,author,quote):
        self.id=id
        self.author=author
        self.quote=quote
        

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(),unique = True,index = True)
    pass_word = db.Column(db.String(255))
    
    
    @property
    def

    def __repr__(self):
        return f'User {self.username}'        
        