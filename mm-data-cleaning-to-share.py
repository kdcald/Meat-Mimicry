# --------------------------------------------------------------- # 
# import libraries and data
# --------------------------------------------------------------- #
import pandas as pd
import os
import numpy as np

#  set working directory
path = "/Users/Krystal/Library/CloudStorage/GoogleDrive-kdcald@gmail.com/My Drive/Work/OpenPhil Contracting Work/Meat mimicry"
os.chdir(path)
os.getcwd()

# import data
pilot = pd.read_csv("To share/mm-pilot-conjointly-raw-data.csv")
main = pd.read_csv("To share/mm-main-conjointly-raw-data.csv")

# --------------------------------------------------------------- # 
# data cleaning
# --------------------------------------------------------------- #
# splitting PACKAGE colum into two
pilot[['package','terms']] = pilot['PACKAGE'].str.split(',',expand=True)
pilot['terms'] = pilot['terms'].str.lstrip()

main[['package','terms']] = main['PACKAGE'].str.split(',',expand=True)
main['terms'] = main['terms'].str.lstrip()

# cleaning diet cols
pilot_diet_cols = [
       'Q7_HOW_DO_YOU_TYPICALLY_DESCRIBE_YOUR_DIET_O1_OMNIVORE_MEAT_EATER',
       'Q7_HOW_DO_YOU_TYPICALLY_DESCRIBE_YOUR_DIET_O2_REDUCETARIAN',
       'Q7_HOW_DO_YOU_TYPICALLY_DESCRIBE_YOUR_DIET_O3_FLEXITARIAN',
       'Q7_HOW_DO_YOU_TYPICALLY_DESCRIBE_YOUR_DIET_O4_SEMI_VEGETARIAN',
       'Q7_HOW_DO_YOU_TYPICALLY_DESCRIBE_YOUR_DIET_O5_PESCETARIAN',
       'Q7_HOW_DO_YOU_TYPICALLY_DESCRIBE_YOUR_DIET_O6_VEGETARIAN',
       'Q7_HOW_DO_YOU_TYPICALLY_DESCRIBE_YOUR_DIET_O7_VEGAN',
       'Q7_HOW_DO_YOU_TYPICALLY_DESCRIBE_YOUR_DIET_O8_OTHER']
pilot['diet'] = pd.Series(pilot[pilot_diet_cols].columns[np.where(pilot[pilot_diet_cols]!=0)[1]])

main_diet_cols = [
       'Q4_DIET_O1_OMNIVORE_MEAT_EATER',
       'Q4_DIET_O2_REDUCETARIAN',
       'Q4_DIET_O3_FLEXITARIAN',
       'Q4_DIET_O4_SEMI_VEGETARIAN',
       'Q4_DIET_O5_PESCETARIAN',
       'Q4_DIET_O6_VEGETARIAN',
       'Q4_DIET_O7_VEGAN',
       'Q4_DIET_O8_OTHER']
main['diet'] = pd.Series(main[main_diet_cols].columns[np.where(main[main_diet_cols]!=0)[1]])

pilot_diet_dict = {
       'Q7_HOW_DO_YOU_TYPICALLY_DESCRIBE_YOUR_DIET_O1_OMNIVORE_MEAT_EATER' : 'omnivore',
       'Q7_HOW_DO_YOU_TYPICALLY_DESCRIBE_YOUR_DIET_O2_REDUCETARIAN' : 'reducer',
       'Q7_HOW_DO_YOU_TYPICALLY_DESCRIBE_YOUR_DIET_O3_FLEXITARIAN' : 'reducer',
       'Q7_HOW_DO_YOU_TYPICALLY_DESCRIBE_YOUR_DIET_O4_SEMI_VEGETARIAN' : 'reducer',
       'Q7_HOW_DO_YOU_TYPICALLY_DESCRIBE_YOUR_DIET_O5_PESCETARIAN' : 'reducer',
       'Q7_HOW_DO_YOU_TYPICALLY_DESCRIBE_YOUR_DIET_O6_VEGETARIAN' : 'veg',
       'Q7_HOW_DO_YOU_TYPICALLY_DESCRIBE_YOUR_DIET_O7_VEGAN' : 'veg',
       'Q7_HOW_DO_YOU_TYPICALLY_DESCRIBE_YOUR_DIET_O8_OTHER' : 'omnivore'}
