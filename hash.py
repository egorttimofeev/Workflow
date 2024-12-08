import bcrypt
password = b'3'
 
salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(password, salt)

print(hashed)