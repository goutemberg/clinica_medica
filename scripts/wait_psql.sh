#!/bin/sh

while ! nc -z dpg-crutsju8ii6s738hnki0-a 5432; do
  echo "🟡 Waiting for Postgres Database Startup (dpg-crutsju8ii6s738hnki0-a 5432) ..."
  sleep 2
done

echo "✅ Postgres Database Started Successfully (dpg-crutsju8ii6s738hnki0-a 5432)"


