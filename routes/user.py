from fastapi import APIRouter, Response, status
from starlette.status import HTTP_204_NO_CONTENT

#Models and Schemas
from config.db import conn
from models.user import user
from schemas.user import User

#utils
from config.user import key_f 

users = APIRouter()

@users.get('/user', response_model=User, tags=['users'])
def get_users():
    users = conn.execute(user.select()).fetchall()
    return users

@users.get('/user/{id}', tags=['users'])
def get_user(id: int):
    user_information = conn.execute(user.select().where(user.c.id == id)).first()
    if user_information == None:
        return Response(status_code=HTTP_204_NO_CONTENT)
    return user_information

@users.post('/user', response_model=User, tags=['users'])
def create_users(information: User):
    user_data = {
        'name': information.name,
        'email': information.email,
    }
    user_data['password'] = key_f.encrypt(information.password.encode('utf-8'))
    
    result = conn.execute(user.insert().values(user_data))
    return 'new user added sucessfully'

@users.delete('/user/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['users'])
def delete_user(id: int):
    result = conn.execute(user.delete().where(user.c.id == id))
    if result == None:
        return Response(status_code=HTTP_204_NO_CONTENT)
    return 'user deleted successfully'

@users.put('/user/{id}', response_model=User, tags=['users'])
def update_user(id: int, information: User):
    result = conn.execute(user.update().values(name=information.name,
                        email=information.email, 
                        password=key_f.encrypt(information.password.encode('utf-8'))).where(user.c.id == id))
    return 'user information updated'