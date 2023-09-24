# Используйте официальный образ Python
FROM python:3.11

# Установите переменную окружения для отключения буферизации вывода
ENV PYTHONUNBUFFERED 1

# Установите рабочую директорию в контейнере
WORKDIR /Weatherdir

# Установите зависимости вашего проекта
COPY requirements.txt /Weatherdir/
RUN pip install -r requirements.txt

# Копируйте содержимое проекта в контейнер
COPY . /Weatherdir/

CMD ["python manage.py runserver 0.0.0.0:8000"]
