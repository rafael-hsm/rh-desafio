# - Aplica as migrações automaticamente no heroku
release: python manage.py migrate --noinput
# - Configuração do "log file" heroku
web: gunicorn rh-desafio.wsgi --log-file -