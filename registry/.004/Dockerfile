# Starting with a baseline NVIDIA/CUDA image
FROM nvidia/cuda:12.2.0-base-ubuntu20.04

ENV PATH="/opt/miniconda3/bin:${PATH}"
ARG PATH="/opt/miniconda3/bin:${PATH}"

SHELL [ "/bin/bash", "-c" ]

# Ubuntu ...
RUN apt update && apt -q -y upgrade && apt -y install sudo && apt -y install vim && apt -y install wget

# Enhancing, ... source /etc/profile
RUN wget -P Downloads https://repo.anaconda.com/miniconda/Miniconda3-py311_23.5.2-0-Linux-x86_64.sh && \
  chmod +x Downloads/Miniconda3-py311_23.5.2-0-Linux-x86_64.sh && \
  bash Downloads/Miniconda3-py311_23.5.2-0-Linux-x86_64.sh -b -p /opt/miniconda3 && \
  echo -e 'export PATH="/opt/miniconda3/bin:$PATH"\n\n' >> /etc/profile

RUN exec bash && conda init bash && conda config --set auto_activate_base true

# Evaluating ...
RUN useradd -m algebra && usermod -aG sudo algebra

# Hence, the default user is
USER algebra

# Finally
WORKDIR /home/algebra
CMD [ "/bin/bash"] 