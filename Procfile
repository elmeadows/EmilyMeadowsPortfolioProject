release: python manage.py migrate && python manage.py collectstatic --noinput
web: gunicorn web_django.wsgi:application
