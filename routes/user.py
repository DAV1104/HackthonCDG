from fastapi import APIRouter, Depends
from config.db import conn
from models.user import users
from schemas.user import User
from sqlalchemy import select
from cryptography.fernet import Fernet
from passlib.context import CryptContext

user = APIRouter(prefix = '/user', tags=['user'])
crypt = CryptContext(schemes=["bcrypt"])
secret_key = "53b280f8b866fbb9ee893067f45c7175570b0f6e"

algorithm = "HS256"

key = Fernet.generate_key()
f = Fernet(key)


def get_password_hash(password: str):
    return crypt.hash(password)

@user.get('/u')
async def get_users():
    busqueda = conn.local.execute(users.select()).fetchall()
    print(busqueda)
    return busqueda

@user.post('/userp')
def create_user(user: User):
    new_user = user.dict()
    new_user["password"] = get_password_hash(user.password)
    result = conn.execute(users.insert().values(new_user))
    print(user)
    print (new_user)
    print(result)
    rows_affected = result.rowcount
    print(rows_affected)
    return "Hola"

@user.put('/')
async def helloworld():
    return "helloworld"

@user.delete('/')
async def helloworld():
    return "helloworld"