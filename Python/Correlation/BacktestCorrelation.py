import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns

test_file = pd.read_excel("ArgosData.xlsx")

print(test_file)

fig, ax1 = plt.subplots()
reported_figures = test_file["Reported Figure"]
reporting_period = np.arange(len(y_axis))
ax1.plot(reporting_period, reported_figures, "b-")
xlabels = test_file["Period"]
plt.xticks(reporting_period, xlabels, rotation = 45)

ax2 = ax1.twinx()
mdb_spend_figures = test_file["MDB Spend Figures"]
ax2.plot(reporting_period, mdb_spend_figures, "r")


# ax1.plot(test_file["Reported Figure"])
# ax2.plot(test_file["MDB Spend Figures"])

# xlabels = test_file["Period"]
# plt.xticks(test_file["Reported Figure"], xlabels)
# plt.xticks(test_file["MDB Spend Figures"], xlabels)

plt.show()

# ax1.sns.pointplot(x="Period", y="Reported Figure", data = test_file)
# ax2.sns.pointplot(x="Period", y="MDB Spend Figures", data = test_file)
# plt.xticks(rotation=45)
# sns.plt.show()