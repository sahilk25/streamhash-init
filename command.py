#!/usr/bin/env python3
import subprocess
import time
import os
import sys
import shutil
from os import path

not_installed=[]
installed=[]

def mysql_conf():
    subprocess.check_call(["./streamhash-init/db.sh"])
    trepalce("DB_DATABASE=streamview","DB_DATABASE=streamhash","/var/www/html/streamview-backend/.env",occ=3)
    trepalce("DB_PASSWORD=12345","DB_PASSWORD=streamhash@123","/var/www/html/streamview-backend/.env",occ=3)


def some_perm():

    print("Adjusting some permissions")
    subprocess.run("sudo chmod -R 777 /var/www/html/streamview-backend/storage",shell=True)
    subprocess.run("sudo chmod -R 777 /var/www/html/streamview-backend/public/uploads",shell=True)
    subprocess.run("sudo chmod -R 777 /var/www/html/streamview-backend/bootstrap/cache",shell=True)
    


def restart_apa():
    try:
        subprocess.check_call("sudo systemctl restart apache2",stderr=open('/dev/null', 'w'), shell=True)
    
    except subprocess.CalledProcessError:
        subprocess.Popen("sudo journalctl -xe",stderr=open('/dev/null', 'w'), shell=True)
        sys.exit()


def update_apa():
    print("updating apache2 conf files")

    trepalce("DirectoryIndex index.html index.cgi index.pl index.php index.xhtml index.htm","DirectoryIndex index.php index.cgi index.pl index.html index.xhtml index.htm","/etc/apache2/mods-enabled/dir.conf")
    restart_apa()
    trepalce("AllowOverride None","AllowOverride All","/etc/apache2/apache2.conf",occ=3)
    restart_apa()
    file_1=path.exists("/etc/apache2/sites-available/frontend.conf")
    if file_1==True:
        None
    else:
        shutil.copy2("/etc/apache2/sites-available/000-default.conf", "/etc/apache2/sites-available/frontend.conf")
    file_2=path.exists("/etc/apache2/sites-available/backend.conf")
    if file_2==True:
        None
    else:
        shutil.copy2("/etc/apache2/sites-available/000-default.conf", "/etc/apache2/sites-available/backend.conf")
    trepalce("#ServerName www.example.com","ServerName backend-domain.com","/etc/apache2/sites-available/backend.conf")
    trepalce("DocumentRoot /var/www/html","DocumentRoot /var/www/html/streamview-backend/public","/etc/apache2/sites-available/backend.conf")
    trepalce("#ServerName www.example.com","ServerName frontend-domain.com","/etc/apache2/sites-available/frontend.conf")
    trepalce("DocumentRoot /var/www/html","DocumentRoot /var/www/html/streamview-frontend","/etc/apache2/sites-available/frontend.conf")
    restart_apa()
    subprocess.run("sudo phpenmod mcrypt", shell=True)
    subprocess.run("sudo phpenmod mbstring", shell=True)

    subprocess.run("sudo a2ensite frontend",shell=True)
    subprocess.run("sudo a2ensite backend",shell=True)
    subprocess.run("sudo a2enmod rewrite",shell=True)
    restart_apa()

def repo_install(l3):
    subprocess.run("sudo apt update -y", shell=True)
    path_1=path.exists("/etc/apt/sources.list.d/chris-lea-ubuntu-redis-server-bionic.list")
    path_2=path.exists("/etc/apt/sources.list.d/ondrej-ubuntu-php-bionic.list")
    if path_1==True and path_2==True: 
        for i in l3:
            subprocess.run("sudo add-apt-repository -y" + " " + i, shell=True)
            subprocess.run("sudo apt update -y", shell=True)
    else: 
        None


def is_installed(l1):
    
    print("checking, if packages are installed or not")
    time.sleep(2)

    for pak in l1:
        gg = subprocess.check_output(["./streamhash-init/as.py", pak])

        if gg == b'Package  is NOT installed!\n':
            not_installed.append(pak)

        else:
            installed.append(pak)
    print("These packages are not intalled:", not_installed)

    print("These packages are intalled:", installed)




