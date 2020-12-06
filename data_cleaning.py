#%%
import pandas as pd

df = pd.read_csv("glassdoor_jobs.csv")

#%%
# df

# TO DO IN DATA CLEANING
# -------------------
# salary parsing
# company name text only
# state field
# age of company
# parsing of job description (PYTHON)
#%%
df = df[df["Salary Estimate"] != "-1"]

# %%
