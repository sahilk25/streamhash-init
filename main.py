#!/usr/bin/env python3
import subprocess
from os import path
import sys
from command import *
import shutil 
from termcolor import colored

repo_list=["ppa:ondrej/php","ppa:chris-lea/redis-server"]
package_list=["apache2", "mysql-server", "php7.1", "php7.1-cli php7.1-mysql php7.1-xml  php7.1-mbstring php7.1-gettext php7.1-curl \
    php7.1-common php7.1-opcache php7.1-readline php7.1-mcrypt php7.1-zip", "phpmyadmin php-mbstring php-gettext", "unzip composer ffmpeg nodejs", "build-essential", \
    "redis-server"]





#repo installation
repo_install(repo_list)

#checking packages
is_installed(package_list)

#installing packages
install(not_installed)
#unzipping the website
print(colored('Unzipping the website and adding to itss destination','green'))
is_zip_exists=path.exists("/home/alpha/website.zip")
website_front=path.exists("/var/www/html/streamview-frontend")
website_back=path.exists("/var/www/html/streamview-backend")
if website_back==True and website_front==True:
    if is_zip_exists ==True:
        print("zip exists")
        print(colored('zip exists','green'))
        subprocess.run("sudo unzip website.zip -d /var/www/html/",shell=True)
        subprocess.run("mkdir ~/main",shell=True)
        subprocess.run("sudo ln -sf /var/www/html/ ~/main",shell=True)
        subprocess.run("sudo ln -sf /var/www/html/streamview-backend/public/uploads/smil /var/www/html/streamview-frontend/assets",shell=True)
        subprocess.run("sudo ln -sf /var/www/html/streamview-backend/public/uploads/subtitles /var/www/html/streamview-frontend/assets",shell=True)
    else:
        
        print(colored('zip file doesnt exist','red'))
        sys.exit()



#making changes to msql

print(colored('Configuring mysql','green'))
#mysql_conf()


time.sleep(2)
#updating apache server
update_apa()

time.sleep(1)
#updating php file
print("updating php.ini")
print(colored('updating php.ini','green'))
trepalce("max_execution_time = 30","max_execution_time = -1","/etc/php/7.1/apache2/php.ini")
trepalce("max_input_time​= 60","max_input_time = -1","/etc/php/7.1/apache2/php.ini")
trepalce("memory_limit = 128M","memory_limit​= -1","/etc/php/7.1/apache2/php.ini")
trepalce("upload_max_filesize = 2M","upload_max_filesize = 5000M","/etc/php/7.1/apache2/php.ini")
trepalce("post_max_size = 8M","post_max_size​ =3000M","/etc/php/7.1/apache2/php.ini")


time.sleep(2)
some_perm()
#composer

print(colored('comoser streamview-backend','green'))

#updating ufw

print(colored('updating ufw','green'))
ufw_conf()


