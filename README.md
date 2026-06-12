# ⏱️ Workflow

Программа для учета рабочего времени сотрудников, разработанная с поддержкой Windows и macOS.

![HTML](https://img.shields.io/badge/HTML5-Desktop-E34C26?style=for-the-badge&logo=html5&logoColor=white)
![Database](https://img.shields.io/badge/Database-PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)

---

## 📋 Возможности

- **Учет рабочего времени** — отслеживание активности сотрудников
- **Управление пользователями** — хранение информации о сотрудниках
- **История активности** — логирование всех видов деятельности
- **Многоплатформность** — поддержка Windows и macOS

---

## 🛠 Технологический стек

- Frontend: HTML5
- Backend: PostgreSQL
- Кроссплатформа: Windows & macOS

---

## 💾 База данных

### Таблица Users (Пользователи)
- `id_user` — первичный ключ
- `First_name` — имя
- `Last_name` — фамилия
- `Surname` — отчество
- `Login` — логин
- `Password` — пароль (зашифрован)
- `Role` — должность
- `Phone_number` — телефон
- `Birthday` — дата рождения
- `Passport` — паспортные данные
- `Place_of_registration` — место регистрации
- `Place_of_residence` — место проживания
- `Family` — семейное положение
- `Conscription` — статус военного сбора
- `Education` — образование

### Таблица Activities (Активность)
- `id_activity` — первичный ключ
- `id_user` — внешний ключ (ссылка на Users)
- `activity_name` — вид активности
- `duration` — продолжительность
- `date` — дата
- `is_busy` — статус занятости

---

## 🚀 Установка и запуск

### Windows

1. Скачайте или клонируйте репозиторий
2. Откройте папку `For_Windows`
3. Перейдите в папку `dist`
4. Запустите `Workflow.exe`

### macOS

1. Скачайте или клонируйте репозиторий
2. Откройте папку `For_MacOs`
3. Перейдите в папку `dist`
4. Запустите `Workflow.app`

---

## 🔧 Настройка базы данных

Для подключения к собственной базе данных:

1. Откройте файл `config.txt`
2. Вставьте строку подключения к вашей БД
3. Убедитесь, что в базе созданы две таблицы:
   - `Users` — для хранения данных сотрудников
   - `Activities` — для логирования активности

**Пример строки подключения:**
```ini
[database]
connection_string = postgresql://user:password@localhost:5432/workflow_db
```

---

## 📁 Структура проекта

```
Workflow/
├── For_Windows/
│   └── dist/
│       └── Workflow.exe
├── For_MacOs/
│   └── dist/
│       └── Workflow.app
├── config.txt                 # Конфигурация БД
└── README.md
```

---

## 💡 Использование

1. **Запустите приложение** в зависимости от вашей ОС
2. **Введите учетные данные** для входа
3. **Управляйте активностью** сотрудников
4. **Просматривайте отчеты** по рабочему времени
