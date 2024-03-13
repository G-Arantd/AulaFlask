from app import db

from app.Models.Tabelas import Tabela

def get_tabela(id: int):
    tabela = Tabela.query.filter_by(id=id).first()
    
    if tabela:
        return tabela
    else:
        return None
    
def get_tabela_all():
    tabela = Tabela.query.all()
    
    if tabela:
        return tabela
    else:
        return None

def create_tabela(username: str, password: str):
    
    try:
        new_tabela = Tabela(username=username, password=password)
        db.session.add(new_tabela)
        db.session.commit()
    
        return True
    
    except Exception as e:
        
        return False
    
def update_tabela(id: int, username: str, password: str):
    
    try:
        tabela = get_tabela(id=id)
        
        if tabela:
            tabela.username = username
            tabela.password = password
            
            db.session.commit()
            
            return True
        
        else:
            
            return False
        
    except Exception as e:
        db.session.rollback()
        
        return False

def delete_tabela(id: int):
    try:
        tabela = get_tabela_all(id=id)
        
        if tabela:
            db.session.delete(tabela)
            db.session.commit()
            
            return True
        
        else: 
            return False
        
    except Exception as e:
        db.session.rollback()
        
        return False