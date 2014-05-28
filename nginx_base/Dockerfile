FROM stackbrew/ubuntu:saucy
RUN apt-get update
RUN apt-get install -y nginx nano
RUN rm -v /etc/nginx/nginx.conf
ADD nginx.conf /etc/nginx/nginx.conf
RUN mkdir -p /home/docker/opt
ADD uwsgi_params /home/docker/uwsgi_params
EXPOSE 80
CMD service nginx start
#how to run: docker run -p 80:80 -v /opt/docker_sites/sites-enabled:/etc/nginx/sites-enabled -v /opt/docker_sites:/home/docker/opt -a stdin -a stdout -i -t jeysonmc/nginx  /bin/bash
