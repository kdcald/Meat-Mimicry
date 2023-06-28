# import libraries
library(cjpowR)
library(readr)
library(dplyr)
library(cjoint)

# resources
# https://osf.io/preprints/socarxiv/9yuhp/
# https://github.com/m-freitag/cjpowR 
# https://osf.io/preprints/socarxiv/spkcy/download 


# the amce was obtained from running a model with the pilot data. 
# see file mm-conjoint-analysis-to-share.R for model
cjpowr_amce (amce = 0.065052, power = 0.8, levels = 6, alpha =0.05)


