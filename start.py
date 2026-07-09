import os
import sys
from gunicorn.app.wsgiapp import run


def get_port():
    value = os.environ.get('PORT') or os.environ.get('RAILWAY_PORT') or '8080'
    value = str(value).strip()
    # Se o Railway/Start Command deixar literal tipo "$PORT", não deixa o Gunicorn quebrar.
    if not value.isdigit():
        value = '8080'
    return value


if __name__ == '__main__':
    port = get_port()
    workers = os.environ.get('WEB_CONCURRENCY', '1')
    if not str(workers).isdigit():
        workers = '1'

    sys.argv = [
        'gunicorn',
        'app:app',
        '--bind', f'0.0.0.0:{port}',
        '--workers', workers,
        '--threads', '4',
        '--timeout', '120',
        '--access-logfile', '-',
        '--error-logfile', '-',
    ]
    run()
