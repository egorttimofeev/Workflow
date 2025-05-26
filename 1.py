import bcrypt

# Пароль для хеширования
password = "1"

# Хеширование пароля
hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

print(f"Исходный пароль: {password}")
print(f"Хешированный пароль: {hashed}")