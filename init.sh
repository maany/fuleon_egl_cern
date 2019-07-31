#!/bin/bash

echo "*/${REFRESH_INTERVAL} * * * * root /usr/bin/python3 /code/manage.py fetch_data >> /code/fetch_data_output" >> /etc/crontab
service cron start
python3 manage.py runserver 0.0.0.0:8000