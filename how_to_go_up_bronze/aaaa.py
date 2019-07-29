#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

#%%
df_summoners = pd.read_csv('C:\output\list\summonerGeneral.csv')


#%%
df_summoners.columns
"""
Index(['id', 'tier', 'division', 'summonerId', 'summonerName', 'leaguePoints',
       'win', 'lose', 'total', 'veteran', 'inactive', 'freshBlood',
       'hotStreak'],
      dtype='object')
"""
#%%
df_match_total = df_summoners['total']
# plt.hist(np.round(df_match_total, -2), bins=20)
plt.hist(df_match_total, bins=20)
plt.xlabel("match frequency")
plt.ylabel("summoner count")

#%%
# ((1598, 13), (222, 13))
df_summoners.query('total < 100').shape, df_summoners.query('100 <= total < 200').shape

#%%
# (411, 13)
df_summoners.query('total >= 100').shape

#%%
df_dropped = df_summoners.drop(['id', 'summonerId', 'summonerName'], axis=1)

#%%
df_dropped.head()

#%%
df_target = df_dropped.query('total >= 100')
df_target.describe()

#%%
# target is between 25% and 75% of total column
df_target.query('130 <= total <= 285').shape
df_analysis_target = df_target.query('130 <= total <= 285')

#%%
