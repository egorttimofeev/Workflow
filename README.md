# Workflow 
## Программа для учета рабочего времени сотрудников
***
### Чтобы открыть программу, скачайте репозиторий, например, в формате zip-файла, разархивируйте
#### Для Windows:
Откройте папку For_Windows, далее dist и запустите программу Workflow.exe
***
#### Для MacOS:
Откройте папку For_MacOs, далее dist и запустите программу Workflow.app
***
### Чтобы поменять базу данных на вашу откройте файл config.txt и вставьте туда ссылку на свою бд, должны быть 2 таблицы Users и Activities, в которых должны быть строки:
Users:
id_user (первичный ключ)
First_name
Last_name
Surname
Login
Password
Role
Phone_number
Birthday
Passport
Place_of_registration
Place_of_residence
Family
Conscription
Education
***
Activities:
id_activity (первичный ключ)
id_user (вторичный ключ)
activity_name
duration
date
is_busy
***
### Чтобы зашифровать пароль, откройте в любом компиляторе (например, VS code) файл hash.py, напишите во второй строке в ковычках свой пароль и запустите файл, в терминале в ковычках будет прописан зашифрованный пароль, его вставьте в своей бд в Users\Password для сотрудника
