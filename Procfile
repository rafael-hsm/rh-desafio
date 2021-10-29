# - Aplica as migrações automaticamente no heroku
release: python manage.py migrate --noinput
# - Configuração do "log file" heroku
web: gunicorn rh_desafio.wsgi --log-file -