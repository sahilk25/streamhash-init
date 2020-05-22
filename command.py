#!/usr/bin/env python3
import subprocess

package_list=["apache2", "mysql-server", "php7.3", "php7.3-cli php7.1-mysql php7.1-xml  php7.1-mbstring php7.1-gettext php7.1-curl \
php7.1-common php7.1-opcache php7.1-readline php7.1-mcrypt php7.1-zip", "phpmyadmin php-mbstring php-gettext", "unzip composer ffmpeg nodejs build-essential", \
"redis-server"]
for pak in package_list:
    gg=subprocess.check_output(["./as.py", pak])
    print(pak)
    print(gg)
        
