#!/home/common/studtscm05/anaconda3/bin/python3

import numpy as np
import matplotlib.pyplot as plt

for i in range(1, 5):

    Coord_dict={}
    currentStep=0
    numberParticles=0
    walls=[0,0,0]
    readTimestep=0
    readNAtoms=0
    readCell=0
    readParticle=0
    f = open(f"/home/common/studtscm05/obstacle/obstacle/data/{i}/dump.obstacle", "r")
    n=10
    for line in f.readlines():
        line=line[:-1]
        if (line=="ITEM: TIMESTEP"):
            # print("READ1")
            readTimestep=1
            continue
        if readTimestep:
            # print("READ2")
            readTimestep=0
            currentStep=int(line)
            Coord_dict[currentStep]=[]
            continue
        if (line=="ITEM: NUMBER OF ATOMS"):
            readNAtoms=1
            continue
        if readNAtoms:
            readNAtoms=0
            numberParticles=int(line)
            continue
        if (line=="ITEM: BOX BOUNDS pp ss pp"):
            readCell=3
            continue
        if readCell>0:
            readCell-=1
            walls[readCell]=float(line.split()[1])
            continue
        if (line=="ITEM: ATOMS id type xs ys zs"):
            readParticle=numberParticles
            continue
        if readParticle>0:
            readParticle-=1
            Coord_dict[currentStep].append([float(x) for x in line.split()[2:]])
            continue
    steps=list(Coord_dict.keys())       
    plt.figure(figsize=(12,9))
    plt.scatter(np.array(Coord_dict[steps[-1]])[:, 0], np.array(Coord_dict[steps[-1]])[:, 1], s=10)
    
    plt.title(f"param = {round(0.6+i*2/10, 2)}")
    plt.savefig(f'/home/common/studtscm05/obstacle/obstacle/data/plots/{i}.jpg')
    
