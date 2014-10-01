tinyctf-platform
================

`tinyctf-platform` is yet another open-source (jeopardy style) CTF platform. It is relatively easy to set up and modify. Hopefully it will become even better over time, with other people contributing.

![alt text](http://i.imgur.com/dqGeLNM.jpg "tinyctf-platform in action")

Deployment
----------

To deploy `tinyctf-platform` on an EC2 instance, execute the following commands:

Become root, upgrade

    sudo su
    yum upgrade -y
    
Install some prerequisites

    yum install -y git
    yum install -y gcc-c++
    yum install -y python-devel
    
Install Flask and dataset

    easy_install Flask
    easy_install dataset
    exit
    
Clone the repo

    git clone https://github.com/balidani/tinyctf-platform.git
    cd tinyctf-platform/
    
Import the tasks

    python task_import.py
    
Start the server

    python server.py

*Note*: Flask should run on top of a proper web server if you plan to have many players.

Caveats
-------

* CSRF is currently not addressed
* The platform does not support tasks with the same score and category right now
