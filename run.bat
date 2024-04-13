@echo off

REM Open a new console window and execute the main.py script
start cmd.exe /k python main.py

REM Open another new console window and start the Django development server using manage.py
start cmd.exe /k python manage.py runserver 4500

exit
