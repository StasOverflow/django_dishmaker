#!/bin/bash

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Create superuser
# echo "from django.contrib.auth.models import User; \
# User.objects.create_superuser('$ADMIN_NAME', '$ADMIN_MAIL', '$ADMIN_PASS')" | python manage.py shell

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000