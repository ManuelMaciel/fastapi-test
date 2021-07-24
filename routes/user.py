from fastapi import APIRouter

user = APIRouter()

@user.get('/users')
def getUsers():
    return 'users'

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
