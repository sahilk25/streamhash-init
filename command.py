#!/usr/bin/env python3
import subprocess
import time
import os
import sys
import shutil

not_installed=[]
installed=[]

def mysql_conf():
    subprocess.check_call(["./db.sh"])


def some_perm():

    print("Adjusting some permissions")
    subprocess.run("sudo chmod -R 777 /var/www/html/streamview-backend/storage",shell=True)
    subprocess.run("sudo chmod -R 777 /var/www/html/streamview-backend/public/uploads",shell=True)
    subprocess.run("sudo chmod -R 777 /var/www/html/streamview-backend/bootstrap/cache",shell=True)
    


def restart_apa():
    try:
        subprocess.check_call("sudo apt install 123sadcs",stderr=open('/dev/null', 'w'), shell=True)
    
    except subprocess.CalledProcessError:
        sys.exit()


def update_apa():
    print("updating apache2 conf files")

    trepalce("DirectoryIndex index.html index.cgi index.pl index.php index.xhtml index.htm","DirectoryIndex index.php index.cgi index.pl index.html index.xhtml index.htm","/home/alpha/Desktop/stream hash/dir.conf")
    restart_apa()
    trepalce("AllowOverride None","AllowOverride All","/home/alpha/Desktop/stream hash/apache2.conf",occ=3)
    restart_apa()
    shutil.copy2("/etc/apache2/sites-available/000-default.conf", "/etc/apache2/sites-available/000-default.conf/frontend.conf")
    shutil.copy2("/etc/apache2/sites-available/000-default.conf", "/etc/apache2/sites-available/000-default.conf/backend.conf")
    trepalce("#ServerName www.example.com","ServerName backend-domain.com","/etc/apache2/sites-available/000-default.conf/backend.conf")
    trepalce("DocumentRoot /var/www/html","DocumentRoot /var/www/html/streamview-backend/public","/etc/apache2/sites-available/000-default.conf/backend.conf")
    trepalce("#ServerName www.example.com","ServerName frontend-domain.com","/etc/apache2/sites-available/000-default.conf/frontend.conf")
    trepalce("DocumentRoot /var/www/html","DocumentRoot /var/www/html/streamview-frontend","/etc/apache2/sites-available/000-default.conf/frontend.conf")
    restart_apa()

    subprocess.run("sudo a2ensite frontend",shell=True)
    subprocess.run("sudo a2enmod rewrite",shell=True)
    restart_apa()

def repo_install(l3):
    subprocess.run("sudo apt update && upgrade -y")
    for i in l3:
        subprocess.run("sudo add-apt-repository -y" + " " + i)
        subprocess.run("sudo apt update && upgrade -y")



def is_installed(l1):
    
    print("checking, if packages are installed or not")
    time.sleep(2)

    for pak in l1:
        gg = subprocess.check_output(["./as.py", pak])

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
        subprocess.run("sudo apt update && upgrade -y")
        for x in l2:
            subprocess.run("sudo apt install -y" + " " + l2, shell=True)
            time.sleep(1)
            print(l2 + "installed")
    else: 
        return 0








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









