FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive
ARG RUNLEVEL=1
ENV TERM linux

RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections
RUN apt update -y  && apt upgrade -y
RUN apt install -y apache2 libapache2-mod-auth-openidc
RUN apt clean -y && apt-get autoremove -y
RUN a2enmod headers rewrite proxy_http proxy_wstunnel

ENTRYPOINT /bin/rm -f /var/run/apache2/apache2.pid; /usr/sbin/apache2ctl -D FOREGROUND
