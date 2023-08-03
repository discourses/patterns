# TensorFlow & Computing via Graphics Processing Units
FROM tensorflow/tensorflow:latest-gpu

# Updating the packages of the underlying operating system, and addressing privileges
RUN add-apt-repository ppa:git-core/ppa
RUN apt update && apt -y install sudo && apt -y install vim && apt -y install git-all

# ... privileges
# https://linux.die.net/man/8/chpasswd
RUN useradd -m algebra && echo "algebra:algebra" | chpasswd && adduser algebra sudo

# Hence, the default user is
USER algebra

# .local/bin for installations
RUN echo $PATH
RUN echo "export PATH=$PATH:$HOME/.local/bin" >> ~/.bashrc

# After addressing privileges, and .local/bin for installations, proceed with
# underlying image enhancement
RUN python -m pip install --upgrade pip

# Set application directory <app>
WORKDIR /app

# This command copies requirements.txt into /app
COPY ./requirements.txt .

# --no-cache => do not save downloads
RUN python -m pip install --no-cache -r requirements.txt

# Finally
CMD [ "/bin/bash" ] 
