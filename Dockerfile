FROM python:3.8-buster
MAINTAINER sacharya <sacharya@tripadvisor.com>

# Install nginx
RUN apt-get update
RUN apt-get install nginx vim -y --no-install-recommends
COPY nginx.default /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

# Copy app source and install dependencies
RUN mkdir -p /opt/app
RUN mkdir -p /opt/app/django_skeleton
COPY requirements.txt start-server.sh manage.py db.sqlite3* .pip_cache* /opt/app/
COPY custom_entity_store /opt/app/django_skeleton/

WORKDIR /opt/app
RUN pip install -r requirements.txt --cache-dir /opt/app/.pip_cache
RUN chown -R www-data:www-data /opt/app

# Start server
EXPOSE 8020
STOPSIGNAL SIGTERM
CMD ["/opt/app/start-server.sh"]
