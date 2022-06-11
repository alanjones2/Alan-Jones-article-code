# How to Scrape and Clean Wikipedia Tables with Python and Pandas

## Wikipedia tables are designed for people to look at not for processing but with some help from Python and Pandas we can sort them out. We use the results of the 2021 Formula 1 season as an example.

![](https://github.com/alanjones2/Alan-Jones-article-code/raw/master/Wikitable/images/Rosberg_Hamilton_-_2016_Monaco_GP_2.jpg)

_The Mercedes F1 team in the 2016 Monaco GP. Image by [Andrew Walks](https://flickr.com/photos/97811441@N07/26772038553), CC-BY-2.0._

Wikipedia is a fantastic resource but doesn't particularily lend itself to use by data analysts. The data in the articles is designed to be looked at by people not processed by a computer and so it doesn't necessarily provide an immediately usable resource. But Python and Pandas give us the tools to both scrape and clean the Wikipedia data.

In a Wikipedia table there is often more than one piece of data in a single column. For example, in the Formula 1 data that we are going to look at, there is one column that contains the position in which a driver finishes a race. Great.

The problem is that the data is appended with codes that indicate whether the driver started on pole position, whether they drove the fastest lap, if they retired and other possible outcomes. This is not something that is directly usable.

But Pandas comes to the rescue by first of all allowing us to scrape the data from Wikipedia tables and second to clean up that data so that we can process it effectively.

As an example we are going to look at the results for the 2021 Formula 1 season and see how the data can be extracted from the Wikipedia page and then manipulated so that it can be processed and visualised nicely.

Here is what the table looks like:

![](https://github.com/alanjones2/Alan-Jones-article-code/raw/master/Wikitable/images/driverstablescreenshot.png)
_The results of the 2021 Formula 1 season, source Wikipedia, CC BY-SA 3.0

It's fairly clear, the races have nice little flags by them so we can see where they were and the drivers too have their nationality indicated.

The final position of each driver is indicated for each race and each cell is color coded depending on the pariticular outcome for that driver and along with the colour coding a symbol may be added to the finishing position. So, for example, in the Italian grand prix, Lewis Hamilton came second (indicated by the silver color and the number 2 in the cell) but the cell also contains a 'P' and an 'F' to indicte that he started in pole position and also drove the fastest lap.

It all make sense to the reader but will be confusing when analysing it programatically.

To download the table we use the Pandas ``read_html`` function. I've covered this in a previous article [How to Use Wikipedia as a Data Source](https://towardsdatascience.com/how-to-use-wikipedia-as-a-data-source-3dfea29e6539) and so won't dwell on it too much here.

Suffice it to say that the function returns a list of all the tables from a web page. As there may be a lot of tables on any given web page, we can add a parameter that filters what is returned. So the code below returns all the tables from the web page ``url`` that have the string ``"Driver"`` as one of the column names,

````Python
url="https://en.wikipedia.org/wiki/2021_Formula_One_World_Championship"
df = pd.read_html(url,match="Driver")
````

Ìt is then up to us to find the table that we need in the returned list.

There are only a few tables on this particular Wikipedia web page and the one that I am looking for here is last in the returned list, i.e. ``df[2]``.

![](https://github.com/alanjones2/Alan-Jones-article-code/raw/master/Wikitable/images/driverstablepandas.png)

Now we have something that we can deal with in Pandas but it needs a little processing first.

The first thing to notice is that the last two rows are redundant and that is easily sorted.

````Python
df2 = df[2][:-2]
````
That code creates a new dataframe ``df2`` from the downloaded one but misses of the last two rows.

Our next task is to change the ``Points`` column to be numeric (it was treated as a string because of the column name in the second to last row).

````Python
df2.Points = pd.to_numeric(df2.Points)
````

Now we are able to do something with this data. The following line of code draws a bar graph of teh number of points gained by each driver.

````Python
df2.plot.bar(x='Driver', y='Points')
````

![](https://github.com/alanjones2/Alan-Jones-article-code/raw/master/Wikitable/images/pointschart.png)
