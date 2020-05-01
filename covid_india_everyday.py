import plotly.graph_objects as go
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('C:/Users/Prakhar/Downloads/owid-covid-data.csv')
print(df.columns)

print(df[df["location"].isin(['India'])])
df_india = df[df["location"].isin(['India'])]
print(df_india)
df_india[-7:].plot(kind='bar', x='date', y=['total_cases', 'new_cases','total_deaths','new_deaths','new_tests'])
plt.show()

# sel_country=input('Provide a name of Country: ')

# df_selection = df.loc()
#
#
# # df_selection = df[df["location"].isin([{}])].to_string().format("India")
#
# print(df_selection)