import streamlit as st
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt


###load the data

data = pd.read_csv(r"C:\Users\Sarah\Downloads\clean.csv")

### Setting the layout of the page
st.set_page_config(layout="wide")


#### Setting the colors of the matplotlib
plt.rcParams["text.color"] = "#e2c870"
plt.rcParams["axes.labelcolor"] = "#e2c870"
plt.rcParams["xtick.color"] = "#e2c870"
plt.rcParams["ytick.color"] = "#e2c870"
plt.rcParams["axes.facecolor"] = "#0e1117"
plt.rcParams["axes.edgecolor"] = "#e2c870"
plt.rcParams["patch.facecolor"] = "#0e1117"
plt.rcParams["figure.facecolor"] = "#0e1117"

### Title of the page
st.markdown(
	"<h1 style='text-align: center; color: #C0A824;'>HR Analytics</h1>",
	unsafe_allow_html=True,
)

## SECTION 1
st.markdown("## Type of company")

# filter the data for
clist = data["company_type"].unique()
st.sidebar.markdown("## Companies: ")
company_type = st.sidebar.selectbox("Select a type company: ", clist)
filter1 = data[data["company_type"] == company_type]

########## METRICS INDICATORS
m1, m2, m3, m4 = st.columns((1, 1, 1, 1))
mean_experience = round(filter1["experience"].mean(), 1)
mean_last_job = round(filter1["last_new_job"].mean(), 1)
mean_training_hours = round(filter1["training_hours"].mean(), 1)
candidate_count = filter1["enrollee_id"].count()
m1.metric(label="Number of candidates", value=candidate_count)
m2.metric(label="Average experience", value=str(float(mean_experience)) + " Years")
m3.metric(label="Time since last job", value=str(float(mean_last_job)) + " Years")
m4.metric(label="Average training", value=str(float(mean_training_hours)) + " Hours")

########## PIE CHART
st.write("Gender share")
# data to make garph
gender = pd.crosstab(
	filter1.gender, "gender", values=filter1.enrollee_id, aggfunc="count"
)
# chart
labels = filter1["gender"].unique()
colors = [
	"steelblue",
	"deepskyblue",
	"darkturquoise",
	"mediumaquamarine",
	"greenyellow",
	"yellowgreen",
	"darkolivegreen",
]
fig, ax1 = plt.subplots(figsize=(6, 4))
ax1.pie(
	gender["gender"],
	labels=labels,
	autopct="%1.1f%%",
	colors=colors,
	pctdistance=0.85,
	startangle=90,
	textprops={"fontsize": 15, "color": "#C0A824"},
)
# draw circle
fig.patch.set_facecolor("#0e1117")
centre_circle = plt.Circle((0, 0), 0.70, fc="#0e1117")
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
ax1.axis("equal")
plt.tight_layout()

# data to create table
comp_edu2 = pd.crosstab(filter1.company_size, filter1.education_level)

######## Layout of SECTION 1
# Pie chart
container1 = st.container()
col1, col2, col12 = st.columns([1, 3, 1])

with container1:
	with col2:
		fig
# Table
st.write("Company size and Education Level")
container6 = st.container()
col122 = st.columns([1, 3, 1])
with container1:
	with col2:
		comp_edu2


########### SECTION 2
###### Scatter plot? Education
st.sidebar.markdown("## Education ")
st.sidebar.markdown("#### Scatter plot: ")
st.markdown("## Education")

##### Layout of section2
container2 = st.container()
col3, col4 = container2.columns(2)
container8 = st.container()
col5, col6 = container8.columns(2)

