from app import db

from app.Models.RegistrationsTable import RegistrationsTable

def get_table(id: int):
    table = RegistrationsTable.query.filter_by(id=id).first()
    
    if table:
        return table
    else:
        return None
    
def get_table_all():
    table = RegistrationsTable.query.all()
    
    if table:
        return table
    else:
        return None

def create_table(username: str, password: str):
    
    try:
        new_table = RegistrationsTable(username=username, password=password)
        db.session.add(new_table)
        db.session.commit()
    
        return True
    
    except Exception as e:
        
        return False
    
def update_table(id: int, username: str, password: str):
    
    try:
        table = get_table(id=id)
        
        if table:
            table.username = username
            table.password = password
            
            db.session.commit()
            
            return True
        
        else:
            
            return False
        
    except Exception as e:
        db.session.rollback()
        
        return False

def delete_table(id: int):
    try:
        table = get_table(id=id)
        
        if table:
            db.session.delete(table)
            db.session.commit()
            
            return True
        
        else: 
            return False
        
    except Exception as e:
        db.session.rollback()
        
        return False