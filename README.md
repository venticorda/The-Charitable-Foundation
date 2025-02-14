# Благотворительный фонд для кошек

Этот проект направлен для сбора средств и поддержки различных благотворительных проектов, связанных с благополучием кошек. Пользователи могут создавать благотворительные проекты, пожертвовать на существующие и отслеживать прогресс каждого проекта.

## Как запустить проект
* Клонировать репозиторий и перейти в него в командной строке:

``` bash
git clone https://github.com/venticorda/cat_charity_fund.git
```
* Cоздать и активировать виртуальное окружение:

``` bash
python3 -m venv venv
```

* Если у вас Linux/macOS

    ``` bash
    source venv/bin/activate
    ```

* Если у вас windows

    ``` bash
    source venv/scripts/activate
    ```

* Установить зависимости из файла requirements.txt:

``` bash
python3 -m pip install --upgrade pip
```

``` bash
pip install -r requirements.txt
```

* Запуск сервера с авторестартом
``` bash
uvicorn app.main:app --reload
```
* Инициализируем Alembic в проекте
``` bash
alembic init --template async alembic
```
* Создание файла миграции
``` bash
alembic revision --autogenerate -m "migration_name"
```
* Применение миграций
``` bash
alembic upgrade head
```
* Запуск тестов
``` bash
pytest
```
## Использованные технологии
В проекте использовались следующие технологии:
- [Python 3.10.12](https://www.python.org/)
- [FastAPI 0.78.0](https://fastapi.tiangolo.com/)
- [Alembic 1.7.7](https://alembic.sqlalchemy.org/)
- [Google Cloud](https://console.cloud.google.com/)
- [Google Drive](https://drive.google.com/)
- [Google Sheets](https://workspace.google.com/products/sheets/)

## Автор:
[Даниил Варлащенко](https://github.com/venticorda)
***