education = data[
	(data["enrolled_university"] != "no_enrollment")
	& (data["enrolled_university"] != "Not_defined")
][["company_type", "enrolled_university", "training_hours"]]
column = education.columns.tolist()
x_axis = st.sidebar.selectbox("X-Axis", column)
y_axis = st.sidebar.selectbox("Y-Axis", column, index=1)
if x_axis and y_axis:
	scatter_fig = plt.figure(figsize=(6, 4))
	scatter_ax = scatter_fig.add_subplot(111)
	scatter_fig.patch.set_facecolor("#0e1117")
	education.plot.scatter(
		x=x_axis,
		y=y_axis,
		s=120,
		c="#76b5c5",
		alpha=0.6,
		ax=scatter_ax,
		title="{} vs {}".format(x_axis.capitalize(), y_axis.capitalize()),
	)
	plt.setp(scatter_ax.get_xticklabels(), rotation=45, ha="right")

with col3:
	scatter_fig


################# Histogram Logic ########################
##code to create df for this chart
x1 = data.loc[data.education_level == "Graduate", "experience"]
x2 = data.loc[data.education_level == "Masters", "experience"]
x3 = data.loc[data.education_level == "High School", "experience"]
x4 = data.loc[data.education_level == "Phd", "experience"]
x5 = data.loc[data.education_level == "Not_defined", "experience"]
x6 = data.loc[data.education_level == "Primary School", "experience"]

new = pd.DataFrame([x1, x2, x3, x4, x5, x6])
new = new.transpose()
new.columns = [
	"Graduate",
	"Masters",
	"High School",
	"PhD",
	"Not_defined",
	"Primary School",
]

# chart creation

st.sidebar.markdown("Histogram: Eductation vs. Experience: ")

hist_axis = st.sidebar.multiselect(
	label="Histogram Ingredient",
	options=new.columns.tolist(),
	default=["Graduate", "Masters"],
)
bins = st.sidebar.radio(label="Bins :", options=[5, 10, 15, 20])

if hist_axis:
	hist_fig = plt.figure(figsize=(6, 4))
	hist_fig.patch.set_facecolor("#0e1117")
	hist_ax = hist_fig.add_subplot(111)

	sub_new = new[hist_axis]

	sub_new.plot.hist(
		bins=bins,
		alpha=0.7,
		colormap="YlGnBu",
		ax=hist_ax,
		title="Distribution of experience",
	)
	hist_ax.set_xlabel("Years of experience")
else:
	hist_fig = plt.figure(figsize=(6, 4))
	hist_fig.patch.set_facecolor("#0e1117")
	hist_ax = hist_fig.add_subplot(111)
	sub_new = new[["Graduate", "Masters"]]

	sub_new.plot.hist(
		bins=bins,
		alpha=0.7,
		colormap="YlGnBu",
		ax=hist_ax,
		title="Distribution of experience",
	)

with col4:
	hist_fig

############### BAR 2
edu = pd.crosstab(data.major_discipline, data.last_new_job)
bar3_fig, ax = plt.subplots()
disc = col5.radio("Select Discipline", edu.index)
ax.bar(x=edu.columns, height=edu.loc[disc])
ax.set_xlabel("Number of years between jobs")
ax.set_ylabel("Number of people")
col6.pyplot(bar3_fig)

##### SECTION3
st.markdown("## Location")
############Slider for city development

city_dev = {
	"city_11": 0.55,
	"city_16": 0.91,
	"city_21": 0.624,
	"city_23": 0.899,
	"city_28": 0.939,
	"city_61": 0.913,
	"city_65": 0.802,
	"city_67": 0.855,
	"city_71": 0.884,
	"city_73": 0.754,
	"city_75": 0.939,
	"city_90": 0.698,
	"city_100": 0.887,
	"city_102": 0.804,
	"city_103": 0.92,
	"city_104": 0.924,
	"city_114": 0.926,
	"city_136": 0.897,
	"city_149": 0.689,
	"city_160": 0.92,
}

