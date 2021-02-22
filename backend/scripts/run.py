import os
import sys

def run_wsgi_application():
    workers = sys.argv[1] if len(sys.argv) > 1 else 1
    os.system(f'gunicorn -w {workers} --access-logfile - "backend.wsgi:app"')