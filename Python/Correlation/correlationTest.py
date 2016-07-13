import pandas as pd
from scipy.stats.stats import pearsonr

test_file = pd.read_excel("ArgosData.xlsx")

reported_figures = test_file["Reported Figure"]
mdb_spend_figures = test_file["MDB Spend Figures"]

print(pearsonr(reported_figures, mdb_spend_figures))