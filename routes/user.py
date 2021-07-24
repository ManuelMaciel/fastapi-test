from fastapi import APIRouter
from config.db import conn
from schemas.user import userEntity, usersEntity

user = APIRouter()

@user.get('/users')
def getUsers():
    return usersEntity(conn.local.user.find())

@user.get('/user/{id}')
def getUsersById():
    return 'get user by id'

@user.post('/users')
def createUser():
    return 'create user'

@user.delete('users/{id}')
def deleteUserById():
    return 'delete user'

@user.put('/users/{id}')
def updateUserById():
    return 'update user by id'
