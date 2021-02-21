import os

def run_wsgi_application():
    os.system('gunicorn -w 4 --access-logfile - "backend.wsgi:app"')