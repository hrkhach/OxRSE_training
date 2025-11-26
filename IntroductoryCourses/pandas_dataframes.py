### Pandas Dataframes
import pandas as pd

# data = pd.read_csv("data/gapminder_gdp_oceania.csv")
# print(data)
#
# data = pd.read_csv("data/gapminder_gdp_oceania.csv", index_col="country")
# print(data)
#
# data.info()
# print(data.columns)
# print(data.T)
# print(data.describe())
#
# americas = pd.read_csv("data/gapminder_gdp_americas.csv", index_col="country")
# print(americas.describe())
#
# help(americas.head)
# help(americas.tail)
#
# print(americas.head(3))
# print(americas.T.tail(3).T)
#
# americas.to_csv("data/processed.csv")
# help(americas.to_csv)
#
# data = pd.read_csv("data/gapminder_gdp_europe.csv", index_col="country")
# print(data.head())
# print(data.iloc[0, 0])
#
# print(data.loc["Albania", "gdpPercap_1952"])
#
# print(data.loc["Albania", :])
# print(data.loc["Albania"])
# print(data.loc[:, "gdpPercap_1952"])
#
# print(data.loc["Italy":"Poland", "gdpPercap_1962":"gdpPercap_1972"])
#
# print(data.loc["Italy":"Poland", "gdpPercap_1962":"gdpPercap_1972"].max())
# print(data.loc["Italy":"Poland", "gdpPercap_1962":"gdpPercap_1972"].min())

# # Use a subset of data to keep output readable
# subset = data.loc["Italy":"Poland", "gdpPercap_1962":"gdpPercap_1972"]
# print("Subset of data:\n", subset)
#
# # Which values were greater than 10000?
# print("\nWhere are values large?\n", subset > 10000)
#
# mask = subset > 10000
# print(subset[mask])
#
# print(subset[subset > 10000].describe())
#
## Group By: split-apply-combine
# mask_higher = data > data.mean()
# wealth_score = mask_higher.aggregate("sum", axis=1) / len(data.columns)
# print(wealth_score)
#
# print(data.groupby(wealth_score).sum())
#
# print(data.loc["Serbia", "gdpPercap_2007"])
#
# print(data.iloc[0:2, 0:2])
# print(data.loc["Albania":"Belgium", "gdpPercap_1952":"gdpPercap_1962"])
#
# first = pd.read_csv("data/gapminder_all.csv", index_col="country")
# second = first[first["continent"] == "Americas"]
# third = second.drop("Puerto Rico")
# fourth = third.drop("continent", axis=1)
# fourth.to_csv("data/result.csv")
#
# americas = first[first["continent"] == "Americas"]
# print(americas)
#
# not_americas = first[first["continent"] != "Americas"]
# print(not_americas)

data = pd.read_csv("data/gapminder_gdp_europe.csv", index_col="country")
# print(data.idxmin())
# print(data.idxmax())

# # Practice with Selection
# # 1
# print(data["gdpPercap_1982"])
#
# # 2
# print(data.loc["Denmark"])
#
# # 3
# print(data.loc[:, "gdpPercap_1985":])
#
# # 4
# print(data.loc[:, "gdpPercap_2007"] / data.loc[:, "gdpPercap_1952"])

print(dir(data))
print(data.median())