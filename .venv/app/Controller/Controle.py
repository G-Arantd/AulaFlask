from flask import jsonify
from app.Services.Crud import *

def get_user(data):
    
    id: int = data.get("id")
    
    user = get_tabela(id)
    
    if user:
        
        profile_info = {
            "username": user.usename,
            "password": user.password
        }
        
        return jsonify(profile_info)
    
    else:
        
        return jsonify({"message": "Não existe este usuário."}), 400
        
    
def get_users():
    
    users = get_tabela_all()
    
    users_list = []
    
    if users:
        
        for user in users:
            
            users_list.append({
                "username": user.username,
                "password": user.password 
            })
            
        return jsonify(users_list)
    
    else:
        
        return jsonify({"message": "Não possuí usúarios registrados."})
    
def create_user(data):
    
    username: str = data.get("username")
    password: str = data.get("password")
    
    if not username or not password:
        
        return jsonify({"message": "as informações são vazias para serem registradas."})
    
    result = create_tabela(username, password)
    
    if result:
        
        return jsonify({"message": "Usuário criado com sucesso."})
    
    else:
        
        return jsonify({"message": "Falha ao criar o Usuário."})
    
def update_user(data):
    
    id: int = data.get("id")
    username: str = data.get("username")
    password: str = data.get("password")
    
    result = update_tabela(id, username, password)
    
    if result:
        return jsonify({"message": "Usuário atualizado com sucesso!"})
    
    else:
        return jsonify({"message": "Falhar em atualizar as informações do usuário"})
    
def delete_user(data):
    
    id: int = data.get("id")
    
    if id:
        
        result = delete_tabela(id)
        
        if result:
            return jsonify({"message": "Usuário removido com sucesso."}), 200
            
        else:
            return jsonify({"message": "Falha ao remover o Usuário"}), 500
    
    else:
        return jsonify({"message": "Falha ao deletar a informação, pois o Id é vazio"}), 401