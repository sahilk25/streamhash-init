#!/bin/bash

#scp Downloads/Current/streamview-website.zip ubuntu@3.6.93.197:~/ 
sudo apt-get install apache2

#mysql setup
echo "setting up mysql"
sudo apt-get install mysql-server -y
sudo mysql_secure_installation 
sudo mysql -u root -pstreamhash@123 -e "ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'streamhash@123';flush privileges;create database streamhash;"

mysql -u root -pstreamhash@123 streamhash < /home/ubuntu/Streamview/streamview-backend/DB/streamview.sql

echo "some php stuff"
sudo apt install build-essential -y
sudo add-apt-repository ppa:ondrej/php
sudo apt-get update -y 
sudo apt install php7.1 -y
sudo apt install php7.1-cli php7.1-xml php7.1-mysql \
php7.1-mbstring php7.1-gettext php7.1-curl php7.1-common \
php7.1-opcache php7.1-readline php7.1-mcrypt php7.1-zip -y


sudo sed -i 's/DirectoryIndex index.html index.cgi index.pl index.php index.xhtml index.htm/DirectoryIndex index.php index.cgi index.pl index.html index.xhtml index.htm/g' /etc/apache2/mods-enabled/dir.conf
sudo systemctl restart apache2
sudo apt-get install phpmyadmin php-mbstring php-gettext -y
sudo phpenmod mcrypt
sudo phpenmod mbstring
sudo sed -i "s/max_execution_time = 30/max_execution_time = -1/g;s/max_input_time = 60/max_input_time = -1/g;\
s/memory_limit = 32M/memory_limit = -1/g;s/post_max_size = 8M/post_max_size = 3000M/g;\
s/upload_max_filesize = 2M/upload_max_filesize = 2048M/g" /etc/php/7.1/apache2/php.ini

sudo systemctl restart apache2

sudo sed -i "s/AllowOverride None/AllowOverride All/3" /etc/apache2/apache2.conf
echo "Include /etc/phpmyadmin/apache.conf"  | tee -a /etc/apache2/apache2.conf   #(apeend)
sudo systemctl restart apache2
sudo apt-get install unzip
cd
unzip streamview-website.zip
sudo  cp -r /home/ubuntu/streamview-backend /var/www/html
sudo  cp -r /home/ubuntu/streamview-frontend /var/www/html
sudo chown -R www-data:www-data /var/www/html/

sudo apt-get install composer -y
cd /var/www/html/streamview-backend
composer update
sudo add-apt-repository ppa:chris-lea/redis-server
sudo apt-get update
sudo apt-get install redis-server -y
sudo service redis-server start
sudo apt-get install ffmpeg -y
sudo apt-get install nodejs -y
sudo apt-get install npm -y

echo "nginx shit"
cd
mkdir nginx
sudo apt-get install git gcc make zlib1g-dev -y
sudo apt-get install libpcre3-dev libssl-dev -y
cd nginx
git clone https://github.com/arut/nginx-rtmp-module
wget http://nginx.org/download/nginx-1.14.2.tar.gz
tar xzf nginx-1.14.2.tar.gz
cd nginx-1.14.2
sudo ./configure --add-module=/home/USERNAME/nginx/nginx-rtmp-module/ --with-http_ssl_module --prefix=/usr/local/nginx-streaming/
sudo make 
sudo make install



echo ".env changes"
cd 
cd /var/www/html/streamview-backend
sudo sed -i "s/DB_DATABASE=streamview/DB_DATABASE=streamhash/g;s/DB_PASSWORD=12345/DB_PASSWORD=streamhash@123/g" .env


echo "some permissions"
sudo chmod -R 777 storage
sudo chmod -R 777 public/uploads
sudo chmod -R 777 bootstrap/cache
sudo chmod -R 777 .env

echo "another apache updates"
cd /etc/apache2/sites-available/
sudo cp 000-default.conf frontend.conf
sudo sed -i "s/#ServerName www.example.com/ServerName backend-domain.com/g; \
s#DocumentRoot /var/www/html#DocumentRoot /var/www/html/streamview-backend/public#g" /etc/apache2/sites-available/000-default.conf
sudo sed -i "s/#ServerName www.example.com/ServerName frontend-domain.com/g; \
s#DocumentRoot /var/www/html#DocumentRoot /var/www/html/streamview-frontend#g" /etc/apache2/sites-available/frontend.conf

sudo a2ensite frontend
sudo a2enmod rewrite
sudo systemctl restart apache2

echo "app.js"
sudo ln -sf /var/www/html/streamview-backend/public/uploads/smil /var/www/html/streamview-frontend/assets
sudo ln -sf /var/www/html/streamview-backend/public/uploads/subtitles /var/www/html/streamview-frontend/assets

sudo apt remove cmdtest
sudo apt remove yarn
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
sudo apt-get update && sudo apt-get install yarn