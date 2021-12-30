import pandas as pd
from lifelines import CoxPHFitter

data = pd.read_csv('BREAST_CANCER_ANLN.csv', sep=';', index_col='id_sample')
print('data', data.shape)
print('data', data.head())

print('\nCox model')
cph = CoxPHFitter()
cph.fit(data, 'time', 'event')

print('\n--- Hazard ratio', '---')
print(cph.hazard_ratios_)


print('\n--- P-value', '---')
print(cph.summary.p)