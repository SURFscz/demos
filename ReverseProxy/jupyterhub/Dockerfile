# JupyterHub Dockerfile that loads your jupyterhub_config.py
#
# Adds ONBUILD step to jupyter/jupyterhub to load your jupyterhub_config.py into the image
#
# Derivative images must have jupyterhub_config.py next to the Dockerfile.

ARG BASE_IMAGE=jupyterhub/jupyterhub:latest
FROM $BASE_IMAGE

RUN python3 -m pip install notebook
RUN python3 -m pip install jhub_remote_user_authenticator

ENV USERNAME=admin
ENV PASSWORD=admin

RUN useradd -m -p $(openssl passwd -1 ${PASSWORD}) -s /bin/bash -G sudo ${USERNAME}
USER admin
WORKDIR /home/admin

CMD ["jupyterhub", "-f", "/srv/jupyterhub/jupyterhub_config.py"]
