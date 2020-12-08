#%%
# from numpy.core.fromnumeric import size
import pandas as pd

df = pd.read_csv("glassdoor_jobs.csv")

df = df[df["Salary Estimate"] != "-1"]
df

# TO DO IN DATA CLEANING
# -------------------
# salary parsing

#%%
salary = df["Salary Estimate"].apply(lambda x: x.split("(")[0])
# salary
minus_Kd = salary.apply(
    lambda x: x.replace("K", "").replace("₹", "").replace(",", ""))
minus_Kd[0]
df["min_salary"] = minus_Kd.apply(lambda x: int(x.split("-")[0]))
# df
# #%%
# type(df["min_salary"])

# df["min_salary"].dtype
df["max_salary"] = minus_Kd.apply(lambda x: int((x.split("-")[1])))
# df
df["average-salary"] = (df.min_salary + df.max_salary) / 2
# df
df["currency"] = "LAKh"
# df
df

# company name text only
#%%
df["company_txt"] = df["Company Name"].apply(lambda x: x.split("\n")[0])
df

# state field
#%%
df.Location.value_counts()

#%%
# 2 ways to delete undesired column from the data frame
# 1.
# del df["Headquarters"]
# df = df.drop("Headquarters", 1)
df = df.drop("Competitors", 1)
df
# age of company
#%%

df["age"] = df.Founded.apply(lambda x: x if x < 1 else 2020 - x)
df

# parsing of job description (PYTHON)
#%%
# will check all job descriptions keyword - analysis
# python
df["analysis"] = df["Job Description"].apply(lambda x: 1
                                             if "analysis" in x.lower() else 0)
df.analysis.value_counts()
#%%
df["Job Description"][0]
# df["hourly"] = df["Salary Estimate"].apply(lambda x: 1
#                                            if "per hour" in x.lower() else 0)
# df

# %%
df
# df["employer_provided"] = df["Salary Estimate"].apply(lambda x: 1
#                                            if "employer provided" in x.lower() else 0)
# df
# min_hr = minus_Kd.apply(lambda x: x.lower().replace("per hour". '').replace('employer provided salary:', ''))

# %%
# *df cleaned*
df_out = df
df_out
# %%
df_out.to_csv("GL_sal_data_cleaned.csv", index=False)

# %%
pd.read_csv("GL_sal_data_cleaned.csv")

# %%
