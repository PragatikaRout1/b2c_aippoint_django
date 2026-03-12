#!/bin/bash
# Start Daphne in the background
echo "Starting Daphne server..."
daphne -b 0.0.0.0 -p 8004 resume_parser_mongodb.asgi:application &
 
# Optional: Wait a little for Daphne to start
sleep 10
 
# Start Celery worker
echo "Starting Celery worker..."
celery -A resume_parser_mongodb worker --loglevel=info --pool=threads -E
 