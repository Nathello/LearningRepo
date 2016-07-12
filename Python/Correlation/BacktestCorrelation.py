import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

test_file = pd.read_excel("ArgosData.xlsx")

fig = plt.figure()
merchant_spend = fig.add_subplot(1,2,1)

reported_figures = test_file["Reported Figure"]
reporting_period = np.arange(len(reported_figures))
merchant_spend.plot(reporting_period, reported_figures, "b-")
xlabels = test_file["Period"]
plt.xticks(reporting_period, xlabels, rotation = 45)


mdb_spend = merchant_spend.twinx()
mdb_spend_figures = test_file["MDB Spend Figures"]
mdb_spend.plot(reporting_period, mdb_spend_figures, "r")

correlation_graph = fig.add_subplot(1,2,2)
correlation_graph.scatter(mdb_spend_figures,reported_figures)

plt.show()