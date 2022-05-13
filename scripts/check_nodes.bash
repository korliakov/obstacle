#!/bin/bash

sinfo

echo "Available nodes:"


srun -N 8 -p RT hostname
