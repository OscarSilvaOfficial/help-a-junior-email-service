from api.configs.enviroment import SECRET_KEY
import os, re, jwt

def encript_passwd(passwd):
    response = jwt.encode(
        {"passwd": passwd}, 
        SECRET_KEY, 
        algorithm="HS256"
    )
    return response

def decript_passwd(passwd):
    response = jwt.decode(
        passwd, 
        SECRET_KEY, 
        algorithms="HS256"
    )
    return response['passwd']
    