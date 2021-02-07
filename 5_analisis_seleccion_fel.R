#!/usr/bin/env Rscript
#
# Plotea los valores de dN/dS en cada posicón del alineamiento.
#

library(tidyverse)

directorio <- '/Users/diegoruiz/Google Drive/4.1 Biotecnología/EMF - Evolución molecular y filogenia/_tEMF - Trabajo final/5_presiones_de_seleccion/fel'
files <- list.files(directorio)

# Parsea los archivos .csv
data_list <- list()
i = 1
for (file in files){
  organism_name <- strsplit(file, '_')[[1]][1]
  datos <- read_csv(paste(directorio, file, sep='/'))
  n_pos <- nrow(datos)
  id_col <- matrix(organism_name, ncol=1, nrow=n_pos)
  datos <- cbind(datos, id_col)
  data_list[[i]] <- datos
  i = i + 1
}
df <- bind_rows(data_list)
names(df) <- c('sitio', 'particion', 'a', 'b', 'o', 'a_equal_b', 'LRT', 'p_val', 'branch_l', 'id_col')

# Define un umbral de p-valor
umbral <- 0.9
df_f <- filter(df, p_val > 0.05)

# Plot
ggplot(filter(df_f, a >3), aes(x=sitio, y=a)) + 
  geom_point(aes(color=id_col)) + geom_linerange(aes(ymax=a, color=id_col), ymin=0) + 
  theme_minimal() + ylim(0,30)


