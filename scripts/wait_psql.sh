#!/bin/sh

while ! nc -z psql 5432; do
  echo "🟡 Waiting for Postgres Database Startup (psql 5432) ..."
  sleep 2
done

echo "✅ Postgres Database Started Successfully (psql 5432)"