#!/usr/bin/env python3
#
# Comprueba si, para cada huésped, hay secuencias repetidas.
#

from Bio import SeqIO

path = '/Users/diegoruiz/Google Drive/4.1 Biotecnología/EMF - Evolución molecular y filogenia/_tEMF - Trabajo final/Rabies_ALL_SPECIES_N.FULL.DATED.fas'

def get_host(seq):
    """
    Returns the host name of a sequence.
    """
    id = seq.id
    host = id.split('_')[0]
    return(host)

all_sequences = SeqIO.parse(path, 'fasta')

# Fetch all hsot names
hosts_all = []
for fa in all_sequences:
    hosts_all.append(get_host(fa))

hosts_unique = list(set(hosts_all))


for host in hosts_unique:
    print(host)
    # Find sequences for each host
    i = 0
    all_sequences = SeqIO.parse(path, 'fasta')
    host_sequences = []
    for sequence in all_sequences:
        if get_host(sequence) == host:
            host_sequences.append(str(sequence.seq))
            i +=1
    
    print(str(len(host_sequences)) + ' sequences found.') # Total sequences
    sequences_unique = list(set(host_sequences))
    print(str(len(sequences_unique)) + ' distinct sequences.') # Distinct seq
    

    
    
