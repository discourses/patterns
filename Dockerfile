# TensorFlow
FROM tensorflow/tensorflow:latest-gpu

# Updating the packages of the underlying operating system, and addressing privileges
RUN apt update && apt -y install sudo

# ... privileges
# https://linux.die.net/man/8/chpasswd
RUN useradd -m algebra && echo "algebra:algebra" | chpasswd && adduser algebra sudo

# Hence, the default user is
USER algebra

CMD [ "/bin/bash" ] 
