import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns

test_file = pd.read_excel("ArgosData.xlsx")

print(test_file)

fig, ax1 = plt.subplots()
y_axis = test_file["Reported Figure"]
x_axis = np.arange(len(y_axis))
ax1.plot(x_axis, y_axis, "b-")
xlabels = test_file["Period"]
plt.xticks(x_axis, xlabels, rotation = 45)

plt.show()


# ax2 = ax1.twinx()

# ax1.plot(test_file["Reported Figure"])
# ax2.plot(test_file["MDB Spend Figures"])

# xlabels = test_file["Period"]
# plt.xticks(test_file["Reported Figure"], xlabels)
# plt.xticks(test_file["MDB Spend Figures"], xlabels)

# plt.show()

# ax1.sns.pointplot(x="Period", y="Reported Figure", data = test_file)
# ax2.sns.pointplot(x="Period", y="MDB Spend Figures", data = test_file)
# plt.xticks(rotation=45)
# sns.plt.show()