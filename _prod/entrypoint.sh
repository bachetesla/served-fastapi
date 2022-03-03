#!/bin/bash

set -a # automatically export all variables
source .env
set +a

#!/bin/sh

if [ "$DB" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

exec "$@"