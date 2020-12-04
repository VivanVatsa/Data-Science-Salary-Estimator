# %%
import glassdoor_scraper as gs
import pandas as pd

path = "C:/Users/Vivan/Documents/GitHub/ds-salary-proj/geckodriver"

df = gs.get_jobs("data scientist", 15, False, path, 15)
#%%
df
# %%
