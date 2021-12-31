<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Data Cleaning | Shore Pollution
*[Radoslaw Debek]*

*[Data Analytics, Paris & 17.12.2021]*

## Content
- [Data Cleaning | Shore Pollution](#data-cleaning--shore-pollution)
	- [Content](#content)
	- [Project Description](#project-description)
	- [Workflow/Organisation](#workfloworganisation)
	- [Challenges](#challenges)
	- [Results](#results)
	- [Links](#links)

## Project Description
The project was to preapre a given dataset for analysis via following data papeline and data cleaning.
The dataset which was analysed presented the shore pollution on the cost of Australia (Queensland) i.e. accidents registered between years 2002 and 2020.

![Queensland_map](https://media.australias.guide/file/sitemedia/wp-content/uploads/sites/5/qld-regions2.jpg)

## Workflow/Organisation
The organisation of the project was done using Trello (the link to the workspace is presented below as well as the workflow chart).
The project was  realized and followed subseuent steps:

1. Importing given data set to Pandas.
The data set was given in 5 different files and with diffrent fromats (.csv and .xls) with diffrent column names etc.
2. Looking and describing the Data.
The data was presented in 8 columns: Date (diffrent formating), Region (should contain only 5 unique values), Source (should contain only 3 unique values), Ship Type (should contain only 3 unique values), Area (should conatin only 2 unique values), Location, Pollutant, Estimated Litres (should be a number, but was a sting with variuos content).
The data with the exceptopn of 'Date' column was categorical.
3. Data Cleaning

	3.1. Drop columns

    I decided to drop 2 columns i.e. Location and Ship Type, because:
    - Location: this column presents values unique for each accident and can be replaced (in a more general manner) by the Region and Area columns.
    - Ship Type: The column Source already shows if the origin of a pollution was a ship. At the same time this is the column with the most missing values. Therefore,I decided to drop it.

	3.2. Date format

    The column 'Date' had diffrent formatiing in the files, thus it was necessary to unify that. There were present also some typos like 219 instead of 2019. There were 2 rows like that and they were dropped.

      3.3. Missing values

    The missing values were presented in three columns: Source (7), Pollutant (2) and Estimated Litres (21).
    - Source: I replaced missing values with 'Unknown' as it can be coming only from Land, Ship r Unknown SOurce
    - Pollutant: There were only 2 values missing, so I droped these 2 rows.
    - Estimated Litres: I also decided to drop these rows as there was only 21 of them.

    3.4. Cleaning the text

    Firstly I wrote a function that would remove spaces at the begining and end of the string and will unify the text in terms of case size.
    Then I went through every column.
    - Region: This column should contain only 5 unique values, but it contained 14. There were some typos as well as smetimes insted of a Regions name, port name was gived. I created a dictionary which allowd to assign incorrect values to the correct region names.
    - Source: This column should conatin inly valyes: Land, Ship or Unknown. I used similar procedure (dictonary) to assign correct values.
    - Area: This column should contain only 2 values. The same procedure was assigned as for Region and Source column.
    - Pollutant: This column should specify which pollutant was released to the environment. I used regex in order to find in the strings some patterns and then convert these values to a unify system. I used the mst popular ones, and for the rest I changed the values to 'Other'. Finally I finished with a column which showed 11 unique values.
    - Estimmated Littres: This colum  should conatiun a number insted of there was a lot of text or incorrect values. In order to change it I wrote a function which:
            - converted unknown to 0.
            - removed all the letters and the special characters from the strings
            - if there was incorect unit m, g or kg then these values were converted to 0.
            - if the range was given, the mean value was calculated
            - Finally, when there were only numbers left. All of the values were converted to floats.

	3.5. Removing duplicates

     Two rows like that were found

	3.6. Outliers
	
     I created a plots which showed for every column if there were any outliers.
4. Encoding non numerical data
After data cleaning the non numericla data were presented in columns: Region, Source, Area, Pollutant. Since all of these data were not ordinal I could use dummy encoder (One Hot Encoding) in order to encode these columns.
5. Saving clean data to csv file
6. Connecting to MySQL and exporting the dataframes
7. Writing three queries to show that the data can be clearly analysed.
8. Preparing readme file and the presentation.


## Challenges
1. Working alone. Brainstorming ideas is much easier in a team as well as dividing the tasks.
2. Data cleaning. The data needed much cleaning (typos, wrong names, wrong column names, wrong values, missing values etc.)

## Results
Ther result of the project are presented in:
- readme.md file | Description of the project and the prcoess.
- jupyter notebook | Code which was used to clean the data with comments.
- SQL script | Queries used to analyse the data.
- csv file | Clean data
- ppt presentation | Presentation of the project

## Links

[Repository](https://github.com/radek-deb/Projects/tree/main/Project3_Data_Cleaning)  
[Slides](https://docs.google.com/presentation/d/1QL0klNy47-UhiYv4tQwaom0f-TvZ5F_x/edit?usp=sharing&ouid=102785489791173764779&rtpof=true&sd=true)  
[Trello](https://trello.com/b/KCDt4Wui/shore-pollution)  
