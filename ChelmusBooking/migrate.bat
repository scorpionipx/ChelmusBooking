@echo off
color c
cls
C:\Python34\python.exe manage.py makemigrations
C:\Python34\python.exe manage.py migrate
pause