import pandas as pd
import matplotlib.pyplot as plt

from sksurv.nonparametric import kaplan_meier_estimator

input_file = 'Survival_TCGA-BRCA_os.csv'
data = pd.read_csv(input_file , sep = ';', index_col='id_sample')

data['event_bool'] = data['event'].astype(bool)

time, survival_probability = kaplan_meier_estimator(data['event_bool'], data['time'])

fig = plt.figure(figsize=(4, 4))
ax = fig.add_axes([0.15, 0.15, 0.75, 0.75])

ax.step(time, survival_probability, where='post', label='Kaplan-Meier\nestimator')

ax.set_ylabel('Survival probability')
ax.set_xlabel('Time in months')
ax.set_ylim([-0.05, 1.05])
ax.legend()

plt.show()

fig.savefig('survival_curve_Kaplan_Meier_scikit_survival.png', dpi=300, format='png', bbox_inches='tight')