Host, django+uwsgi container and nginx container. 

Check docker (http://docker.io).

The goal is to run one nginx server (inside container) and several isolated django containers with an uwsgi instance. Still alpha, in fact doesn't fully work yet, but you can use the ideas exposed here to inspire yourself!.

![alt tag](https://raw.github.com/jeysonmc/docker_django-uwsgi_nginx/master/docker_diagram.png)

Notes:
- This is just an excercise I made to learn more about docker (http://docker.io). Still a draft, buggy, not intended for production.
- I'm still having problems with shared folders read/write permissions. nginx container needs to write on uwsgi's socket.
- Maybe running several uwsgi instances separately is not efficient. Perhaps I should explore emperor mode, subscription (fastrouter), etc. Need to check memory usage.
