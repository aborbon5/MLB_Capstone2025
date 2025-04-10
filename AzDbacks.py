import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file_path = 'C:/Users/Marissa/Documents/MasterMLB.xlsx'

df = pd.read_excel(file_path, sheet_name = 'AzDbacks')

print(df.head())

#Remove whitespaces and unwanted characters
df['Date'] = df['Date'].str.strip()
df['Date'] = df['Date'].str.replace(r'\s\(\d+\)', '', regex=True)
df['Date'] = df['Date'].str.replace(r'^[A-Za-z]+, ', '', regex=True)

df['Date'] = df['Date'] + ' ' + df['Year'].astype(str)

#Make sure date is read as such
df['Date'] = pd.to_datetime(df['Date'], format = '%b %d %Y')
print(df['Date'].head())

#Create 10 Year Attendance (base plot)
sns.set(rc={"figure.figsize":(14,10)})
sns.set_style("darkgrid")
custom_palette = sns.color_palette(["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", 
                                   "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf", "#ff99cc"])

sns.lineplot(data = df, x = "Date", y = "Attendance", hue = "Year", palette = custom_palette).set(xlabel = "Game", ylabel = "Attendance", title = "Arizona Diamondbacks Attendance");

#Set x-axis limits
plt.xlim(df['Date'].min(), df['Date'].max())
plt.legend(loc = "best")
plt.show()

#Create zoomed in plots
sns.lineplot(data = df, x = "Date", y = "Attendance")
plt.xlim(pd.to_datetime('2014-03-22'), pd.to_datetime('2014-09-30')) #Games typically start in March and end in Sept
plt.show()