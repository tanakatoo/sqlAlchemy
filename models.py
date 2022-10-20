from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

def connect_db(app):
    db.app=app
    db.init_app(app)
    app.app_context().push()
    

# models go here
class Pet(db.Model):
    __tablename__ = "pets"
    
    def __repr__(self):
        return f"<Pet id={self.id} name={self.name} species={self.species} hunger={self.hunger}>"
    
    id=db.Column(db.Integer,
                 primary_key=True,
                 autoincrement=True
                 )
    name=db.Column(db.String(50),
                   nullable=False,
                   unique=True)
    species = db.Column(db.String(30))
    hunger = db.Column(db.Integer, 
                       nullable=False,
                       default=20)