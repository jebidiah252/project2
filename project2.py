# Project 2 Group 1
# Gordon Fjeldsted Joshua Handschin
# %% [markdown]
# # Thought: Zip codes with a higher percentage of non white individuals will have a higher percentage with a population below the poverty line
# %%
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

dataSet = pd.read_csv('crime-housing-austin-2015.csv')

povertyLevelDataSet = dataSet[['Zip_Code_Housing', 'Populationbelowpovertylevel', 'HispanicorLatinoofanyrace', 'Non-WhiteNon-HispanicorLatino']]

povertyLevelDataSet = povertyLevelDataSet.drop_duplicates(subset=['Zip_Code_Housing'], keep='last')
povertyLevelDataSet = povertyLevelDataSet.dropna()
povertyLevelDataSet['Populationbelowpovertylevel'] = povertyLevelDataSet['Populationbelowpovertylevel'].str.replace('%', '').astype('float')
povertyLevelDataSet['HispanicorLatinoofanyrace'] = povertyLevelDataSet['HispanicorLatinoofanyrace'].str.replace('%', '').astype('float')
povertyLevelDataSet['Non-WhiteNon-HispanicorLatino'] = povertyLevelDataSet['Non-WhiteNon-HispanicorLatino'].str.replace('%', '').astype('float')

povertyLevelDataSet['NonWhiteSum'] = povertyLevelDataSet['HispanicorLatinoofanyrace'] + povertyLevelDataSet['Non-WhiteNon-HispanicorLatino']
# %%
sns.scatterplot(x='NonWhiteSum', y='Populationbelowpovertylevel', data=povertyLevelDataSet)

# %% [markdown]
# # Turns out this thought is true.