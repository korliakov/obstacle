#!/bin/bash

sbatch -N 1 --ntasks-per-node=1 --partition=RT --nodelist=node20-37 --wrap="srun jupyter lab --port 6677 --no-browser"
