#!/bin/sh

# Fail on any error.
set -e

poetry run python manage.py migrate entries 0002

# Run database migrations.
echo "Running database migrations..."
make migrate

# Create a passkey
echo "Creating a passkey..."
make createpasskey

# Collect static files.
echo "Collecting static files..."
make collectstatic

# Start the server.
echo "Starting the server..."
exec "$@"

