<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Project week 6 | Descriptive, predictive analysis and visualization in Tableaue
*[Sandrine Prevot, Radoslaw Debek]*

*[Data Analytics, Paris & 21.01.2022]*

## Content
- [](#)
- [Money Transfers - PayLocator](#payLocator)
	- [Content](#content)
	- [Project Description](#project-description)
	- [Requirements](#requirements)
	- [Workflow](#workflow)
	- [Dashboard/Widgets Description](#widgets)
	- [Links](#links)

## Project Description
The aim of this project is to prapre an informative Dashboard in Tableau. The dashboard whould reflect the descriptive and predictive analysis of the dataset on money transfers between diffrect banks.

## Requirements

- Dashboard should be interactive
- Dashboard should be constantly upadted (connected to Tableau by Gogglesheets)
- The work should be planned and realized using Trello
- Dashboard should have at least 12 widgets which describe KPIs
- Each widget should be described in Trello frol the user story perspective
- Dashboard should show:
      - Average time of transactio
      - Status of payment
      - Total charges per period
      - Payment status forecast
      - Issues in correspondance chain
      - Probability of delay
      - Troubles forecast
- Dashoboar dshould give the possibility to filter the data
- 3 widgets should reflect forecasted values
- Dashboards should be created using corporate colors.
- Dashboard should contain logo and the SWIFT Compability Label

## Workflow
The whole work in the project was organised using Trello platform. The main steps of the projest are presented below:

1. Brainstorming ideas.
2. Getting to know the data.
3. Connecting dataset to Tableau.
4. Analysis of Data.
5. Calaculation of parpametrs to be presented on the Dashboard.
6. Upadting the data.
7. Creation of charts (bar charts and forecast charts).
8. Creating Dashboard.
9. Preparing deliverables (readme file, Git-Hub repository, presenation)

## Dashboard/Widget Description

We created a dashboard form a perspective of a person who tracks the transactions, so it is either a bank worker or a person who is intrested in bank money crossboarder transfers as it is important for their business; For that we developed 12 wigdets, including 8 numbers and 4 charts, which are interactive and there is a possibility to fileter the data. The description of each widget (also form the user story) is presented below. The link to the Dashboard, slides, Git-Hub repo and Trello can be found at the bottom of the page.

### Widget 1: AVERAGE TRANSACTION TIME |

Average time of transaction was caluclated first in Gogglesheets (using Query) and then in Tableau.
The claculations were performed for each transation.
This parameter is important as it directly shows how much time on average it takes for a transaction to be finished.

**User story:**

As a bank customer I want to transfer money between diffrent accounts so I need to know the average time of transcation so I can plan my other business activities and pedpendeces from my clients.

### Widget 2: STATUS OF TRANSACTION |

We created a chartbar which shows all stages for all transactions registred in the dataset. In order to go that the trancactions had to be identiifed (unique ID number) as well as each stage of the transaction had to be identified and appropritly orderd in time. These actions were done in Googlesheets.
Grph shows all stages of each transaction. It is informative as we can observed what were the stages of each transaction. It also tells if the problems with transaction were sucessfully solved i.e.: change of status from pending to completed.

**User story:**

As a bank surpervisor I can check what is the status of diffrent transactions so I easly see which transaction are still pending, which are completed etc.

### WIDGET 3: MAXIMUM TRANSACTION TIME |

The maximum transaction time is an important parameter as it alows to check how much it differs from the average and also if this parameter increases it is alarming signal.

**User story:**

As a bank worker I need to monitor time of transaction and if the transaction takes too much time I can act on it and make the money transfer if there are any problems.

### WIDGET 4: AVERAGE CHARGES PERCENTAGE |

In order ot calculate the charges for each transaction we had to identify eeach step of transaction and charges associated with that step. Then we also had to take into account the fact that the transactions were done in 2 currencies. In order to get the appropriate values we created a sperate sheet in googlesheet document which is connected to the current exchange rate between dollars and euros. The calaculations were performed in the Excel file. The final charge for each transaction was calaculated as a sum of charges for each transaction step. In order to avoid any mistake, all of the charges 5from different stages of the transaction) were converted into USD.

This parameter is important as it gives information about avearge cost associated with money transfer.

**User story:**

As a potential bank customer/bank worker I need to know what are the average charges of the money transfer so I can plan the coststs of bank/company.

### WIDGET 5: PAYMENT STATUS - PROBABILITY OF PENDING |

This paramater was calaculated in Tableau, using formula below:
```Tableau
count(If [Status]="PENDING" then [ID] END)/count(If [Status]="NEW" then [ID] END)
```

Probaility of pending tells if it is probable that there will be problems with our transaction. It was calaculated as all of the transactions with status pending divided by the number of all transactions.

**User story:**

As a bank customer I need to plan my business actions so it is important for me to know what is probability that my transaction will be pending.

### WIDGET 6: PAYMENT STATUS - PROBABILITY OF COMPLETED |

This paramater was calaculated in Tableau, using formula below:
```Tableau
count(If [Status]="COMPLETED" then [ID] END)/count(If [Status]="NEW" then [ID] END)
```

Probaility of complited tells if it is probable that the transaction will be sucessfull. It was calaculated as all of the transactions with status complited divided by the number of all transactions.

**User story:**

As a bank worker I need to know what is the probability (percentage of completed transactions) so I can act if these number is too low I can check what are the issues with delayed transactions

### WIDGET 7: PROBABILITY OF CANCELED |

This paramater was calaculated in Tableau, using formula below:
```Tableau
count(If [Status]="CANCELLED" then [ID] END)/count(If [Status]="NEW" then [ID] END)
```

Probaility of cancelled tells if it is probable that there will be problems with our transaction. It was calaculated as all of the transactions with status cancelled divided by the number of all transactions.

**User story:**

As a bank worker I want to know how many transactions were cancelled so I can act on it and find out why they were cancelled.

### WIDGET 8: PROBABILITY OF DELAY |

This paramater was calaculated in Tableau, using formula below:
```Tableau
count(If [Time transaction]> 24 then [Time transaction] END)/count([Time transaction])
```

We considered that the status of delayed transaction will be given to the transactions that took more than 24h. This parameter is important as it indicates how probable is that the money will be transfered in more than 24h. This is very important information from the business perspective.

**User story:**
As a bank customer it is important for me that the transactions are done fast so I need to know what is the probability that my transaction will take more than 24 hours.

### WIDGET 9: PROBABILITY OF DELIVERED |

This paramater was calaculated in Tableau, using formula below:
```Tableau
count(If [Status]="DELIVERED" then [ID] END)/count(If [Status]="NEW" then [ID] END)
```

Probaility of delivered tells if it is probable that there will be problems with our transaction. It was calaculated as all of the transactions with status delivered divided by the number of all transactions.

**User story:**
As a bank worker I want to know if transactions were delivered and not completed this allows me to take decisions and make the system more efficient in the future.

### WIDGET 10 ISSUES IN CORRESPONDENCE - MAP WITH COUNTRIES WHICH SHOWS NUMBER OF DELAYS |

It is importat to locate the countries in which are located banks that are causing the most problems with transactions. We can observe that on the interactive map, which shows the count of transaction with specific status in their location. The map can be filtered and thus we can observe which country had the most transactions with the status pending. The information about the coutry was ectracted from the bankcode in Gogglesheets.

**User story:**

As a bank worker I need to know through which countries send money in order to make the transactions fast. If there are countries in which banks are causing the delays too often I will see it on the map.

### WIDGET 11: FORECAST OF AVERAGE TIME OF TRANSACTION, AVERAGE CHARGES AND AVERAGE AMOUNT TRANSFERRED |

It is important to be able to predict the behaviours in the coming months. We decided that there are three parameters which are important from the business perspective: average time of transaction, average charges associated with transaction, and avrergae amounts transfered. They were presenetd as a monthly average for the observed period on the line chart. It is possible to filter the chart in order to observe data only for the desired period/month. Based on these observations forecast is shown on the graph with corresponding confidence intervals and average valeus of time of transaction, charges associated with transaction, and amounts transfered for the upcoming moths.

**User story:**

As a bank worker I need to know the forecast associated with charges total amounts of money transfer and time of transactions so I can prepare the future actions and make the money transfers more efficient.

### WIDGET 12 AVERAGE TIME OF TRANSACTION ASSOCIATED WITH BANKS:

We decided that it is important to see average time of transaction associated iwth diffrent banks. We showed it on the bar chart, which is also interactive and there is a possibility of filter trough diffrent stages of transaction. Thus we can observe not only the avreage time of transaction, but also how long each stage of transaction lasted.

**User story:**

As a bank customer I want to know which banks are causing delays in the money transfer so in the future I can avoid them while choosing ways to transfer money.


## Links

[Dashboard](https://public.tableau.com/app/profile/radek7851/viz/Project6_16429472543890/Dashboard1?publish=yes)
[Data_in_Googlesheets](https://docs.google.com/spreadsheets/d/1IGpgipGi_JbL6SQ2Un56PJ5iDwxgpUXv/edit?usp=sharing&ouid=102785489791173764779&rtpof=true&sd=true)
[Repository](https://github.com/radek-deb/Project1-MasterMind-Game)
[Slides](https://docs.google.com/presentation/d/1QL0klNy47-UhiYv4tQwaom0f-TvZ5F_x/edit?usp=sharing&ouid=102785489791173764779&rtpof=true&sd=true)
[Trello](https://trello.com/b/NiaCEmTf/projectweek6-sandrine-radek)
