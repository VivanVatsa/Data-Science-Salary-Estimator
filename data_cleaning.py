#%%
# from numpy.core.fromnumeric import size
import pandas as pd

df = pd.read_csv("glassdoor_jobs.csv")

df = df[df["Salary Estimate"] != "-1"]
df

# size(df)
# df = df[df["Salary Estimate"] != "-1"]

# TO DO IN DATA CLEANING
# -------------------
# salary parsing
# company name text only
# state field
# age of company
# parsing of job description (PYTHON)
# %%
