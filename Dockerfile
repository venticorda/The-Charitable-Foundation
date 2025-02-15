# Используем официальный образ Python в качестве базового
FROM python:3.10.16-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файлы requirements.txt в контейнер
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir --no-deps -r requirements.txt

# Копируем все файлы проекта в контейнер
COPY . .

# Устанавливаем переменную окружения DATABASE_URL
ENV DATABASE_URL=sqlite+aiosqlite:///./test.db

# Выполняем команды для создания и применения миграций
RUN alembic revision --autogenerate -m "Initial migration" && alembic upgrade head

# Указываем команду для запуска приложения
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
