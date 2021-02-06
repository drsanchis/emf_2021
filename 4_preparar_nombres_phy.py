#!/usr/bin/env python3
#
# 
#


from Bio import SeqIO
import os

path = '/Users/diegoruiz/Google Drive/4.1 Biotecnología/EMF - Evolución molecular y filogenia/_tEMF - Trabajo final/Rabies_ALL_SPECIES_N.FULL.DATED.fas'



def get_host(seq):
    """
    Returns the host name of a sequence.
    """
    id = seq.id
    host = id.split('_')[0][0]
    return(host)


all_sequences = SeqIO.parse(path, 'fasta')

# Retrieves host names
hosts_all = []
for fa in all_sequences:
    hosts_all.append(get_host(fa))

hosts_unique = list(set(hosts_all))



with open ('preparado_para_phy.fa', 'w') as f:
    
        all_sequences = SeqIO.parse(path, 'fasta')
        for sequence in all_sequences:
            complete_id = sequence.id
            separated_id = complete_id.split('_')
            host_id = separated_id[0][0:2]
            access = separated_id[2]
            print(host_id+access)
            
            f.write('>'+ host_id + access + "\n")
            f.write(str(sequence.seq) + "\n")

f.close()
    