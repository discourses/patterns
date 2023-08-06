# TensorFlow
FROM tensorflow/tensorflow:latest-gpu


# Updating the packages of the underlying operating system, and addressing privileges
# ... apt install nvidia-modprobe
# ... privileges -> https://linux.die.net/man/8/chpasswd
RUN add-apt-repository ppa:git-core/ppa && apt update && apt -y install sudo && \
  apt -y install vim && apt -y install git-all && \ 
  useradd -m algebra && echo "algebra:algebra" | chpasswd && \ 
  adduser algebra sudo


# Hence, setting the default user ...
USER algebra


# Set application directory <app>
WORKDIR /app


# This command copies requirements.txt into /app
COPY ./requirements.txt .


# Steps:
# In this section, and relative to the <user>, (a) a /etc path is created within the user's directory, and 
# ld.so.cache is created within ${HOME}/etc, next (b) the command ldconfig (linux.die.net/man/8/ldconfig) updates 
# ld.so.cache, next (c) a local bin is created for pip installations, next ...
#
# Note: 
# --no-cache => do not save downloads
#
RUN mkdir -p ${HOME}/etc && touch ${HOME}/etc/ld.so.cache && ldconfig -C ${HOME}/etc/ld.so.cache && \ 
  echo "export PATH=$PATH:$HOME/.local/bin" >> ~/.bashrc && \ 
  python -m pip install --upgrade pip && \
  python -m pip install --no-cache -r requirements.txt


# Finally
CMD [ "/bin/bash" ] 
