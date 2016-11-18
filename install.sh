#!/bin/bash
# teste jenkins
apt-get update
apt-get -y remove gunicorn
apt-get -y install python3-pip libmysqlclient-dev libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk
sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password password framework'
sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password framework'
sudo apt-get -y install mysql-server
pip3 install -r requirements.txt
rm -r /etc/init/gunicorn.conf
rm -r /etc/nginx/sites-available/django
ln -s /home/django/framework-base/gunicorn.conf /etc/init/gunicorn.conf
ln -s /home/django/framework-base/django /etc/nginx/sites-available/django
service mysql start
echo 'create database if not exists framework;' | mysql -u root -pframework
python3 manage.py makemigrations
python3 manage.py migrate
mysql -u root -pframework framework<framework.sql
initctl reload-configuration
service nginx restart
service gunicorn restart