city_1, city_2 = st.select_slider(
	"Select 2 cities to see their development indexes",
	options=[
		"city_11",
		"city_16",
		"city_21",
		"city_23",
		"city_28",
		"city_61",
		"city_65",
		"city_67",
		"city_71",
		"city_73",
		"city_75",
		"city_90",
		"city_100",
		"city_102",
		"city_103",
		"city_104",
		"city_114",
		"city_136",
		"city_149",
		"city_160",
	],
	value=["city_11", "city_160"],
)
st.write("Index of first city is equal to:")
city_dev[city_1]
st.write("and the index of second city is: ")
city_dev[city_2]


########3bar chart
st.sidebar.markdown("## Location ")
st.sidebar.markdown(
	"#### Bar Chart | Number of employees in the city  : "
)  # Title on the side bar to choose values to comapre

cities = pd.crosstab(
	data.city, data.relevent_experience, margins=True, margins_name="All"
)
ct2 = cities.sort_values("All", ascending=False)[1:21]
ct2["Percentage with no experience"] = round(
	(
		ct2["No relevent experience"]
		/ (ct2["Has relevent experience"] + ct2["No relevent experience"])
	)
	* 100,
	1,
)
ct2 = ct2.transpose()


bar_axis = st.sidebar.multiselect(
	label="Number of employes in the city",
	options=ct2.columns.tolist(),
	default=["city_21", "city_103", "city_16", "city_114"],
)
# Creation of the bar plot
if bar_axis:
	bar_fig = plt.figure(figsize=(6, 4))
	bar_ax = bar_fig.add_subplot(111)
	sub_bar_cities = ct2[bar_axis].loc[
		[
			"Has relevent experience",
			"No relevent experience",
			"Percentage with no experience",
		]
	]

	sub_bar_cities.plot.bar(
		alpha=0.8, ax=bar_ax, colormap="YlGnBu", title="Number of employees in the city"
	)
	plt.setp(bar_ax.get_xticklabels(), rotation=45, ha="right")

else:
	bar_fig = plt.figure(figsize=(6, 4))
	bar_ax = bar_fig.add_subplot(111)
	sub_bar_cities = ct2[["city_21", "city_103", "city_16", "city_114"]].loc[
		[
			"Has relevent experience",
			"No relevent experience",
			"Percentage with no experience",
		]
	]

	sub_bar_cities.plot.bar(
		alpha=0.8, ax=bar_ax, colormap="YlGnBu", title="Number of employees in the city"
	)
	plt.setp(bar_ax.get_xticklabels(), rotation=45, ha="right")


#############LINE City
bins = [0, 0.25, 0.5, 0.75, 1]
data["dev"] = pd.cut(
	data["city_development_index"],
	bins=bins,
	labels=["0-0.25", "0.25-0.5", "0.5-0.75", "0.75-1"],
)
city_comp = pd.crosstab(data.dev, data.company_type)

line_axis = st.sidebar.multiselect(
	label="Type of company:",
	options=city_comp.columns.tolist(),
	default=["Early Stage Startup"],
)

# Creation of the bar plot
if line_axis:
	line_fig = plt.figure(figsize=(6, 4))
	line_ax = line_fig.add_subplot(111)
	sub_line_cities = city_comp[line_axis]
	sub_line_cities.plot.line(
		alpha=0.8,
		ax=line_ax,
		colormap="winter",
		title="Companies located in cities with development index:",
	)
	line_ax.set_xlabel('City development index group')
	line_ax.set_ylabel('Number of locations')

else:
	line_fig = plt.figure(figsize=(6, 4))
	line_ax = line_fig.add_subplot(111)
	sub_line_cities = ct2[["Early Stage Startup"]]
	sub_line_cities.plot.line(
		alpha=0.8,
		ax=line_ax,
		colormap="winter",
		title="Number of employees in the city",
	)
	line_ax.set_xlabel('City development index group')
	line_ax.set_ylabel('Number of locations')


# Layout of SECTION 3
container3 = st.container()
col7, col8 = st.columns(2)

with container3:
	with col7:
		bar_fig
	with col8:
		line_fig
