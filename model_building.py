#%%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("data_EDA.csv")
# choose the relevant columns

#%%
df.columns

#%%
df_model = [[
    "average-salary",
    "Rating",
    "Size",
    "Type of ownership",
    "Industry",
    "Sector",
    "Revenue",
    "Location",
    "age",
    "python_yn",
    "job_simp",
    "Seniority",
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
