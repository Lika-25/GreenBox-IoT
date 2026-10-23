#!/bin/bash
cd "/mnt/d/1 курс МАГИСТРАТУРА/Проектування та моделювання IoT систем/лаб 1/GreenBox"
source env/bin/activate
exec uwsgi --ini uwsgi.ini
