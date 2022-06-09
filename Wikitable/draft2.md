# How to Scrape Wikipedia Tables with Pandas

## Wikipedia tables are designed for people to look at not for processing but with some help from Pandas we can sort them out

Wikipedia is a fantastic resource but doesn't particularily lend itself to use by programmers. The data in the articles is designed to be looked at not processed and so doesn't necessarily provide a tidy data resource.

In a Wikipedia table there is often more than one piece of data in a single column. For example, in the Forlmula 1 data that we are going to look at, a one column contains the position in which a driver finishes a race. Great.

The problem is that the data is appended with codes that indicate whether the driver started on pole position, whether they drove the fastest lap, if they retired and other possible outcomes.

But Pandas comes to the rescue by first of all allowing us to scrape the data from Wikipedia tables and second to clean up that data so that we can process it effectively.

As an example we are going to look at the results for the 2021 Formula 1 season and see how the data can be extracted from the Wikipedia page and then manipulated so that it can be processed and visualised properly.

Here is what the table looks like:

