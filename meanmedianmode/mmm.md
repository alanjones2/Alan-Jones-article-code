### Statistics 101

## Mean, Median and Mode: What Are they and When Should You Use Them

### You probably remember Mean, Median and Mode from high school stats classes but they are often used wrongly. We look at how you _should_ use them with Python Pandas examples.

What is the average height of an 18-year-old American male? Or the average price of a house in Madrid? Or the average grade achieved by high school students in England?

These are all perfectly worded questions but mean something slightly different in each case. The average in the first case is calculated using the _mean_, the house prices would be better represented using the _median_ and the school grades by the _mode_.

The average is a measurement of a central tendency and typically we would expect that it would be calculated by adding a set of values  together and then dividing by the number of values. 

This is the _mean_ and this works perfectly well for a normally distributed set of data like height.
The _median_ is the central value meaning that there are an equal number of measurements either side of this value.
Whereas the _mode_ is the most frequent value in a set.

You can legitimately track the height of adult Americans by adding all of their height together and divided by the number of Americans. (That's quite a task so you'd probably want to take a representative sample instead.)

And if you tracked this over time you'd get a graph like the one below from Our World in Data.


![Change in height](https://github.com/alanjones2/Alan-Jones-article-code/raw/master/meanmedianmode/images/changeinheight.png)




This works fine because height follows a normal distribution as illustrated here:

![Height distribution](https://github.com/alanjones2/Alan-Jones-article-code/raw/master/meanmedianmode/images/heightnormaldist.jpg)

Licensed by [Illustrative Mathematics](https://illustrativemathematics.org/) under a
Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International 

In a normal distribution values are distributed evenly around a central point and tail off similarly to the left and right. You can see the mean in the graph above is 70 inches.

![Levante players](https://github.com/alanjones2/Alan-Jones-article-code/raw/master/meanmedianmode/images/levante10.png)

In a normal distribution the mean and the median are the same value but that is not true for other types of distribution.

Take the house price example. In Madrid like in any other major city there are a wide range of properties and prices but there are a small number


The data come from the web site [Salary Sport](https://salarysport.com/football/la-liga/levante/) and to the best of my knowledge (which is admittedly limited) are, at least indicative of the actual salaries.

    Mean weekly wage with Messi 49051.724137931036
    Mean weekly wage without Messi 15089.285714285714
    3.250765149969394
    

https://gist.github.com/alanjones2/4d570fc1c9835d4732c1d64bbaaca547

    Median weekly wage with Messi 15000.0
    Median weekly wage without Messi 14500.0
    1.0344827586206897
    
