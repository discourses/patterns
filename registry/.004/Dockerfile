# Starting with a baseline NVIDIA/CUDA image
FROM nvidia/cuda:12.2.0-base-ubuntu20.04

# Thus far, unspecified user
RUN mkdir -p /home/algebra && cd /home/algebra

# Ubuntu ...
RUN apt update && apt list --upgradable && apt upgrade && apt -y install vim && apt -y install wget

# Enhancing, ...
RUN wget -P Downloads https://repo.anaconda.com/miniconda/Miniconda3-py311_23.5.2-0-Linux-x86_64.sh && \
  chmod +x Downloads/Miniconda3-py311_23.5.2-0-Linux-x86_64.sh && \
  bash Downloads/Miniconda3-py311_23.5.2-0-Linux-x86_64.sh -b -p /opt/miniconda3 && \
  echo -e 'export PATH="/opt/miniconda3/bin:$PATH"\n\n' >> /etc/profile
