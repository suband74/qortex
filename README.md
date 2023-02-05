# Backend-сервис "Каталог исполнителей и их альбомов с песнями"

## Общее описание

3. API доступно:
    - http://localhost:8000/swagger/
    - http://localhost:8000/redoc/
    - http://localhost:8000/api/v1/

## Установка проекта на локальный компьютер:

1. Должен быть предустановлен менеджер зависимостей `poetry`. Или установите `poetry` любым удобным способом. 
   Например: `curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -` 
2. Выполните клонирование репозитория: `https://github.com/suband74/qortex`
3. Затем выполните установку зависимостей проекта: `poetry install`
4. Установить docker и docker-compose. Инструкции по установке доступны в официальной документации.
5. В папке с проектом выполнить команду:
```
docker-compose up
```