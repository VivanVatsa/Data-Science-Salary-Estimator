# %%
import glassdoor_scraper as gs
import pandas as pd

path = "C:/Users/Vivan/Documents/GitHub/ds-salary-proj/drivers/geckodriver"

df = gs.get_jobs("data scientist", 25, False, path, 15)
# df
#%%
df.to_csv("glassdoor_jobs.csv", index=False)
