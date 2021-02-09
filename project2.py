# Project 2 Group 1
# Gordon Fjeldsted Joshua Handschin
# %% [markdown]
# # Thought: Zip codes with a higher percentage of non white individuals will have a higher percentage with a population below the poverty line

# %%
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from scipy import stats

dataSet = pd.read_csv('crime-housing-austin-2015.csv')

povertyLevelDataSet = dataSet[['Zip_Code_Housing', 'Populationbelowpovertylevel', 'HispanicorLatinoofanyrace', 'Non-WhiteNon-HispanicorLatino']]

povertyLevelDataSet = povertyLevelDataSet.drop_duplicates(subset=['Zip_Code_Housing'], keep='last')
povertyLevelDataSet = povertyLevelDataSet.dropna()
povertyLevelDataSet['Populationbelowpovertylevel'] = povertyLevelDataSet['Populationbelowpovertylevel'].str.replace('%', '').astype('float')
povertyLevelDataSet['HispanicorLatinoofanyrace'] = povertyLevelDataSet['HispanicorLatinoofanyrace'].str.replace('%', '').astype('float')
povertyLevelDataSet['Non-WhiteNon-HispanicorLatino'] = povertyLevelDataSet['Non-WhiteNon-HispanicorLatino'].str.replace('%', '').astype('float')

povertyLevelDataSet['NonWhiteSum'] = povertyLevelDataSet['HispanicorLatinoofanyrace'] + povertyLevelDataSet['Non-WhiteNon-HispanicorLatino']
# %%
print('Pearson Correlations')
pearsonr = stats.pearsonr(povertyLevelDataSet.Populationbelowpovertylevel, povertyLevelDataSet.NonWhiteSum)

print('R Value:')
print(pearsonr[0])
print('P Value:')
print(pearsonr[1])

# Scatter plot
sns.lmplot(x='NonWhiteSum', y='Populationbelowpovertylevel', data=povertyLevelDataSet, hue='Zip_Code_Housing', legend=False, fit_reg=True)
plt.xlabel('% of Non White Population')
plt.ylabel('% of the Population below the Poverty Level')
plt.figure()
# %% [markdown]
# # Turns out this thought seems true, according to the pearson correlations.
# # But what if we were to standardize this a little bit more?
# %%

# standardized data
povertyMean = povertyLevelDataSet['Populationbelowpovertylevel'].mean()
povertyStd = povertyLevelDataSet['Populationbelowpovertylevel'].std()
povertyLevelDataSet['povertyStd'] = (povertyLevelDataSet['Populationbelowpovertylevel'] - povertyMean) / povertyStd

nonWhiteMean = povertyLevelDataSet['NonWhiteSum'].mean()
nonWhiteStd = povertyLevelDataSet['NonWhiteSum'].std()
povertyLevelDataSet['nonWhiteStd'] = (povertyLevelDataSet['NonWhiteSum'] - nonWhiteMean) / nonWhiteStd

# scatterplot of standardized data
sns.lmplot(x='povertyStd', y='nonWhiteStd', data=povertyLevelDataSet, hue='Zip_Code_Housing', legend=False)
plt.figure()