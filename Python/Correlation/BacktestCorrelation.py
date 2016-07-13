import numpy as np
import pandas as pd
from pandas.tools.plotting import table
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter 
from scipy.stats.stats import pearsonr

test_file = pd.read_excel("ArgosData.xlsx")

fig = plt.figure()
merchant_spend = fig.add_subplot(2,2,1)
merchant_spend.get_yaxis().set_major_formatter(FuncFormatter(lambda x, p: format(int(x), ',')))
reported_figures = test_file["Reported Figure"]
reporting_period = np.arange(len(reported_figures))
merchant_spend.plot(reporting_period, reported_figures, "b-")
xlabels = test_file["Period"]
plt.xticks(reporting_period, xlabels, rotation = 45)


mdb_spend = merchant_spend.twinx()
mdb_spend.get_yaxis().set_major_formatter(FuncFormatter(lambda x, p: format(int(x), ',')))
mdb_spend_figures = test_file["MDB Spend Figures"]
mdb_spend.plot(reporting_period, mdb_spend_figures, "r")

data_table = fig.add_subplot(2,2,2)
data_table.axis('off')
the_table = table(data_table, np.round(test_file[["Reported Figure", "MDB Spend Figures"]],0), rowLabels=xlabels, loc='center')
the_table.auto_set_font_size(False) 
the_table.set_fontsize(10)

correlation_graph = fig.add_subplot(2,2,3)
correlation_graph.get_yaxis().set_major_formatter(FuncFormatter(lambda x, p: format(int(x), ',')))
correlation_graph.get_xaxis().set_major_formatter(FuncFormatter(lambda x, p: format(int(x), ',')))
correlation_graph.scatter(mdb_spend_figures,reported_figures)
# calc the trendline (linear)
z = np.polyfit(mdb_spend_figures, reported_figures, 1)
p = np.poly1d(z)
correlation_graph.plot(mdb_spend_figures,p(mdb_spend_figures),"r--")
r, p_value = pearsonr(mdb_spend_figures, reported_figures)
r_sq = r ** 2
plt.annotate("r^2 = {0:.2f}".format(r_sq), (0.05, 0.9), xycoords="axes fraction")
plt.annotate("P Value = {0:.4f}".format(p_value), (0.05, 0.85), xycoords="axes fraction")

plt.show()