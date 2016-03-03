import pandas as pd

df = pd.read_csv("IvyTeamScores.csv")
df["Total"] = df.Brown + df.Columbia + df.Cornell + df.Dartmouth + df.Harvard + df.Penn + df.Princeton + df.Yale
df = df.drop("Unnamed: 0", axis=1)

Total = np.array(df["Total"])
print(Total)

# df2 = df.divide(df["Total"], axis=1)

df/df["Total"]