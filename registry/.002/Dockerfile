# TensorFlow
FROM tensorflow/build:latest-python3.11

# Updating the packages of the underlying operating system, and addressing privileges
RUN add-apt-repository ppa:git-core/ppa
RUN apt update && apt -y install sudo && apt -y install vim && apt -y install git-all