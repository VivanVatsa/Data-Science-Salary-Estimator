#%%
# from numpy.core.fromnumeric import size
import pandas as pd

df = pd.read_csv("glassdoor_jobs.csv")

df = df[df["Salary Estimate"] != "-1"]
df

# TO DO IN DATA CLEANING
# -------------------
# salary parsing
# company name text only
# state field
# age of company
# parsing of job description (PYTHON)

#%%
salary = df["Salary Estimate"].apply(lambda x: x.split("(")[0])
salary

# %%
minus_Kd = salary.apply(lambda x: x.replace("K", "").replace("₹", ""))
minus_Kd

# %%
df["hourly"] = df["Salary Estimate"].apply(lambda x: 1
                                           if "per hour" in x.lower() else 0)

df

# %%
