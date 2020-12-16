#%%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("data_eda.csv")
# choose the relevant columns

#%%
df.columns

#%%
ddf_model = df[[
    "avg_salary",
    "Rating",
    "Size",
    "Type of ownership",
    "Industry",
    "Sector",
    "Revenue",
    "num_comp",
    "hourly",
    "employer_provided",
    "job_state",
    "same_state",
    "age",
    "python_yn",
    "spark",
    "aws",
    "excel",
    "job_simp",
    "seniority",
    "desc_len",
]]

#%%
# get dummy data
df_dum = pd.get_dummies(df_model)
# train test split
# multiple linear regression
# lasso regression
# random forest
# tune models GridSearchCV
# test end samples

# %%
type(df["average-salary"])

# %%
