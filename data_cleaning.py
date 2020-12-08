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

# age of company
# parsing of job description (PYTHON)

#%%
# df["hourly"] = df["Salary Estimate"].apply(lambda x: 1
#                                            if "per hour" in x.lower() else 0)
# df

# %%
# df["employer_provided"] = df["Salary Estimate"].apply(lambda x: 1
#                                            if "employer provided" in x.lower() else 0)
# df
# min_hr = minus_Kd.apply(lambda x: x.lower().replace("per hour". '').replace('employer provided salary:', ''))
