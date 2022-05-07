#!/bin/bash
#SBATCH -N 1
#SBATCH --ntasks-per-node=1 # MPI process
#SBATCH --partition=RT




srun  ~/bin/lmp_mpi -in in.obstacle

