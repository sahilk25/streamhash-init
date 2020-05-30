#!/usr/bin/env python3

import subprocess
def restart_apa():
    try:
        subprocess.check_output("sudo apt install apache2",stderr=open('/dev/null', 'w'), shell=True)
    
    except subprocess.CalledProcessError:
        print("dhat tmkc")

restart_apa()
