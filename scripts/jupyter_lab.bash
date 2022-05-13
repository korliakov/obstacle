#!/bin/bash

port=6593
node=$(srun -N 8 -p RT hostname | tail -n 1)

echo "The node is: $node"
echo "The port is: $port"

cd ~



result=$(sbatch -N 1 --ntasks-per-node=1 --partition=RT --nodelist=$node --wrap="srun jupyter lab --port $port --no-browser"  | grep "Submitted" | awk '{print $4}' )


echo "$node $port $result"

