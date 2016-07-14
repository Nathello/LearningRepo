import numpy as np
import pandas as pd
from pandas.tools.plotting import table
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter 
from scipy.stats.stats import pearsonr

test_file = pd.read_excel("ArgosData.xlsx")

#This step adds two columns to the data converting it to strings with currency for presentation

int_reported_figures = pd.to_numeric(test_file["Reported Figure"])
int_mdb_spend = pd.to_numeric(test_file["MDB Spend Figures"])

test_file["Reported Figures (£)"] = ['£{:20,.2f}'.format(x) for x in int_reported_figures]
test_file["MDB Spend Figures (£)"] = ['£{:20,.2f}'.format(x) for x in int_mdb_spend]

fig = plt.figure()
fig.suptitle("MDB Merchant Backtest", fontsize=20, fontweight='bold')

#First plot - line graph mapping reported spend data against mdb spend

merchant_spend = fig.add_subplot(2,2,1)
merchant_spend.set(xlabel=("Reporting Period"), ylabel=("Reported Spend(£000s)"))
merchant_spend.get_yaxis().set_major_formatter(FuncFormatter(lambda x, p: format(int(x/1000), ',')))
reported_figures = test_file["Reported Figure"]
reporting_period = np.arange(len(reported_figures))
merchant_spend_series = merchant_spend.plot(reporting_period, reported_figures, "b-", label="Reported Figure")
xlabels = test_file["Period"]
plt.xticks(reporting_period, xlabels, rotation = 45)
merchant_spend_legend = merchant_spend.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=2, mode="expand", borderaxespad=0.)


mdb_spend = merchant_spend.twinx()
mdb_spend.set(ylabel=("MDB Spend(£000s)"))
mdb_spend.get_yaxis().set_major_formatter(FuncFormatter(lambda x, p: format(int(x/1000), ',')))
mdb_spend_figures = test_file["MDB Spend Figures"]
mdb_spend_series = mdb_spend.plot(reporting_period, mdb_spend_figures, "r")
mdb_spend_legend = mdb_spend.legend(frameon=False, bbox_to_anchor=(0., 1.006, 1., .1), loc='center right', borderaxespad=0.)

#Second plot - data table showing the data with currency mark

data_table = fig.add_subplot(2,2,2)
data_table.axis('off')
the_table = table(data_table, test_file[["Reported Figures (£)", "MDB Spend Figures (£)"]], rowLabels=xlabels, loc='center')
the_table.auto_set_font_size(False) 
the_table.set_fontsize(10)

#Third plot - correlation scatter plot of reported spend vs mdb spend with line of best fit 

correlation_graph = fig.add_subplot(2,2,3)
correlation_graph.set(title=("Correlation"), xlabel=("MDB Spend(£000s)"), ylabel=("Reported Spend(£000s)"))
correlation_graph.get_yaxis().set_major_formatter(FuncFormatter(lambda x, p: format(int(x/1000), ',')))
correlation_graph.get_xaxis().set_major_formatter(FuncFormatter(lambda x, p: format(int(x/1000), ',')))
correlation_graph.scatter(mdb_spend_figures,reported_figures)
# calc the trendline (linear)
z = np.polyfit(mdb_spend_figures, reported_figures, 1)
p = np.poly1d(z)
correlation_graph.plot(mdb_spend_figures,p(mdb_spend_figures),"r--")
r, p_value = pearsonr(mdb_spend_figures, reported_figures)
r_sq = r ** 2
plt.annotate("r^2 = {0:.2f}".format(r_sq), (0.05, 0.9), xycoords="axes fraction")
# plt.annotate("P Value = {0:.2f}".format(p_value), (0.05, 0.85), xycoords="axes fraction")
plt.annotate("P Value = {0:.2f}".format(p_value), (0.05, 0.85), xycoords="axes fraction")

plt.subplots_adjust(top=0.88, bottom=0.04, left=0.11, right=0.90, hspace=0.4, wspace=0.61)

plt.show()