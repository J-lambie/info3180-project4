from . import db  
class User(db.Model):   
    __tablename__='user'
    user_id = db.Column(db.Integer, primary_key=True)
    email=db.Column(db.String(80))
    name = db.Column(db.String(80))     
    password= db.Column(db.String(80)) 
    image=db.Column(db.String(80))

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.user_id)  # python 2 support
        except NameError:
            return str(self.user_id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.first_name)
        
class Wishlist(db.Model):
    __tablename__='wishlist'
    wishlist_id=db.Column(db.Integer, primary_key=True,autoincrement=True)
    title=db.Column(db.String(80))
    url=db.Column(db.String(100))
    description=db.Column(db.String(250))
    thumbnail=db.Column(db.String(100))
    user_id=db.Column(db.Integer,db.ForeignKey('user.user_id'),autoincrement=False)

    def __init__(self,title,url,description,thumbnail,user_id):
        self.title=title
        self.url=url
        self.description=description
        self.thumbnail=thumbnail
        self.user_id=user_id
        
    def is_authenticated(self):
        return True
        
    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support