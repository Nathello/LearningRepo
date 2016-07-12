import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

test_file = pd.read_excel("ArgosData.xlsx")

print(test_file)
#print(test_file["Period"])

sns.pointplot(x=test_file["Period"], y=test_file["Reported Figure"])
sns.plt.show()