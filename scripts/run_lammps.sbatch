#!/bin/bash
node=$(srun -N 8 -p RT hostname | tail -n 1)  
#SBATCH -N 1
#SBATCH --ntasks-per-node=1 # MPI process
#SBATCH --partition=RT
#SBATCH --nodelist=$node


cd ~/obstacle/obstacle/data

srun  ~/bin/lmp_mpi -in ~/obstacle/obstacle/data/in.obstacle



