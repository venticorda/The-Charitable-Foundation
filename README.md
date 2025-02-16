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

## Примеры функций и возможностей

### Создание благотворительного проекта

Супер пользователь может создать новый благотворительный проект, указав его название, описание и полную сумму.

Пример запроса:
```json
POST /charity_project/
{
    "name": "Помощь бездомным кошкам",
    "description": "Сбор средств на корм и лечение бездомных кошек",
    "full_amount": 100000
}
```

### Пожертвование на существующий проект

Пользователь может сделать пожертвование на существующий проект, указав сумму пожертвования и комментарий.

Пример запроса:
```json
POST /donation/
{
    "full_amount": 5000,
    "comment": "Помощь бездомным кошкам"
}
```

### Отслеживание прогресса проектов

Пользователь может отслеживать прогресс всех проектов, включая общую собранную сумму и оставшуюся до цели.

Пример запроса:
```json
GET /charity_project/
```

Пример ответа:
```json
[
  {
    "name": "Помощь бездомным кошкам",
    "description": "Сбор средств на корм и лечение бездомных кошек",
    "full_amount": 100000,
    "id": 1,
    "invested_amount": 50000,
    "fully_invested": false,
    "create_date": "2025-02-15T18:07:45.356441"
  },
  {
    "name": "Помощь бездомным собакам",
    "description": "Сбор средств на корм и лечение бездомных собак",
    "full_amount": 100000,
    "id": 2,
    "invested_amount": 0,
    "fully_invested": false,
    "create_date": "2025-02-15T18:08:09.743501"
  }
]
```

## CI/CD

Проект настроен для автоматического запуска тестов и проверки кода при каждом пуше в репозиторий с использованием GitHub Actions. Конфигурация находится в файле `.github/workflows/ci.yml`.

### Настройка CI/CD

1. Создайте файл конфигурации для GitHub Actions:
    ```yaml
    name: CI

    on:
      push:
        branches:
          - main
      pull_request:
        branches:
          - main
    
    jobs:
      build:
        runs-on: ubuntu-latest

        steps:
        - name: Checkout code
          uses: actions/checkout@v2
    
        - name: Set up Python
          uses: actions/setup-python@v2
          with:
            python-version: 3.10.16
    
        - name: Install dependencies
          run: |
            python -m pip install --upgrade pip
            pip install -r requirements.txt
    
        - name: Set up environment variables
          run: echo "DATABASE_URL=sqlite+aiosqlite:///./test.db" >> $GITHUB_ENV
    
        - name: Run tests
          run: |
            alembic upgrade head
            pytest"

    ```

2. Коммит и пуш изменений в репозиторий:
    ```bash
    git add .github/workflows/ci.yml
    git commit -m "Add CI/CD configuration"
    git push origin main
    ```

Теперь каждый раз, когда вы пушите изменения в ветку `main`, GitHub Actions будет автоматически запускать тесты и проверять код.

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
