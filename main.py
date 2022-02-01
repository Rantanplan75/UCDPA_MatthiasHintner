import pandas as pd

# Loading of csv files into panda dataframes
df = pd.read_csv('athlete_events.csv')
df1 = pd.read_csv('noc_regions.csv')

# Merge the athlete_event table with the noc_region table with a left join
dfjoined = df.merge(df1, on='NOC', how='left')

print(dfjoined.info())


# Built-in Pause. Waiting for input to continue
print()
input("JOINED DATA MERGE DATAFRAME - Press Enter to continue...")
print()


# selecting and rearranging columns using Panda loc
dfjoined_select = dfjoined.loc[:, ['Year', 'region', 'Name', 'Sex', 'Season', 'Sport', 'Medal', 'Age']]
print(dfjoined_select.info())

# Built-in Pause. Waiting for input to continue
print()
input("SELECTED COLUMNS - Press Enter to continue...")
print()


# Sorting of values within columns
dfjoined_sorted = dfjoined_select.sort_values(['region', 'Year'], ascending=(True, False))
print(dfjoined_sorted.head())


# Built-in Pause. Waiting for input to continue
print()
input("SORTED ROW VALUES - Press Enter to continue...")
print()


# Selecting only Olympic games after the World War II >1945 using Panda iloc
dfjoined_sorted_WII = dfjoined_sorted.loc[dfjoined_sorted['Year'] >= 1945]
print("HERE")
print(dfjoined_sorted_WII.info())

# Built-in Pause. Waiting for input to continue
print()
input("SLICED OFF PRE-WWII GAMES - Press Enter to continue...")
print()

# Search and Clean all NaN values in column region and Medal
dfjoined_sorted_cleaned1 = dfjoined_sorted_WII.dropna(subset=['region', 'Medal'])
print(dfjoined_sorted_cleaned1.info())


# Built-in Pause. Waiting for input to continue
print()
input("REMOVED NULL VALUES - Press Enter to continue...")
print()


# dfjoined_unique_regions = dfjoined.drop_duplicates(subset=["regions"])
print(dfjoined_sorted_cleaned1.nunique())


# Built-in Pause. Waiting for input to continue
print()
input("COUNT OF UNIQUE VALUES - Press Enter to continue...")
print()


# Print all unique regions
print("All UNIQUE REGIONS")
print(dfjoined_sorted_cleaned1.region.unique())
print()

# Print all unique Sport
print("All UNIQUE SPORTS")
print(dfjoined_sorted_cleaned1.Sport.unique())
print()

# Built-in Pause. Waiting for input to continue
input("LIST OF UNIQUE REGIONS AND SPORTS - Press Enter to continue...")
print()

# Print Head with old index
print("HEAD OF DATA FRAME OLD INDEX")
print(dfjoined_sorted_cleaned1.head())
print()


# Reindexing of data table
dfjoined_sorted_cleaned1.reset_index(drop=True, inplace=True)
print("HEAD OF DATA FRAME RESET INDEX")
print(dfjoined_sorted_cleaned1.head())
print()
print()
print("DATAFRAME TABLE NOW READY FROM MANIPULATION")
print()
print("NEXT STEP IS DATA VISUALISATION")

# Built-in Pause. Waiting for input to continue
print()
input("Press Enter to continue...")
print()


# Visualisation of Data using Seaborn and Matplotlib

# Import Matplotlib and Seaborn
import seaborn as sns
import matplotlib.pyplot as plt

# Change the context to "notebook"
sns.set_context("notebook")
# Set the figure theme to "darkgrid"
sns.set_theme(style="darkgrid")
# Plot a nested boxplot to show number of medals per age and per sex
sns.boxplot(x="Medal", y="Age",
            hue="Sex", palette=["m", "g"],
            data=dfjoined_sorted_cleaned1, showmeans=True, meanprops={"marker": "+",
                      "markeredgecolor": "black",
                       "markersize": "10"})
plt.title("Medals distribution by age and sex", size=16)
plt.savefig('figure0.png')

# Show plot
plt.show()


# Histagram plot of medals won by age
# Change the context to "notebook"
sns.set_context("notebook")
# Set the figure theme to "darkgrid"
sns.set_theme(style="darkgrid")
# Set a custom color palette
custom_palette = ['#b08d57', '#C0C0C0', '#FFD700']
sns.set_palette(custom_palette)
# plot graph
his = sns.histplot(dfjoined_sorted_cleaned1, x="Age", hue="Medal", multiple="stack", linewidth=0.1, binwidth=1)
# add overall title
his.set_title("Total Medals won by Age" , size=16)
plt.savefig('figure1.png')


# Bar plot - Number of total medals won by Sport all seasons
# Change the context to "notebook"
sns.set_context("notebook")
# Set the figure theme to "darkgrid"
sns.set_theme(style="darkgrid")
# Adjust to add subplots
g = sns.catplot(x='Sport', data=dfjoined_sorted_cleaned1, kind="count", aspect=2.5)
# Add x-axis and y-axis labels
g.set(xlabel="Year of the Olympic Games", ylabel="Total Medals won - combined")
# Rotate x-tick labels
plt.xticks(rotation=85)
# Set title to "Number of total medals won by Sport all seasons"
g.fig.suptitle("Number of total medals won by Sport all seasons", y=1.001, size=16)
plt.savefig('figure2.png')


# Bar plot - Number of total medals won by year between seasons
# Change the context to "notebook"
sns.set_context("notebook")
# Set the figure theme to "darkgrid"
sns.set_theme(style="darkgrid")
# Adjust to add subplots
c = sns.catplot(x='Year', data=dfjoined_sorted_cleaned1, kind="count", col="Season")
# Add x-axis and y-axis labels
c.set(xlabel="Year of the Olympic Games", ylabel="Total Medals won - combined")
# Rotate x-tick labels
plt.xticks(rotation=90)
# Set title to "Number of total medals won by year between seasons"
c.fig.suptitle("Number of total medals won by year between seasons", y=1.001, size=16)
plt.savefig('figure3.png')
