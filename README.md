<p align="center">
  <img width="560" height="300" src="https://user-images.githubusercontent.com/74840026/129602214-0df5cdab-9437-4abb-8943-95f61e3ef0ae.PNG">
</p>

# Surfs Up

# Overview of Analysis
Our dream is to open a surf shop that also serves ice cream on the beautiful island of Oahu.  We have developed a business case and pitched our idea to investors.  Catching the attention of one investor, W. Avy, we have our first meeting with him and it goes well.  His only concern was information regarding the weather.  He provides us with a weather data set and asks us to run some analysis on it and provide him some feedback.  We are presenting our weather analysis to him to show temperature trends during summer and winter months, specificaly June and December.  

# Results
The provided data set had temperature and precipitation measurements from 9 different stations from 2010 thru 2018.  We used Python and SQLite to analyze and filter it to show statistics for the months June and December during the timeframe.

## Temperature Statistics                
![June_temps](https://user-images.githubusercontent.com/74840026/129605186-d5ec6db7-81bf-4ebc-837b-69d3a93e06f0.PNG)                  ![Dec_temps](https://user-images.githubusercontent.com/74840026/129605195-45be52de-0e43-4fd1-b439-e2a95c567afb.PNG)
### 
- June avg temp - 74.9°F / December avg temp - 71.0°F
    - Similar averages indicate the temperatures in Oahu stay relativly steady in the 70's year round
- June min temp - 64.0°F / December min temp - 56.0°F
    - June's lows still provide good surfing and ice cream weather as December's lows could show lees opportunities for both surfing and ice cream
- June 75th percentile - 77°F / December 75th percentile - 74°F
    - Indicates 75% of the time the temperature is in the middle to upper 70's
# Summary
Additional analysis could help solidify the business case.
- Query to view percipitation statistics during June and December
    - This would show the relationship between temperatures and precipitation 
- Query to view average temperatures and percipitation levels at different stations
    - This could help narrow down the optimal location foe th shop
