import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")
categorical_cols = ['sex', 'smoker', 'day', 'time']
df[categorical_cols] = df[categorical_cols].astype('category')

sns.set_theme(style="darkgrid")
fig, axs = plt.subplots(2, 2, figsize=(14, 10))

sns.scatterplot(x='total_bill', y='tip', hue='sex', data=df, ax=axs[0, 0])
axs[0, 0].set_title("Total Bill vs Tip")

sns.boxplot(x='day', y='tip', data=df, ax=axs[0, 1])
axs[0, 1].set_title("Tip Distribution by Day")

corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm", ax=axs[1, 0])
axs[1, 0].set_title("Correlation Heatmap")

avg_tip_by_size = df.groupby('size')['tip'].mean().reset_index()
sns.lineplot(x='size', y='tip', data=avg_tip_by_size, ax=axs[1, 1])
axs[1, 1].set_title("Average Tip by Group Size")

plt.show()
