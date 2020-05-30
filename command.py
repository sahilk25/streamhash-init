#!/usr/bin/env python3
import subprocess
import time

package_list = list(input("Enter packages to check: ").split(","))

#=["apache2", "mysql-server", "php7.3", "php7.3-cli php7.1-mysql php7.1-xml  php7.1-mbstring php7.1-gettext php7.1-curl \
#php7.1-common php7.1-opcache php7.1-readline php7.1-mcrypt php7.1-zip", "phpmyadmin php-mbstring php-gettext", "unzip composer ffmpeg nodejs build-essential", \
#"redis-server"]


print("checking, if packages are installed or not")
time.sleep(2)

for pak in package_list:
    gg=subprocess.check_output(["./as.py", pak])
    print(pak)
    print(gg)

