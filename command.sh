#!/bin/sh


repo_list=("ppa:ondrej/php" "ppa:chris-lea/redis-server")
for val in ${repo_list[@]}
do
   echo $val
   echo $val "is added  "
done


#sudo apt-get update -y
package_list=("apache2" "mysql-server" "php7.1-cli php7.1-mysql php7.1-xml  php7.1-mbstring php7.1-gettext php7.1-curl\
php7.1-common php7.1-opcache php7.1-readline php7.1-mcrypt php7.1-zip" "phpmyadmin php-mbstring php-gettext unzip composer ffmpeg nodejs build-essential" \
"redis-server")

for pak in ${!package_list[@]}
do
   echo $pak
   echo $pak "is installed"
done