@echo off
color c
cls
C:\Python34\python.exe manage.py migrate --fake Apps.BookingManager zero
pause