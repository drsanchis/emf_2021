import re
import os
from Bio import SeqIO

path_tree = '/Users/diegoruiz/Google Drive/4.1 Biotecnología/EMF - Evolución molecular y filogenia/_tEMF - Trabajo final/arbol PhyML/preparado_para_phy.phy_phyml_tree.txt'
path_reference = '/Users/diegoruiz/Google Drive/4.1 Biotecnología/EMF - Evolución molecular y filogenia/_tEMF - Trabajo final/Rabies_ALL_SPECIES_N.FULL.DATED.fas'
path_tree_base = os.path.dirname(path_tree)


# Desde el archivo FASTA con todas las secuencias, saco un diccionario que relacione los
# números de accessión con los años
correspondencias = {}
with open (path_reference, 'r') as f:
    all_sequences = SeqIO.parse(f, 'fasta')
    for fa in all_sequences:
        id = fa.id
        split_id = id.split('_')
        accession = split_id[2]
        date = split_id[4]
        correspondencias[accession] = date

    
# Leer el archivo de origen
with open (path_tree, 'r') as f:
    arbol_original = f.read()
    
arbol_modificado = arbol_original

# Sustituir los números de accessión por años
for acc in correspondencias.keys():
    arbol_modificado = arbol_modificado.replace(acc, '_' + acc + '_' + correspondencias[acc])
    
# Escribir el archivo de output
with open (path_tree_base+'/modified_tree.txt', 'w') as f:
    f.write(arbol_modificado)