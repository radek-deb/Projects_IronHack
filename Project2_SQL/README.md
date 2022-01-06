<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Sustainable Development


*[MTIMET Abdelaziz,Nesma Dehili,Radek Debek   IronHack Paris 10/12/2021]*

## Content
- [Project Description](#project-description)
- [Methodology](#Methodology )
- [Workflow](#Workflow)
- [Organization](#organization)
- [Links](#links)

## Project Description
We speak about Sustainable Development and the differents effort and ways countries can contribute in making our world a better one. In this project we develop and analyze data to compare countries contribution. 

## Methodology
Score out of 10: 
If country signed Kyoto protocol 1 point

from normalized co2 emissions (betwwen 0-1 closer to zero the better):
if co2 emissions below 0.25 --> 3 points
if co2 emissions between 0.25-0.5 -> 2 points
if co2 emissions between 0.5-0.75 -> 1 point
and above 0.75 -> 0 points

from normalized energy consumption per capita (between 0-1 the lower the better):
if energy consumption < 0.25 -> 3 points
if energy consumption between 0.25-0.5 - > 2 points,
if energy consumption between 0.5-0.75 -> 1 point
above 0.75 -> 0 points

for number of projects :
if 0 projects -> 0 points
if between 1-5 projects -> 1 point
if between 5-10 projects -> 2 points
if above 10 projects -> 3 points

SO the total of these 4 parameters is max 10 points

The higher the ranking the better

## Workflow
- Subjuct 
- Data scraping 
- Data cleaning 
- Data normalization 
- Score computation

## Organization
We used Jira to divide the work and organize it as the following: 
- Choosing subject -- Sustainable Development
- Checking data (write the python code to extract data( web scraping, exporting csv file from word)
- Develop ER (Entity relational models): Entity, attribute, PK, FK, relation between each entity(1-1, 1-many, m-m)
- Data description : clean data after extracting from the source, definition of the data.
- SQL script (create database,create table and fiding it with data.)
- Missing data ⇒ python or SQL
- Normalization: use (Xi-Xmin)/(Xmax-Xmin)
- Composite indicator calculation: variable x weight(influence)
- Visiualization (slides, and test with mysql)

## Links
Include links to your repository, slides and kanban board. Feel free to include any other links associated with your project.

[Repository](https://github.com/abdelaziz1990/Project-)  
[Slides](https://github.com/abdelaziz1990/Project-/blob/main/Sustainable%20Development.%20Project%20pdf.pdf)  
 
