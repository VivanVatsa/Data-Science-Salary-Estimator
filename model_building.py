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
    "num_comp",
    "hourly",
]]
# get dummy data

# train test split
# multiple linear regression
# lasso regression
# random forest
# tune models GridSearchCV
# test end samples

# %%
