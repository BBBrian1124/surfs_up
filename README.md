# surfs_up
Module 9 - SQLite and SQLAlchemy - UofT Data Analytics Boot Camp

# Overview of the analysis: 
* W. Avy plans on opening up an ice cream and surf shop, but he wants more information about temperature trends before opening the shop. Specifically, he wants temperature data for the months of June and December in Oahu in order to determine if the surf and ice cream shop business is sustainable year-round. We have been provided a SQLite database which contains the weather info over multiple years for Oahu which we will use to query to find information for our analysis.

# Results: 
![Month_comparions] https://github.com/BBBrian1124/surfs_up/blob/main/Challenge/Resouces/Month_comparison.png
* The summary statistics in both months show that at least 75% of the data (temperatures) fall within 1 standard deviation of the mean. This suggests that the temperatures do not vary much within each of the months. If temperature is a driving selling factor, this should be a good sign as it means one of the selling factors are fairly consistent.
* The mean and the median in both months are also extremely close, meaning the data has a symmetrical distribution of data. This also suggests that the temperatures do not vary much within each of the months. This may be useful for forecasting and predictions as it suggests that year to year, the temperature in each month remains fairly consistent. 
* In comparing the two months, we see that the 3rd quartile for December is a temperature of 74 where as the 1st and 2nd quartile for June are 73 and 75 respectively. If we are assuming that the higher the temperature, the higher the ice cream sales, this can have implications on expected sales. For example, if we assumed that 75 was the lowest (or optimal) temperature people are willing to buy ice cream, it would mean 75% of the dataset in December is excluded whereas only 50% of the dataset in June is excluded. We can think of this similar to a "slider" where the lower the "optimal" temperature is, the less of December’s dataset it will cover, in other words, the less likely there will be sales in that month.

# Summary:
* The summary statistics show that the temperature data is consistent as at least 75% of the data falls within one standard deviation in both months, and the mean and median are very similar. This suggests that it is not prone to varying much from the mean which is a good sign as a selling factor (temperature) for ice cream is consistent and suggests that we can rely on this data for forecasting.
* We can preform additional queries to gather more information. I have written a query that will take the user's input to specify the min or optimal temperature and will return a visualization of the frequency distribution/counts based on that filtered dataset. The idea being that temperature has an impact on sales and that there may be a minimum or optimal temperature in order for customers to want to buy ice cream (i.e. if it is too cold they are unlikely to buy). This will allow us to quickly visualize how many instances or how likely we are going to be able to make sales in that month based on our "optimal" temperature.

![Min Temp Set as 56] https://github.com/BBBrian1124/surfs_up/blob/main/Challenge/Resouces/Min%3D56.png
* For the first query we can run, I will set the min temperature to 56 which is the minimum of the 2 datasets so we can visualize the spread of the frequency of the temperature. This will allow for a quick glance at how often we expect certain temperature or temperature ranges to be reached to see if this business venture is worth it.

! [Min Temp Set as 74] https://github.com/BBBrian1124/surfs_up/blob/main/Challenge/Resouces/Min%3D74.png
* The second query will be ran using 74 as the minimum temperature to visualize my last point in the results section that if the min or optimal temperature was 74, we'd be much less likely to be able to sell in December. We can adjust as needed based on what we discover to be the optimal tempature.

# Appendix:
[Repository Link] https://github.com/BBBrian1124/surfs_up/tree/main/Challenge
[Python Code File] https://github.com/BBBrian1124/surfs_up/blob/main/Challenge/SurfsUp_Challenge.ipynb
