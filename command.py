import subprocess

package_list=["apache2", "mysql-server", "php7.1", "php7.1-cli php7.1-mysql php7.1-xml  php7.1-mbstring php7.1-gettext php7.1-curl \
php7.1-common php7.1-opcache php7.1-readline php7.1-mcrypt php7.1-zip", "phpmyadmin php-mbstring php-gettext", "unzip composer ffmpeg nodejs build-essential", \
"redis-server"]
for pak in package_list:
    print(pak)
    command=subprocess.run(["which" +" "+ pak], stdout=subprocess.PIPE, text=True, shell=True)
    if command.stderr == None:
        print(command.stdout)
    else:
        print(command.stderr)
        continue
        
        

    
