# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
data = pd.read_csv(path)
data.rename(columns={'Total':'Total_Medals'},inplace=True)
data.head(10)


# --------------
data['Better_Event'] = np.where(data['Total_Summer']>data['Total_Winter'],'Summer','Winter')
data['Better_Event'] = np.where(data['Total_Summer'] ==data['Total_Winter'],'Both',data['Better_Event'])

better_event = data['Better_Event'].value_counts()
better_event = better_event.idxmax()


# --------------
#Code starts here

#Create a subset of the main dataframe with 4 relevant columns
top_countries = data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
top_countries.tail()

#Drop the last row from the dataframe having sum totals
top_countries.drop(top_countries.tail(1).index,inplace=True)
top_countries.tail()

#Create a function

def top_ten(df, col):
    top_10_summer = df.nlargest(10,col)
    country_list = list(top_10_summer['Country_Name'])
    return country_list

#Calling the function for Top 10 in Summer
top_10_summer = top_ten(top_countries, 'Total_Summer')
print ("Top_10_summer:\n",top_10_summer,"\n")

#Calling the function for Top 10 in Winter
top_10_winter = top_ten(top_countries, 'Total_Winter')
print ("Top_10_winter:\n",top_10_winter,"\n")

#Calling the function for Top 10 in both events
top_10 = top_ten(top_countries, 'Total_Medals')
print ("Top_10_summer:\n",top_10,"\n")

#Extracting common country names from all three lists
common=list(set(top_10_summer) & set(top_10_winter) & set(top_10))

print('Common Countries :\n', common, "\n")


# --------------
#Code starts here

summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]

#Subsetting the dataframe that contains only two columns (for x and y axis)
bar_summer_df = summer_df[['Country_Name','Total_Summer']]

#The below dataframe contains index, which has to be removed, else it appears in the bar plot
bar_summer_df

# reset index to 'Name'
bar_summer_df.set_index('Country_Name', inplace=True)

#WE PLOT THE SERIES

#Plotting the graph for Top 10 summer

#Create the figure
fig_bar = plt.figure(figsize=[14,8])

#Add the axis to the figure
axis_bar = fig_bar.add_axes([0,0,0.75,0.75])

# set the x-axis and y-axis labels
axis_bar.set_xlabel("Country Name")
axis_bar.set_ylabel("Total Medals won in Summer")

# title the plot
axis_bar.set_title("Distribution of Summer Medals among Countries")

# bar chart
bar_summer = bar_summer_df.plot(kind = 'bar', stacked=False, ax = axis_bar)



#Subsetting the dataframe that contains only two columns (for x and y axis)
bar_winter_df = winter_df[['Country_Name','Total_Winter']]

# reset index to 'Name'
bar_winter_df.set_index('Country_Name', inplace=True)

#WE PLOT THE SERIES

#Plotting the graph for Top 10 summer

#Create the figure
fig_bar_winter = plt.figure(figsize=[14,8])

#Add the axis to the figure
axis_bar_w = fig_bar_winter.add_axes([0,0,0.75,0.75])

# set the x-axis and y-axis labels
axis_bar_w.set_xlabel("Country Name")
axis_bar_w.set_ylabel("Total Medals won in Winter")

# title the plot
axis_bar_w.set_title("Distribution of Winter Medals among Countries")

# bar chart
bar_w = bar_winter_df.plot(kind = 'bar', stacked=False, ax = axis_bar)




#Subsetting the dataframe that contains only two columns (for x and y axis)
bar_df = top_df[['Country_Name','Total_Medals']]

# reset index to 'Name'
bar_df.set_index('Country_Name', inplace=True)

#WE PLOT THE SERIES

#Plotting the graph for Top 10 summer

#Create the figure
fig_bar_10 = plt.figure(figsize=[14,8])

#Add the axis to the figure
axis_bar_10 = fig_bar_10.add_axes([0,0,0.75,0.75])

# set the x-axis and y-axis labels
axis_bar_10.set_xlabel("Country Name")
axis_bar_10.set_ylabel("Total Medals won in top 10")

# title the plot
axis_bar_10.set_title("Distribution of top 10 among Countries")

# bar chart
bar_10 = bar_df.plot(kind = 'bar', stacked=False, ax = axis_bar)


# --------------



summer_df['Golden_Ratio']=summer_df['Gold_Summer']/summer_df['Total_Summer']

summer_max_ratio=max(summer_df['Golden_Ratio'])

summer_country_gold=summer_df.loc[summer_df['Golden_Ratio'].idxmax(),'Country_Name']

winter_df['Golden_Ratio']=winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio=max(winter_df['Golden_Ratio'])
winter_country_gold=winter_df.loc[winter_df['Golden_Ratio'].idxmax(),'Country_Name']

top_df['Golden_Ratio']=top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio=max(top_df['Golden_Ratio'])
top_country_gold=top_df.loc[top_df['Golden_Ratio'].idxmax(),'Country_Name']





# --------------
#Code starts here
#Drop the last row
data_1 = data.drop(data.tail(1).index)
#or data_1=data[:-1]
data_1.tail()


#Calculate weighted average such that where each gold medal= 3 points, silver = 2 points, bronze = 1 point
data_1['Total_Points']= data_1['Gold_Total']*3 + data_1['Silver_Total']*2 + data_1['Bronze_Total']*1
# Use of position index to handle the ambiguity of having same name columns

#Finding the maximum value of 'Total_Points' column
most_points=max(data_1['Total_Points'])

#Finding the country associated with the max value of 'Total_Column' column
best_country=data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']
print('The maximum points achieved is ', most_points, ' by ', best_country )

#Code ends here


# --------------
#Code starts here

#Create a single row dataframe by subsetting the best performing country from previous question
best = data[data['Country_Name'] == best_country]
best

#Subset 'best' further to include only 4 columns
best = best[['Gold_Total','Silver_Total','Bronze_Total']]
best

#Create stacked plot
#Create the blank canvas
fig = plt.figure()

#Add the axes
ax = fig.add_axes([0,0,1,1])

#Name the axes and give title
ax.set_title("Distribution of Best Country medals")
ax.set_xlabel("United States")
ax.set_ylabel('Medals Tally')

#Plot the graph
best.plot(kind='bar', stacked=True, figsize=(14,8), ax=ax)

#Rotate the x-axis labels
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')

#Display the graph
plt.show()



