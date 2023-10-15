# api_final
## Описание.
Проект Yatube - интернет-ресурс, на котором можно создавать посты на разные темы, добавлять к ним комментарии. Читать посты и комментарии могу любые пользователи сайта. На данном ресурсы Вы сможете делиться с другими людьми своими достижениями, впечатлениями и многим другим. Добро пожаловать на Yatube!

## Установка.
### Клонировать репозиторий и перейти в него в командной строке:

git clone https://github.com/OwnGlory/api_final_yatube
cd kittygram

### Cоздать и активировать виртуальное окружение:

python3 -m venv venv
source venv/Source/activate

### Установить зависимости из файла requirements.txt:

python3 -m pip install --upgrade pip
pip install -r requirements.txt

### Выполнить миграции:

python3 manage.py migrate

### Запустить проект:

python3 manage.py runserver

## Примеры запросов.

### GET:
http://127.0.0.1:8000/api/v1/posts/
http://127.0.0.1:8000/api/v1/posts/{id}/

### POST:
http://127.0.0.1:8000/api/v1/posts/
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/

### DELETE:
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/