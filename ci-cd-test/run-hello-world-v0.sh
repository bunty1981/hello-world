#!/bin/bash
#eval "$(conda shell.bash hook)"
source "/Users/BHAGARO1/anaconda3/etc/profile.d/conda.sh"
conda activate first-env
echo "In conda environment: $CONDA_DEFAULT_ENV"
python ./hello-world/hello-world.py
#
conda deactivate
echo "In conda environment: $CONDA_DEFAULT_ENV"
