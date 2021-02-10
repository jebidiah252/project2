# Project 2 Group 1
# Gordon Fjeldsted Joshua Handschin
# %% [markdown]
# # Thought: Zip codes with a higher percentage of non white individuals will have a higher percentage with a population below the poverty line

# %%
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from scipy import stats

#%%
dataSet = pd.read_csv('crime-housing-austin-2015.csv')

#%%
povertyLevelDataSet = dataSet[['Zip_Code_Housing', 'Populationbelowpovertylevel', 'HispanicorLatinoofanyrace', 'Non-WhiteNon-HispanicorLatino']]


#%%
povertyLevelDataSet = povertyLevelDataSet.drop_duplicates(subset=['Zip_Code_Housing'], keep='last')
povertyLevelDataSet = povertyLevelDataSet.dropna()
povertyLevelDataSet['Populationbelowpovertylevel'] = povertyLevelDataSet['Populationbelowpovertylevel'].str.replace('%', '').astype('float')
povertyLevelDataSet['HispanicorLatinoofanyrace'] = povertyLevelDataSet['HispanicorLatinoofanyrace'].str.replace('%', '').astype('float')
povertyLevelDataSet['Non-WhiteNon-HispanicorLatino'] = povertyLevelDataSet['Non-WhiteNon-HispanicorLatino'].str.replace('%', '').astype('float')

povertyLevelDataSet['NonWhiteSum'] = povertyLevelDataSet['HispanicorLatinoofanyrace'] + povertyLevelDataSet['Non-WhiteNon-HispanicorLatino']
# %%


display(stats.pearsonr(povertyLevelDataSet.Populationbelowpovertylevel, povertyLevelDataSet.NonWhiteSum))

sns.regplot(y='Populationbelowpovertylevel', x='NonWhiteSum', data=povertyLevelDataSet, scatter_kws={"color": "green", 'alpha': 0.3}, line_kws={"color":"red"})
# sns.scatterplot(x='NonWhiteSum', y='Populationbelowpovertylevel', data=povertyLevelDataSet)
#%%
sns.regplot(x='NonWhiteSum', y='Populationbelowpovertylevel', data=povertyLevelDataSet)
plt.figure()

# %% [markdown]
# # Turns out this thought seems true, according to the pearson correlations.
#%%
PovertyByZip = dataSet[['Zip_Code_Housing', 'Populationbelowpovertylevel']]
PovertyByZip = PovertyByZip[PovertyByZip.Zip_Code_Housing != 78617]
sns.scatterplot(x='Zip_Code_Housing', y='Populationbelowpovertylevel', data=povertyLevelDataSet)

#%%

dataSet = pd.read_csv('crime-housing-austin-2015.csv')

povertyLevelDataSet = dataSet[['Zip_Code_Housing', 'Populationbelowpovertylevel',
                               'HispanicorLatinoofanyrace', 'Non-WhiteNon-HispanicorLatino']]

povertyLevelDataSet = povertyLevelDataSet.drop_duplicates(
    subset=['Zip_Code_Housing'], keep='last')
povertyLevelDataSet = povertyLevelDataSet.dropna()
povertyLevelDataSet['Populationbelowpovertylevel'] = povertyLevelDataSet['Populationbelowpovertylevel'].str.replace('%','').astype('float')
povertyLevelDataSet['HispanicorLatinoofanyrace'] = povertyLevelDataSet['HispanicorLatinoofanyrace'].str.replace('%', '').astype('float')
povertyLevelDataSet['Non-WhiteNon-HispanicorLatino'] = povertyLevelDataSet['Non-WhiteNon-HispanicorLatino'].str.replace('%', '').astype('float')

povertyLevelDataSet['NonWhiteSum'] = povertyLevelDataSet['HispanicorLatinoofanyrace'] + povertyLevelDataSet['Non-WhiteNon-HispanicorLatino']
# %%
print('Pearson Correlations')
pearsonr = stats.pearsonr(
    povertyLevelDataSet.Populationbelowpovertylevel, povertyLevelDataSet.NonWhiteSum)

print('R Value:')
print(pearsonr[0])
print('P Value:')
print(pearsonr[1])

# Scatter plot
sns.lmplot(x='NonWhiteSum', y='Populationbelowpovertylevel',
           data=povertyLevelDataSet, hue='Zip_Code_Housing', legend=False, fit_reg=True)
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
sns.lmplot(y='povertyStd', x='nonWhiteStd', data=povertyLevelDataSet, hue='Zip_Code_Housing', legend=False, logistic=True)

plt.xlabel('Non White Population')
plt.ylabel('Below the Poverty Level')
plt.xlim(-2,2)
plt.figure()

# %%
res = stats.ttest_ind(povertyLevelDataSet['NonWhiteSum'], povertyLevelDataSet['Populationbelowpovertylevel'])
display(res)

#%%
sns.boxplot(x='NonWhiteSum', y='Populationbelowpovertylevel', data=povertyLevelDataSet)
