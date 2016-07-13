import numpy as np
import pandas as pd
from pandas.tools.plotting import table
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

test_file = pd.read_excel("ArgosData.xlsx")

fig = plt.figure()
merchant_spend = fig.add_subplot(2,2,1)


#test_file.plot(table=True, ax=merchant_spend)

reported_figures = test_file["Reported Figure"]
reporting_period = np.arange(len(reported_figures))
merchant_spend.plot(reporting_period, reported_figures, "b-")
xlabels = test_file["Period"]
plt.xticks(reporting_period, xlabels, rotation = 45)


mdb_spend = merchant_spend.twinx()
mdb_spend_figures = test_file["MDB Spend Figures"]
mdb_spend.plot(reporting_period, mdb_spend_figures, "r")

data_table = fig.add_subplot(2,2,2)
data_table.axis('off')
data_table.axes.get_xaxis().set_visible(False)
data_table.axes.get_yaxis().set_visible(False)
the_table = table(data_table, test_file, loc='center')
the_table.auto_set_font_size(False) 
the_table.set_fontsize(10)

correlation_graph = fig.add_subplot(2,2,3)
correlation_graph.scatter(mdb_spend_figures,reported_figures)

plt.show()