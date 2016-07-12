import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

test_file = pd.read_excel("ArgosData.xlsx")

print(test_file)
#print(test_file["Period"])

backtest_graph = sns.pointplot(x="Period", y="Reported Figure", data = test_file)
plt.xticks(rotation=45)
sns.plt.show(backtest_graph)