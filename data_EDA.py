#%%
import pandas as pd

# matplotlib = this is for data visualization
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("GL_sal_data_cleaned.csv")
df.head()

# %%
df.columns


# %%
# part of Exploratory data analysis is also Feature Engineering.
def title_simplifier(title):
    if "data scientist" in title.lower():
        return "data scientist"
    elif "data engineer" in title.lower():
        return "data engineer"
    elif "analyst" in title.lower():
        return "analyst"
    elif "machine learning" in title.lower():
        return "mle"
    elif "manager" in title.lower():
        return "manager"
    elif "director" in title.lower():
        return "director"
    else:
        return "na"


def seniority(title):
    if ("sr" in title.lower() or "senior" in title.lower()
            or "sr" in title.lower() or "lead" in title.lower()
            or "principal" in title.lower()):
        return "senior"
    elif "jr" in title.lower() or "jr." in title.lower():
        return "jr"
    else:
        return "na"


# --x----
## Job title and seniority
# --x---

##  Fix state Los Angeles

##  Job description length

##  Competitor count

## hourly wage to annual

# remove new line from job title

#%%
df["job_simp"] = df["Job Title"].apply(title_simplifier)

df.job_simp.value_counts()

# %%
df["Seniority"] = df["Job Title"].apply(seniority)

df.Seniority.value_counts()

# %%
df.Location.value_counts()
# %%
df["desc_len"] = df["Job Description"].apply(lambda x: len(x))
df["desc_len"]

# %%
df["min_salary"] = df.apply(lambda x: x.min_salary * 2
                            if x.hourly == 1 else x.min_salary,
                            axis=1)

df["max_salary"] = df.apply(lambda x: x.max_salary * 2
                            if x.hourly == 1 else x.max_salary,
                            axis=1)

# df[df["hourly" == 1]][[]]
# df[df.hourly == 1][["hourly", "min_salary", "max_salary"]]

# %%
df.columns

# %%
df.company_txt

# %%
# help(df.describe())
# used to check all the mean median and other metrics of the data provided
df.describe()

# %%
df.Ratings.hist()

# %%
df.columns
# %%
"""
hist() - func used to display the Histogram of the given / fetched data
"""
df.Rating.hist()

# %%
type(df.Rating.hist())

#%%
df["average-salary"].hist()
# %%
df.age.hist()
# %%
# using blogspot to plotting box for grouping by a certain attribute

df.boxplot(column=["age", "average-salary", "Rating"])

# %%
df.boxplot(column="Rating")
# %%
df[["age", "average-salary", "Rating"]].corr()

#%%
cmap = sns.diverging_palette(230, 20, as_cmap=True)
sns.heatmap(
    df[["age", "average-salary", "Rating"]].corr(),
    vmax=0.3,
    center=0,
    cmap=cmap,
    square=True,
    linewidths=0.5,
    cbar_kws={"shrink": 0.5},
)

# %%
df["desc_len"] = df["Job Description"].apply(lambda x: len(x))
df["desc_len"]

#%%
df
# %%
cmap = sns.diverging_palette(230, 20, as_cmap=True)
sns.heatmap(
    df[["age", "average-salary", "Rating", "desc_len"]].corr(),
    vmax=0.3,
    center=0,
    cmap=cmap,
    square=True,
    linewidths=0.5,
    cbar_kws={"shrink": 0.5},
)

# %%
df.columns
# %%
df_cat = df[[
    "Location",
    "Size",
    "Type of ownership",
    "Industry",
    "Sector",
    "Revenue",
    "company_txt",
    "python_yn",
    "data",
    "analysis",
    "job_simp",
    "Seniority",
]]

#%%
for i in df_cat.columns:
    cat_num = df_cat[i].value_counts()
    print("Graph for %s: total =%d" % (i, len(cat_num)))
    chart = sns.barplot(x=cat_num.index, y=cat_num)
    chart.set_xticklabels(chart.get_xticklabels(), rotation=90)
    plt.show()
# %%
