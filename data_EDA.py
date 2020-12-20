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

de
# %%
df["Seniority"] = df["Job Title"].apply(seniority)

df.Seniority.value_counts()

# %%
df.Location.value_counts()
# %%
df["desc_len"] = df["Job Description"].apply(lambda x: len(x))
df["desc_len"]

# %%
# df["min_salary"] = df.apply(lambda x: x.min_salary * 2
#                             if x.hourly == 1 else x.min_salary,
#                             axis=1)

# df["max_salary"] = df.apply(lambda x: x.max_salary * 2
#                             if x.hourly == 1 else x.max_salary,
#                             axis=1)

# df[df["hourly" == 1]][[]]
# df[df.hourly == 1][["hourly", "min_salary", "max_salary"]]

# %%
# df.

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
pd.

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
df.columns

#%%
for i in df_cat[["Location", "company_txt", "Industry"]].columns:
    # cat_num = df_cat[i][:10].value_counts()
    cat_num = df_cat[i].value_counts()[:10]
    print("Graph for %s: total =%d" % (i, len(cat_num)))
    chart = sns.barplot(x=cat_num.index, y=cat_num)
    chart.set_xticklabels(chart.get_xticklabels(), rotation=90)
    plt.show()

# %%
# starting pivot tables

pd.pivot_table(df, index="job_simp", values="average-salary")

# # %%
# pd.pivot_table(df, index=["job_simp", "seniority"], values="average-salary")

# %%
df.columns
pd.to_csv()
# %%
pd.pivot_table(df, index=["job_simp", "Seniority"], values="average-salary")

# %%
pd.pivot_table(df, index=["Location", "job_simp"],
               values="average-salary").sort_values("average-salary",
                                                    ascending=False)

# %%
pd.pivot_table(df, index=["Location", "job_simp"],
               values="average-salary").sort_values("Location",
                                                    ascending=False)

# %%
pd.pivot_table(df[df.job_simp == "data scientist"],
               index="Location",
               values="average-salary").sort_values("Location",
                                                    ascending=False)

# %%
df.columns
# %%
df_pivots = df[[
    "Rating",
    "Industry",
    "Sector",
    "Revenue",
    "python_yn",
    "Type of ownership",
    "average-salary",
]]

# %%
for i in df_pivots.columns:
    print(i)
    print(
        pd.pivot_table(df_pivots, index=i,
                       values="average-salary").sort_values("average-salary",
                                                            ascending=False))

# %%
pd.pivot_table(
    df_pivots,
    index="Revenue",
    columns="python_yn",
    values="average-salary",
    aggfunc="count",
)

# %%

# this is the fun part of EDA
# this is to GENERATION OF WORDCLOUD
#
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# %%

nltk.download("stopwords")
nltk.download("punkt")
words = " ".join(df["Job Description"])


def punctuation_stop(text):
    """remove punctuation and stop words"""
    filtered = []
    stop_words = set(stopwords.words("english"))
    word_tokens = word_tokenize(text)
    for w in word_tokens:
        if w not in stop_words and w.isalpha():
            filtered.append(w.lower())
    return filtered


words_filtered = punctuation_stop(words)

text = " ".join([ele for ele in words_filtered])

wc = WordCloud(
    background_color="white",
    random_state=1,
    stopwords=STOPWORDS,
    max_words=2000,
    width=800,
    height=1500,
)
wc.generate(text)

plt.figure(figsize=[10, 10])
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()

# %%
df.to_csv("data_eda.csv")
# %%
df.columns

# %%
