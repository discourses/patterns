#!/bin/bash


# Create virtual environment <tensors>
conda env create -f environment.yml -p /opt/miniconda3/envs/tensors


# Activate <tensors>
conda activate tensors


: << COMMENT
Finish the set-up
COMMENT

# Create directory <activate.d> within the new environment's directory
mkdir -p "$CONDA_PREFIX"/etc/conda/activate.d

# Hence:sour
# shellcheck disable=SC2016
echo 'CUDNN_PATH=$(dirname $(python -c "import nvidia.cudnn;print(nvidia.cudnn.__file__)"))' >> "$CONDA_PREFIX"/etc/conda/activate.d/env_vars.sh && \
echo 'export LD_LIBRARY_PATH=$CONDA_PREFIX/lib/:$CUDNN_PATH/lib:$LD_LIBRARY_PATH' >> "$CONDA_PREFIX"/etc/conda/activate.d/env_vars.sh && \
source "$CONDA_PREFIX"/etc/conda/activate.d/env_vars.sh