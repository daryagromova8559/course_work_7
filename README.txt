Настройка проекта через Docker
После клонирования введите следующие команды (на Windows, для другой системы команды отличаются) в консоли в папке проекта: docker-compose build docker-compose up
Настройка проекта (без Docker)
После клонирования введите следующие команды (на Windows, для другой системы команды отличаются) в консоли в папке проекта:
python -m venv venv

venv/scripts/activate

pip install -r requirements.txt

Не забудьте активировать миграции, чтобы связи с БД работали, лучше использовать новую БД:
python manage.py migrate

Redis устанавливается на wsl (для windows), команда redis-server

Внесите свои настройки, используя файл .env.example, переименуйте в .env

Запускается проект командой

python manage.py runserver

Зарегистрируйте суперпользователя командой
python manage.py csu

В Postman заполнить во вкладке headers "Autorization" = Bearer [ваш_токен_без_ковычек] Токен можно получить по адресу "localhost"/users/login/

Можно загрузить фикстуры в корне проекта

python manage.py loaddata [данные].json

Запустите в терминале celery worker:
celery -A config worker -l INFO # для Mac и Linux

celery -A config worker -l INFO -P eventlet # для Windows

Запустите во второй вкладке celery beat:
celery -A config beat -l info -S django

Зайдите в телеграм бот, конфигурируйте (шаги 1-6) и нажмите /start Гайд для конфигурации