def install(l2):
   
    print("Do you want to install these packages?")
    print(not_installed)
    print("if you want to install press y else press any key")
    a=input(str)
    if a == "y":
        subprocess.run("sudo apt update -y", shell=True)
        if len(l2) != 0:
            for x in l2:
                subprocess.run("sudo apt install -y" + " " + x, shell=True)
                time.sleep(2)
                print(x + "installed")
                time.sleep(2)
        else:
            return None
    else: 
        sys.exit()
    subprocess.run("sudo systemctl enable redis-server mysql apache2")
    subprocess.run("sudo systemctl restart redis-server mysql apache2")

def composer():
    subprocess.run("cd /var/www/html/streamview-backend && sudo composer dump-autoload", shell=True)
    subprocess.run("cd /var/www/html/streamview-backend && php artisan view:clear", shell=True)
    subprocess.run("cd /var/www/html/streamview-backend && phpartisan config:clear", shell=True)
    subprocess.run("cd /var/www/html/streamview-backend && phpartisan cache:clear", shell=True)
    subprocess.run("cd /var/www/html/streamview-backend && phpartisan config:cache", shell=True)
    subprocess.run("cd /var/www/html/streamview-backend && cp app/ffmpeg-custom/olaferlandsen/ffmpeg-php-class/src/FFmpeg.php vendor/vidhyar2612/ffmpeg-php-class/src/FFmpeg.php", shell=True)






def trepalce(olds: object, news: object, file_path: object, occ: object = 0) -> object:
    fin = open(file_path, "rt")
    #read file contents to string
    data = fin.read()
    #replace all occurrences of the required string
    if occ==0:
        data = data.replace(str(olds), str(news))
    else:
        data = data.replace(str(olds), str(news), occ)
    #close the input file
    fin.close()
    #open the input file in write mode
    fin = open(file_path, "wt")
    #overrite the input file with the resulting data
    fin.write(data)
    #close the file
    fin.close()
    	
def append_new_line(text_to_append, file_name):
    """Append given text as a new line at the end of file"""
    # Open the file in append & read mode ('a+')
    with open(file_name, "a+") as file_object:
        # Move read cursor to the start of file.
        file_object.seek(0)
        # If file is not empty then append '\n'
        data = file_object.read(100)
        if len(data) > 0:
            file_object.write("\n")
        # Append text at the end of file
        file_object.write(text_to_append)
 
def append_multiple_lines(lines_to_append, file_name):
    # Open the file in append & read mode ('a+')
    with open(file_name, "a+") as file_object:
        appendEOL = False
        # Move read cursor to the start of file.
        file_object.seek(0)
        # Check if file is not empty
        data = file_object.read(100)
        if len(data) > 0:
            appendEOL = True
        # Iterate over each string in the list
        for line in lines_to_append:
            # If file is not empty then append '\n' before first line for
            # other lines always append '\n' before appending line
            if appendEOL == True:
                file_object.write("\n")
            else:
                appendEOL = True
            # Append element at the end of file
            file_object.write(line)


def ufw_conf():
    subprocess.run("sudo touch /etc/ufw/applications.d/redis", shell=True)
    redisfile=["[Redis]","title=Persistent key-value database with network interface","description=Redis is a key-value database \
         in a similar vein to memcache but the dataset is non-volatile.", "ports=6379/tcp"]
    append_multiple_lines(redisfile,"/etc/ufw/applications.d/redis")
    subprocess.run("sudo ufw app update Redis", shell=True)
    subprocess.run("sudo systemctl restart ufw", shell=True)





def npm_conf():
    subprocess.run("curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash", shell=True)
    subprocess.run("nvm install v10", shell=True)
    subprocess.run("npm install yarn", shell=True)
    subprocess.run("sudo chown $USER:$USER -R /var/www/html/", shell=True)
    subprocess.run("cd /var/www/html/streamview-frontend && yarn install ", shell=True)
    subprocess.run("cd /var/www/html/streamview-frontend && npm install", shell=True)

    
    
    
    
    


    