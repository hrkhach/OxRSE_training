import pandas as pd
import glob
import matplotlib.pyplot as plt

# for filename in ["data/gapminder_gdp_africa.csv", "data/gapminder_gdp_asia.csv"]:
#     data = pd.read_csv(filename, index_col="country")
#     print(filename, data.min())
#
# print("all csv files in data directory:", glob.glob("data/*.csv"))
# print("all PDB files:", glob.glob("data/*.pdb"))
#
# for filename in glob.glob("data/gapminder_*.csv"):
#     data = pd.read_csv(filename)
# #     print(filename, data["gdpPercap_1952"].min())
#
# fewest = float("Inf")
# for filename in glob.glob('data/*.csv'):
#     dataframe = pd.read_csv(filename)
#     fewest = min(fewest, dataframe.shape[0])
# print('smallest file has', fewest, 'records')
#

# # Comparing data
# fig, ax = plt.subplots(1, 1)
# for filename in glob.glob("data/gapminder_gdp*.csv"):
#     dataframe = pd.read_csv(filename)
#     for col in dataframe.columns:
#         if col == "continent" or col == "country":
#             dataframe.drop(col, axis=1, inplace=True)
#     # extract <regionfrom the filename, expected to be in the format 'data/gapminder_gdp_<region>.csv'.
#     # we will split the string using the split method and `_` as our separator,
#     # retrieve the last string in the list that split returns (`<region>.csv`),
#     # and then remove the `.csv` extension from that string.
#     region = filename.split("_")[-1][:-4]
#     dataframe.mean().plot(ax=ax, label=region)
# plt.legend()
# plt.show()

# dataframe = pd.read_csv("data/gapminder_gdp_americas.csv")
# for col in dataframe.columns:
#     if col == "continent" or col == "country":
#         dataframe.drop(col, axis=1, inplace=True)
# print(dataframe)

# Dealing with File Paths
from pathlib import Path

p = Path("data/gapminder_gdp_africa.csv")
print(p.parent), print(p.stem), print(p.suffix)
print(p.name)
print(dir(p))