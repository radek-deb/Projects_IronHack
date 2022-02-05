import streamlit as st
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go


from streamlit_folium import folium_static
import folium


#### Setting the colors of the matplotlib
plt.rcParams["text.color"] = "#FFFFFF"
plt.rcParams["axes.labelcolor"] = "#FFFFFF"
plt.rcParams["xtick.color"] = "#FFFFFF"
plt.rcParams["ytick.color"] = "#FFFFFF"
plt.rcParams["axes.facecolor"] = "#000000"
plt.rcParams["axes.edgecolor"] = "#FFFFFF"
plt.rcParams["patch.facecolor"] = "#000000"
plt.rcParams["figure.facecolor"] = "#000000"



###load the data

data_sample = pd.read_csv(r"C:\Users\radek\IronHack\IronRadek\Week8\Project_8\data\data_sample_labeled.csv")

### Setting the layout of the page
st.set_page_config(layout="wide")


### Title of the page
st.markdown(
	"<h1 style='text-align: center; color: #ffffff;'>UBER rides in May 2014</h1>",
	unsafe_allow_html=True,
)
day = st.select_slider('Pick day of the week', options=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Saturday', 'Sunday'])
hour = st.select_slider('Pick an hour',[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23])




#Operation on data to be plotted
#Operations for other charts
data_sample['Date/Time'] =pd.to_datetime(data_sample['Date/Time'])
data_sample['hour'] =data_sample['Date/Time'].dt.hour
data_sample['day_of_week'] =data_sample['Date/Time'].dt.day_name()
data_sample['day_Week_num'] = data_sample['Date/Time'].dt.dayofweek
data_sample['week'] = data_sample['Date/Time'].dt.week
data_sample['time_of_day']= pd.cut(data_sample['hour'], bins=[-1,6,10,14,18,24], labels=['night','morning', 'noon', 'afternoon', 'evening'])

data_map = data_sample.loc[(data_sample['hour']==hour) & (data_sample['day_of_week']==day)]
data_map_list_cluster1 = data_map[['Lat','Lon']][data_map['labels_kmeans']==0].values.tolist()
data_map_list_cluster2 = data_map[['Lat','Lon']][data_map['labels_kmeans']==1].values.tolist()
data_map_list_cluster3 = data_map[['Lat','Lon']][data_map['labels_kmeans']==2].values.tolist()
data_map_list_cluster4 = data_map[['Lat','Lon']][data_map['labels_kmeans']==3].values.tolist()
data_map_list_cluster5 = data_map[['Lat','Lon']][data_map['labels_kmeans']==4].values.tolist()
size_map_list_1 = len(data_map_list_cluster1)
size_map_list_2 = len(data_map_list_cluster2)
size_map_list_3 = len(data_map_list_cluster3)
size_map_list_4 = len(data_map_list_cluster4)
size_map_list_5 = len(data_map_list_cluster5)



# Plotting a map with lcoations
m_p= folium.Map(location=[40.7128, -74.0060], zoom_start=10,tiles = "Stamen Toner")

#first cluster
for point in range(0,size_map_list_1):
	folium.CircleMarker(data_map_list_cluster1[point], radius=2,color='blue',fill_color='lightblue',).add_to(m_p)

#second claster
for point in range(0,size_map_list_2):
	folium.CircleMarker(data_map_list_cluster2[point], radius=2,color='green',fill_color='lightgreen',).add_to(m_p)

#third claster
for point in range(0,size_map_list_3):
	folium.CircleMarker(data_map_list_cluster3[point], radius=2,color='purple',fill_color='purple',).add_to(m_p)

#fourth claster
for point in range(0,size_map_list_4):
	folium.CircleMarker(data_map_list_cluster4[point], radius=2,color='orange',fill_color='orange',).add_to(m_p)

#fifth claster
for point in range(0,size_map_list_5):
	folium.CircleMarker(data_map_list_cluster5[point], radius=2,color='red',fill_color='red',).add_to(m_p)

##########Graphs
### Rides per day and hour
#Operation on data
data = pd.read_csv(r'C:\Users\radek\IronHack\IronRadek\Week8\Project_8\data\uber-raw-data-may14.csv')
data['Date/Time'] =pd.to_datetime(data['Date/Time'])
data['hour'] =data['Date/Time'].dt.hour
data['day_of_week'] =data['Date/Time'].dt.day_name()
#Column with the number of a day
data['day_Week_num'] = data['Date/Time'].dt.dayofweek
#Adding a column with the number of a week in a year
data['week'] = data['Date/Time'].dt.week
data['date']= data['Date/Time'].dt.date


#Bar chart
data_hour = data.loc[(data['hour']==hour)]
fig_bar = px.histogram(data_hour, x= data_hour['day_of_week'], color='day_of_week',color_discrete_sequence=px.colors.sequential.RdBu_r,
title="Total number of rides per day and hour",
labels=dict(day_of_week="Day of week", count="Count"))


#### Pie chart
data_time = data_sample.groupby('time_of_day')['week'].agg('count')
data_time = pd.DataFrame(data_time)

fig_pie = px.pie(data_frame=data_time, values="week", names=data_time.index,color_discrete_sequence=px.colors.sequential.RdBu_r, title='Number of rides per time of the day')


### line chart
#operation on data
ride = data_sample.groupby(['week','hour','day_of_week', 'day_Week_num'])['Base'].count()
ride = ride.reset_index()
ride = ride.rename(columns = {'Base':'Ride'})
ride.sort_values('Ride')
avg_wk = ride.groupby(['day_of_week','hour'])['Ride'].agg('mean')
avg_wk = pd.DataFrame(avg_wk)
avg_wk = avg_wk.reset_index()


#chart
fig_line = px.line(avg_wk, x="hour", y="Ride", color='day_of_week', markers=True, color_discrete_sequence=px.colors.sequential.RdBu_r, title='Average number of rides per day and hour',
labels=dict(day_of_week="Day of week", Ride="Averge number of rides", hour='Hour, h'))

#Metrics

n_rides= data['hour'].count()
rides_per_day = data.groupby('date')['hour'].agg('count')
av_rides_per_day = int(np.mean(rides_per_day))


fig_metrics = go.Figure()

fig_metrics.add_trace(go.Indicator(
    mode = "number",
    value = n_rides,
	title = {'text': "Total number of rides"},
    domain = {'row': 0, 'column': 1}))
fig_metrics.add_trace(go.Indicator(
    mode = "number",
    value = av_rides_per_day,
	title = {'text': 'Average number of rides per day'},
    domain = {'row': 1, 'column': 1}))
fig_metrics.update_layout(
    grid = {'rows': 2, 'columns': 1, 'pattern': "independent"},
    template = {'data' : {'indicator': [{
        'mode' : "number",
        }]
                         }})

#Layout of the page
container1 = st.container()
col1, col2 = st.columns([1, 1])

with container1:
	with col1:
		fig_metrics
	with col2:
		fig_pie

container12 = st.container()
with container12:
	st.write(f'You selected {day} and hour {hour}')




container2 = st.container()
col3, col4, col5 = st.columns([1, 3, 1])
with container1:
	with col4:
		folium_static(m_p)

container3 = st.container()
col6, col7, = st.columns([1, 1])

with container3:
	with col6:
		fig_line
	with col7:
		fig_bar
