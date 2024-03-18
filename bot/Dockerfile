FROM python:3.8

# Обновляем pip
RUN pip install --upgrade pip

# Копируем requirements.txt и устанавливаем зависимости
COPY ./bot/requirements.txt .
RUN pip install -r requirements.txt

# Копируем файлы вашего бота в рабочую директорию
COPY ./bot /app

# Устанавливаем рабочую директорию
WORKDIR /app

# Указываем команду запуска вашего бота (может быть изменено в зависимости от того, как запускается ваш бот)
CMD ["python", "main.py"]