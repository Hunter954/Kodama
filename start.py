import os
from gunicorn.app.wsgiapp import run

port = os.environ.get('PORT', '8080')
os.environ.setdefault('WEB_CONCURRENCY', '1')

if __name__ == '__main__':
    import sys
    sys.argv = [
        'gunicorn',
        'app:app',
        '--bind', f'0.0.0.0:{port}',
        '--workers', os.environ.get('WEB_CONCURRENCY', '1'),
    ]
    run()
