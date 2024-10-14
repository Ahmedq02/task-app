#!/bin/sh

# Fail on any error.
set -e

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

