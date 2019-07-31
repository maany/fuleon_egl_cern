#!/bin/bash

echo "*/${REFRESH_INTERVAL} * * * * root cd /code && python3 manage.py fetch_data >> /code/fetch_data_output" >> /etc/crontab
service cron start
python3 manage.py runserver 0.0.0.0:8000