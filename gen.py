# password generator
import random

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJLKMNOPQRSTUVWXYZ0123456789!#$%&/()=?*"

def password_generator(length:int=16):
    res = []
    for i in range(length):
        res.append(random.choice(characters))
    return "".join(res)
