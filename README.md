
# Surfs Up Analysis
Module 9 - Advanced Data Storage and Retrieval

# Overview of Analysis
The objective of this project is to create an analysis to acquire investors to invest in a new surf shop in Oahu, Hawaii. The analysis involved performing a weather analysis of to determine the temperature statistics for June and December in order to determine the sustainability of operating a surf shop year round. 

The project utilized SQLite, SQLAlchemy, and Flask to query, analyze and visualize climate data to build the business case. As part of this analysis, weather precipitation statistics such as minimum, maximum, and average temperatures in June and December and weather stations were analyzed. Flask was used to design and build a climate web application to display the information. The temperature data was converted into a Pandas DataFrame and weather statistics were gathered.

The project utilized SQLite, SQLAlchemy, and Flask to query, analyze and visualize climate data to build the business case. As part of this analysis, weather precipitation statistics such as minimum, maximum, and average temperatures in June and December and weather stations were analyzed. Flask was used to design and build a climate web application to display the information. The temperature data was converted into a Pandas DataFrame and weather statistics were gathered.


# Results
High level summary of the results and two additional queries to gather additional weather data for June and Dec

1) In June, we had a max count of 1700, a minimum temperature of 64, maximimum temperature of 85, and an average temperature of 74.9.

![image](https://user-images.githubusercontent.com/80140082/118376414-9f699100-b57c-11eb-9c36-80a1e1b4f049.png)

2) In December, we had a max count of 1517, a minimum temperature of 56, maximimum temperature of 83, and an average temperature of 71.0.

![image](https://user-images.githubusercontent.com/80140082/118376399-94aefc00-b57c-11eb-9dbb-ce9a9ebcda7c.png)

3) The standard deviation was 3.25 and and 3.75 (rounded up) for June and December, respectively. Also, the mean temperature for June (74.9) is slightly higher than December (74.01)


# Summary
In comparison, for the most active weather station, we had a count of 2772 with:

* minimum temperature of 54.0, maximum temperature of 85.0, and an average temperature of 71.6 for June
* minimum temperature of 58.0, maximum temperature of 79.0, and an average temperature of 69.9 for December


![image](https://user-images.githubusercontent.com/80140082/118379436-29225a00-b58f-11eb-98ee-53cd0add8aa7.png)


![image](https://user-images.githubusercontent.com/80140082/118379437-32abc200-b58f-11eb-8b1d-6ccd4dfad691.png)


* For the most active station, we have a minimum temperature of 65, maximum temperature of 82, and average temperature of 73.7 (rounded up) for June.

![image](https://user-images.githubusercontent.com/80140082/118379389-d34db200-b58e-11eb-86a7-9d48e84740c5.png)

*  For the most active station, we have a minimum temperature of 58, maximum temperature of 79, and average temperature of 69.9 for December.

![image](https://user-images.githubusercontent.com/80140082/118379393-dcd71a00-b58e-11eb-944e-87b755813e6e.png)




