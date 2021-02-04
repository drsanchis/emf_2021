#!/usr/bin/env python3
#
# Separa las secuencias en archivos FASTA distintos según el huésped.
#

from Bio import SeqIO
import os

path = '/Users/diegoruiz/Google Drive/4.1 Biotecnología/EMF - Evolución molecular y filogenia/_tEMF - Trabajo final/Rabies_ALL_SPECIES_N.FULL.DATED.fas'

# Get file basename
basename = os.path.basename(path)
basename_no_ext = basename.split('.')[0:3]
basename_clean = '.'.join(basename_no_ext)


def get_host(seq):
    """
    Returns the host name of a sequence.
    """
    id = seq.id
    host = id.split('_')[0]
    return(host)


all_sequences = SeqIO.parse(path, 'fasta')


# Retrieves a list of hosts
hosts_all = []
for fa in all_sequences:
    hosts_all.append(get_host(fa))

    
hosts_unique = list(set(hosts_all))


# Creates separate files with sequences of each host
for host in hosts_unique:
    print(host)
    i = 0
    with open (path+basename_clean+'_'+host+'.fa', 'w') as f:
    
        all_sequences = SeqIO.parse(path, 'fasta')
        for sequence in all_sequences:
            if get_host(sequence) == host:
                f.write('>'+str(sequence.id) + "\n")
                f.write(str(sequence.seq) + "\n")
                i +=1
    f.close()
    print(str(i) + ' sequences found.')