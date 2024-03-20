from app import db

class RegistrationsTable(db.Model):
    __tablename__ = "tb_registrations"
    id: int = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username: str = db.Column(db.String(128), nullable=False)
    password: str = db.Column(db.String(128), nullable=False)
    
def __init__ (self, username: str, password: str):
    self.username = username
    self.password = password
    
def __repr__(self):
    return f"Username: {self.username} \n Password: {self.password}"