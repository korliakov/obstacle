#!/bin/bash
node=$(srun -N 8 -p RT hostname | tail -n 1)  
#SBATCH -N 1
#SBATCH --ntasks-per-node=1 # MPI process
#SBATCH --partition=RT
#SBATCH --nodelist=$node




srun  ~/bin/lmp_mpi -in in.obstacle



