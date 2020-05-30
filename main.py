#!/usr/bin/env python3
import subprocess
from os import path
import sys
from command import *
import shutil 

repo_list=["ppa:ondrej/php","ppa:chris-lea/redis-server"]
package_list=["apache2", "mysql-server", "php7.3", "php7.3-cli php7.1-mysql php7.1-xml  php7.1-mbstring php7.1-gettext php7.1-curl \
    php7.1-common php7.1-opcache php7.1-readline php7.1-mcrypt php7.1-zip", "phpmyadmin php-mbstring php-gettext", "unzip composer ffmpeg nodejs build-essential", \
    "redis-server"]


#unzipping the website
print("Unzipping the website and adding to it's destination")
is_website_exists=path.exists("~/website.zip")
gg=path.exists("~/website.zip")
if is_website_exists ==True:
    print("zip exists")
    subprocess.run("sudo unzip website.zip -d /var/www/html/",shell=True)
    subprocess.run("mkdir ~/main",shell=True)
    subprocess.run("sudo ln -sf /var/www/html/ ~/main",shell=True)
    subprocess.run("sudo ln -sf /var/www/html/streamview-backend/public/uploads/smil /var/www/html/streamview-frontend/assets",shell=True)
    subprocess.run("sudo ln -sf /var/www/html/streamview-backend/public/uploads/subtitles /var/www/html/streamview-frontend/assets",shell=True)
else:
    print("zip file doesnt exist")
    sys.exit()




#repo installation
repo_install(repo_list)

#checking packages
is_installed(package_list)

#installing packages
install(not_installed)

#making changes to msql
print("Configuring mysql")
subprocess.check_call(["./db.sh"])


time.sleep(2)
#updating apache server
update_apa()

time.sleep(1)
#updating php file
print("updating php.ini")
trepalce("max_execution_time = 30","max_execution_time = -1","/etc/php/7.1/apache2/php.ini")
trepalce("max_input_time​= 60","max_input_time = -1","/etc/php/7.1/apache2/php.ini")
trepalce("memory_limit = 128M","memory_limit​= -1","/etc/php/7.1/apache2/php.ini")
trepalce("upload_max_filesize = 2M","upload_max_filesize = 5000M","/etc/php/7.1/apache2/php.ini")
trepalce("post_max_size = 8M","post_max_size​ =3000M","/etc/php/7.1/apache2/php.ini")


time.sleep(2)
some_perm()