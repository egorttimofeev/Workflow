import bcrypt
password = b'1'
 
salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(password, salt)

print(hashed)