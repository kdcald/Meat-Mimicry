# import libraries
library(readr)
library(cjoint)
library(sievetest)
library(dplyr)
library(plyr)
library(tidyr)

# resources
# https://cran.r-project.org/web/packages/cjoint/cjoint.pdf 

# set working directory and import data
setwd("/Users/Krystal/Library/CloudStorage/GoogleDrive-kdcald@gmail.com/My Drive/Work/OpenPhil Contracting Work/Meat mimicry")
df <- read_csv("To share/mm-all-data-cleaned-to-share.csv")

# renaming terms and packages for clarity
df$terms <- gsub("meatier","Meatier",df$terms)
df$terms <- gsub("1:4lb", "1/4 lb",df$terms)
df$terms <- gsub("thick&juicy","Thick & Juicy",df$terms)
df$package <- gsub("package 1","Package Clear Top",df$package)
df$package <- gsub("package 2","Package Box",df$package)

# converting to factors
df$terms <- factor(df$terms)
df$package <- factor(df$package)

# re-leveling for model
df$terms <- relevel(df$terms, "Meatier")
df$package <- relevel(df$package, "Package Clear Top")

# run model
results <- amce(choice_ind ~ package + terms, data=df,
                  cluster=TRUE, respondent.id="respondent_id")
summary(results)

# plot
plot(results, xlab="Change in Pr(Preference to Purchase Plant-Based Burger)",text.size=13)



