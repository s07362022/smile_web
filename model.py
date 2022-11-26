from app import db,bcrypt

class UserReister(db.Model):
    __tablename__ = 'ncku_w'#'UserRgeisters'
    __table_args__ = {'extend_existing': True} 
    
    index = db.Column(db.Integer, primary_key=True,autoincrement=True, nullable=True) 
    id = db.Column(db.String(100), unique=True, nullable=False)
    username = db.Column(db.String(100),  nullable=False)
    hpname =  db.Column(db.String(100), nullable=False)
    time_ = db.Column(db.String(100), nullable=False)
    #email = db.Column(db.String(100), unique=True, nullable=False)
    #password2 = db.Column(db.String(100), nullable=False) 
    __mapper_args__ = {'primary_key':[index]}
    def __repr__(self):
        return 'username:%s, id:%s' % (self.username, self.id)
    
  