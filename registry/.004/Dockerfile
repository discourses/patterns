# Starting with a baseline NVIDIA/CUDA image
FROM nvidia/cuda:12.2.0-base-ubuntu20.04

# Thus far, unspecified user
RUN mkdir -p /home/algebra

# Ubuntu ...
RUN apt update && apt list --upgradable && apt upgrade && apt -y install wget