#!/usr/bin/env bash
set -e

python manage.py collectstatic --noinput
python manage.py migrate --noinput

# Project module is "whatsapp_webapp"
exec gunicorn flopro_offical.wsgi:application \
  --bind 0.0.0.0:8000 \
  --workers 3 \
  --timeout 90