pilot['diet'] = pilot['diet'].map(pilot_diet_dict)

main_pilot_dict = {
       'Q4_DIET_O1_OMNIVORE_MEAT_EATER' : 'omnivore',
       'Q4_DIET_O2_REDUCETARIAN' : 'reducer',
       'Q4_DIET_O3_FLEXITARIAN' : 'reducer',
       'Q4_DIET_O4_SEMI_VEGETARIAN' : 'reducer',
       'Q4_DIET_O5_PESCETARIAN' : 'reducer',
       'Q4_DIET_O6_VEGETARIAN' : 'veg',
       'Q4_DIET_O7_VEGAN' : 'veg',
       'Q4_DIET_O8_OTHER' : 'omnivore'}
main['diet'] = main['diet'].map(main_pilot_dict)

# subset to only useful columns
pilot_cols_to_keep = [
       'RESPONDENT_ID', 
       'CHOICE_SET',
       'LABEL', 
       'CHOICE_INDICATOR',
       'package', 
       'terms', 
       'diet',
       'RESPONDENT_REGION', 
       'RESPONDENT_LENGTH_OF_INTERVIEW_SECONDS',
       'VARIABLE_EXTERNAL_GENDER',
       'VARIABLE_EXTERNAL_AGE', 
       'VARIABLE_EXTERNAL_MAINREGIONNAME',
       'VARIABLE_EXTERNAL_HOUSEHOLD_INCOME_CLASSIFICATION',
       'VARIABLE_EXTERNAL_FOOD_FAST_FOOD_HOW_OFTEN',
       'VARIABLE_EXTERNAL_PRIMARY_GROCERY_SHOPPER',
       'VARIABLE_EXTERNAL_OCCUPATION',
       'VARIABLE_EXTERNAL_ETHNICITY_US_CANADA_ONLY',
       'VARIABLE_EXTERNAL_PRIMARY_ROLE_IN_ORGANIZATION',
       'VARIABLE_EXTERNAL_MARITAL_STATUS',
       'VARIABLE_EXTERNAL_ACCOMMODATION',
       'VARIABLE_EXTERNAL_HOUSEHOLD_SIZE',
       'VARIABLE_EXTERNAL_FOOD_MAIN_GROCERY_SHOP',
       'VARIABLE_EXTERNAL_EDUCATION_GENERAL',
       'VARIABLE_EXTERNAL_FOOD_FAST_FOOD_RESTAURANT',
       'Q10_COMPLETE_THANK_YOU_FOR_TAKING_THE_TIME_TO_COMPLETE_THIS_SURVEY_FEEL_FREE_TO_LEAVE_ANY_FINAL_COMMENTS']
pilot = pilot[pilot_cols_to_keep]

main_cols_to_keep = [
       'RESPONDENT_ID', 
       'CHOICE_SET',
       'LABEL', 
       'CHOICE_INDICATOR',
       'package', 
       'terms', 
       'diet',
       'RESPONDENT_REGION', 
       'RESPONDENT_LENGTH_OF_INTERVIEW_SECONDS',
       'Q5_FINAL_COMMENTS']
main = main[main_cols_to_keep]

