import pandas as pd
import matplotlib.pyplot as plt

from lifelines import KaplanMeierFitter

input_file = 'Survival_TCGA-BRCA_os.csv'
data = pd.read_csv(input_file , sep = ';', index_col='id_sample')

kmf = KaplanMeierFitter()
kmf.fit(data['time'], data['event'])

fig = plt.figure(figsize=(4, 4))
ax = fig.add_axes([0.15, 0.15, 0.75, 0.75])

kmf.plot(ax=ax, ci_show=True, show_censors=True, label='Kaplan-Meier\nestimator')

ax.set_ylabel('Survival probability')
ax.set_xlabel('Time in months')
ax.set_ylim([-0.05, 1.05])

plt.show()

fig.savefig('survival_curve_Kaplan_Meier_lifelines.png', dpi=300, format='png', bbox_inches='tight')