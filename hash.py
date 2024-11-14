import bcrypt
password = b'2'
 
salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(password, salt)

print(hashed)