# rename columns
pilot_rename_cols = {
       'RESPONDENT_ID' : 'respondent_id', 
       'CHOICE_SET' : 'choice_set',
       'LABEL' : 'label', 
       'CHOICE_INDICATOR' : 'choice_ind',
       'package' : 'package', 
       'terms' : 'terms', 
       'diet' : 'diet',
       'RESPONDENT_REGION' : 'state', 
       'RESPONDENT_LENGTH_OF_INTERVIEW_SECONDS' : "survey_completion_secs",
       'VARIABLE_EXTERNAL_GENDER' : 'gender',
       'VARIABLE_EXTERNAL_AGE' : 'age', 
       'VARIABLE_EXTERNAL_MAINREGIONNAME' : 'us_region',
       'VARIABLE_EXTERNAL_HOUSEHOLD_INCOME_CLASSIFICATION' : 'household_income',
       'VARIABLE_EXTERNAL_FOOD_FAST_FOOD_HOW_OFTEN' : 'fast_food_frequency',
       'VARIABLE_EXTERNAL_PRIMARY_GROCERY_SHOPPER' : 'primary_grocery_shopper',
       'VARIABLE_EXTERNAL_OCCUPATION' : 'occupation',
       'VARIABLE_EXTERNAL_ETHNICITY_US_CANADA_ONLY' : 'ethnicity',
       'VARIABLE_EXTERNAL_PRIMARY_ROLE_IN_ORGANIZATION' : 'primary_role_org',
       'VARIABLE_EXTERNAL_MARITAL_STATUS' : 'marital_status',
       'VARIABLE_EXTERNAL_ACCOMMODATION' : 'housing',
       'VARIABLE_EXTERNAL_HOUSEHOLD_SIZE' : 'household_size',
       'VARIABLE_EXTERNAL_FOOD_MAIN_GROCERY_SHOP' : 'main_grocery_store',
       'VARIABLE_EXTERNAL_EDUCATION_GENERAL' : 'education',
       'VARIABLE_EXTERNAL_FOOD_FAST_FOOD_RESTAURANT' : 'main_fast_food',
       'Q10_COMPLETE_THANK_YOU_FOR_TAKING_THE_TIME_TO_COMPLETE_THIS_SURVEY_FEEL_FREE_TO_LEAVE_ANY_FINAL_COMMENTS' : 'final_comments'}
pilot.rename(columns=pilot_rename_cols, inplace=True)

main_rename_cols = {
       'RESPONDENT_ID' : 'respondent_id', 
       'CHOICE_SET' : 'choice_set',
       'LABEL' : 'label', 
       'CHOICE_INDICATOR' : 'choice_ind',
       'package' : 'package', 
       'terms' : 'terms', 
       'diet' : 'diet',
       'RESPONDENT_REGION' : 'state', 
       'RESPONDENT_LENGTH_OF_INTERVIEW_SECONDS' : "survey_completion_secs",
       'Q5_FINAL_COMMENTS' : 'final_comments'}
main.rename(columns=main_rename_cols, inplace=True)

# adding column to identify data source
pilot['data_source'] = 'pilot'
main['data_source'] = 'main'

# combining pilot and main dfs
df = pd.concat([pilot,main])

# --------------------------------------------------------------- # 
# identifying and removing respondents based on completion time
# --------------------------------------------------------------- #
# first create unique df
df_unique = df.drop_duplicates('respondent_id')
df_unique = df_unique[df_unique['survey_completion_secs']!=16789] # removing this outlier first. it's 4.6 hours and the only outlier identifed below if i don't remove it first.

# identify outliers
data_mean, data_std = df_unique['survey_completion_secs'].mean(), df_unique['survey_completion_secs'].std()
cut_off = data_std * 3
lower, upper = data_mean - cut_off, data_mean + cut_off
outliers = [x for x in df_unique['survey_completion_secs'] if x < lower or x > upper]

# remove outliers
times_to_remove = [1730, 641, 1625, 696, 1323, 16789]
df = df[~df['survey_completion_secs'].isin(times_to_remove)]

# --------------------------------------------------------------- # 
# export data
# --------------------------------------------------------------- #
# this df is imported to R for analysis
#df.to_csv('To share/mm-all-data-cleaned-to-share.csv',index=False)






