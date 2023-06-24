## 1. [Описание](#1)
## 2. [Запуск проекта](#2)
## 3. [Ссылки и примеры запросов](#3)
## 4. [Связаться со мной](#4)

---
## 1. Описание <a id=1></a>

Тестовое задание.
1. Создать новый проект на Django + Django rest framework.
2. Сделать стандартную авторизацию по токену.
3. Создать две модели:
    1. Request - заявка;
    2. RequestMessage - сообщение в заявке.
4. Реализовать следующие методы:
    1. Создание заявки;
    2. Отправка сообщения в заявку;
    3. Получение информации о заявке по ID;
    4. Получение списка сообщений по заявке;
    5. Получения списка заявок.

---
## 2. Запуск проекта <a id=2></a>

### Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:AliceYaroslavtseva/test.git
```
### Cоздать и активировать виртуальное окружение:
```
python -m venv venv # Для Windows
python3 -m venv venv # Для Linux и macOS
```
```
source venv/Scripts/activate # Для Windows
source venv/bin/activate # Для Linux и macOS
```
### Установить зависимости из файла requirements.txt:
```
python.exe -m pip install --upgrade pip # Для Windows
python3 -m pip install --upgrade pip # Для Linux и macOS
```
```
pip install -r requirements.txt
```
### Выполнить миграции:
```
python manage.py migrate # Для Windows
python3 manage.py migrate # Для Linux и macOS
```
### Создать суперпользователя:
```
winpty python manage.py createsuperuser # Для Windows
python manage.py createsuperuser # Для Linux и macOS
```
### Запустить проект:
```
python manage.py runserver # Для Windows
python3 manage.py runserver # Для Linux и macOS
```

---
## 3. Ссылки и примеры запросов <a id=3></a>

### Авторизацию по токену:
```
POST
http://127.0.0.1:8000/api/v1/api-token-auth/
```
Пример:
```
{
  "username": "alice",
  "password": "alice123"
}
```

### Создание заявки:
```
POST
http://127.0.0.1:8000/api/v1/request/
```
Пример:
```
{
  "username": "alice",
  "theme": "la-la-la",
  "phone_number": "+79674910773"
}
```

### Отправка сообщения в заявку:
```
POST
http://127.0.0.1:8000/api/v1/request/1(id заявки)/massages/
```
Пример:
```
{
  "message": "la-la-la",
  "request": "1"(id заявки)
}
```

### Получение информации о заявке по ID:
```
GET
http://127.0.0.1:8000/api/v1/request/2(id заявки)/
```

### Получение списка сообщений по заявке:
```
GET
http://127.0.0.1:8000/api/v1/request/1(id заявки)/massages/
```

### Получения списка заявок:
```
GET
http://127.0.0.1:8000/api/v1/request/
```
---

## 4. Связаться со мной <a id=4></a>

Алиса Ярославцева:
```
Telegram: t.me/hellfoxalice
GitHub: github.com/AliceYaroslavtseva
```
