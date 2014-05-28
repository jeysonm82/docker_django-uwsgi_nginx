#!/usr/bin/python

# usage: install_django_docker https://user:pass@githost.com/django_project

import os
import sys
import subprocess

HOST_BASEDIR = '/opt/docker_sites/'

def cmd(command, msg='', use_os=False):
    try:
        print "==>", msg
        print command

        out = subprocess.check_output(
            command.split(' '), stderr=subprocess.STDOUT)
        return out
    except Exception, e:
        print "Error", e
        raise Exception

if __name__ == '__main__':
    print("==== Django docker container creation ====")

    print "--- Project setup ---"
    project_name = raw_input("==> Enter django project name: ")
    git_url = sys.argv[1] #raw_input("==> Enter Django project Git URL: ")

    print "-- Creating shared subdirectories in host --"
    for d in ('static', 'media'):
        if not os.path.exists('%s/%s/%s'%(HOST_BASEDIR, project_name, d)):
            cmd('mkdir -p %s/%s/%s'%(HOST_BASEDIR, project_name, d))

    print "-- Setting uwsgi.ini --"
    out = cmd("sed s/{project_name}/%s/g uwsgi_base.ini"%(project_name))
    with open('uwsgi.ini', 'w') as f:
        f.write(out)

    print "--- Nginx site configuration ---"
    server_name = raw_input("==> Enter server_name: ")
    port = raw_input("==> Enter port: ")

    out = cmd("sed -e s/{project_name}/%s/g -e s/{server_name}/%s/g -e s/{port}/%s/g mysite_nginx_base.conf"%(project_name, server_name, port))

    with open('%s/%s/mysite_nginx.conf'%(HOST_BASEDIR, project_name), 'w') as f:
        f.write(out)


    print "--- Docker container ---"
    cname = raw_input("Enter docker container name: ")
    
    print "Generating Dockerfile"
    out = cmd('sed s/{git_url}/%s/g Dockerfile_base'%(git_url.replace('/', '\/')))

    with open('Dockerfile', 'w') as f:
        f.write(out)

    print "Building Docker image"
    raw_input("press ENTER to continue")
    os.system("sudo docker build -t %s ."%(cname))


    print "Commands to run docker container"
    print "docker run -a stdin -a stdout -v /opt/docker_sites/%s:/home/docker/opt/ -i -t %s /bin/bash"%(project_name,cname)

    print "=== END ==="
