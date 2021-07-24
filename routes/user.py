from models.user import User
from fastapi import APIRouter
from config.mongo import conn
from schemas.user import userEntity, usersEntity
from models.user import User
user = APIRouter()

@user.get('/users')
def getUsers():
    return usersEntity(conn.local.user.find())

@user.get('/user/{id}')
def getUsersById():
    return 'get user by id'

@user.post('/users')
def createUser(user: User):
    newUser = dict(user)
    id =conn.local.user.insert_one(newUser).inserted_id
    return str(id)

@user.delete('users/{id}')
def deleteUserById():
    return 'delete user'

@user.put('/users/{id}')
def updateUserById():
    return 'update user by id'
