# FastAPI_training_task
Тестовое задание для 5D HUBE

### Логика работы
Реализован http-сервис, который обрабатывает поступающие запросы. 
Сервер стартует по адресу http://127.0.0.1:8080 (значение по умолчанию, можно изменять).

### Стек технологий
FastAPI
SQLAlchemy
PostgreSQL
Alembic
Docker

### Функционал
1. POST-запрос для получения сокращённого варианта переданного URL.
2. GET-запрос для возврата оригинального URL (редирект на первоначальный URL).

### Зависимости
Для управления зависимостями в проекте используется pip. Список зависимостей хранится в файле requirements.txt

### Установка и запуск
1. Установите Python и pip, если они не установлены.
2. Установите все в зависимости от установки pip.
3. Создайте в корне проекта файл .env и сохраните в нем все переменные окружения.
4. Создайте и примените миграции.
```bash 
pip install alembic  
```
```bash 
alembic init alembic    
```
В файле alembic.ini укажите данные для подключения к Вашей БД
В файле .env в директории alembic импортируйте Вашу модель в target_metadata
```bash 
alembic revision --autogenerate -m "Initial migration"   
```
```bash 
alembic upgrade head   
```
5. Запустите приложение.
```bash 
python -m main
```
6. Проверьте работу API. Используйте Postman или swagger для тестирования эндпоинтов:
- POST - / - получить сокращённый вариант переданного URL 
- GET - /{short_id} - возврат оригинального URL.

### Докер

Для создания контейнера в докере нужно подобрать в консоли следующие команды: 
```bash 
docker network create url_shortener_net 
```
```bash 
docker run -d --network=url_shortener_net --name=postgres_container -p 5432:5432 -e POSTGRES_DB=url_shortener -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=password postgres:15-alpine 
```
```bash 
docker-compose up -d --build
```

### 💡 **Автор**
Павлухина Ксения 
[GitHub](https://github.com/XeniaPav/)