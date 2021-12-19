# SQL, Pandas or Both
## Pandas is great for analysing and plotting data but should you store your data in a database and and select it with SQL. Let's take a look at some common operations using Pandas and SQL and see how they compare

![The elections table](https://github.com/alanjones2/Alan-Jones-article-code/raw/master/sqlpandas/images/20211215_123011.jpg)

I'm not an SQL expert. In fact, to be perfectly honest, it's one of the two things that that I have tried to avoid for most of my professional life (the other one is Visual Basic). But there are those who scoff at the idea of using R or Python for data analysis because... well, that's what SQL was designed for.

Certainly SQL has been around for a while - 50 years or so - and is still the de facto query language in the relational database world. Popular products like SQLite, MySQL, MariaDB and Postgresql, are all SQL based, as are the high end enterprise systems, Oracle and Microsoft SQL Server.

So, if you are a Pythonista doing data analysis, which should you use, Pandas or SQL?

I wanted to do a little analysis on some UK election data which required me to do a number of fairly common and straightforward analysis tasks. Initially, I wanted to work out how it is that the UK government has a large majority in Parliament and yet only secured a relatively small percentage of the popular vote.

 I decided to use both Pandas and SQL to see which I was happier with. I'll describe what I did and how and you can decide for yourself which approach you think is better (or, indeed, how they could be improved).

To do the analysis we'll use data from the UK 2019 General Election (the last one), and while we compare SQL and Pandas, we can learn a little bit about how democracy works in Britain, too.

There are two files, a CSV file (to be used by Pandas) and a SQLite database - both contain exactly the same data. The data are a matter of public record and were derived from election results held by the House of Commons Library. This data may be used freely under the Open Parliament Licence 3.0 and my abridged version of it is freely downloadable from my Github repo.

My interest here is to see just how representative the UK Parliament is. Given that the current Conservative goverment recieved much less than 50% of the popular vote, how come they have a majority of around 80 in the House of Commons?

Actually, anyone who is familiar with Britains _first past the post_ voting system already knows the answer but let's make it clear and do the analysis anyway.

### The raw data
As I said there are two identical data sets, one an SQLite database and the other a CSV file. I've anonymised the data to a certain extent in that I have removed the names of the MPs who were elected and the names of the contituencies that they represent - this is not about personalities or areas of the country but just about how the numbers add up.

The tables have the following columns:

- ons_id: the identifier for the constituency
- result: The party that won and whether it was a new win or a 'hold'
- first_party: the party that won
- second_party: the party that came second
- electorate: the number of voters
- valid_votes: the number of valid votes 
- invalid_votes: the number of invalid votes
- majority: the difference in votes between the winner and the runner-up
- con, lab, ld, ,brexit, green, snp, pc, dup, sf, sdlp, uup, alliance, other: the various parties and their share of the votes

To load the data we use the following code. For the CSV file:


    import pandas as pd

    # create df
    election_df = pd.read_csv('elections.csv')

and for the database:


    import sqlite3 as sql

    # create db
    conn = sql.connect('elections.db')

This gives us the two forms of the data set.

And if we do this

    election_df.head(4)

we get to see what it looks like. Here is a partial view:

![The elections table](https://github.com/alanjones2/Alan-Jones-article-code/raw/master/sqlpandas/images/elections_head.png)

The first thing that we want to do in order to start our analysis is to identify the names all of the individual parties that have won a seat in the House of Commons. We start by getting a list of all the winners from the column _first_party_.

Using Pandas we simply do this:

    election_df['first_party']

We can assign that expression to a variable and we have a list of all the winners. How about SQL?

    query = """
        SELECT first_party 
        FROM elections
    """
    cur = conn.execute(query)
    rows = cur.fetchall()

The list is now in ```rows```. Not quite as concise as Pandas.

But we want the unique values from this list of winners and in Pandas this is straightforward:

    partiesdf = election_df['first_party'].unique()

We just use the ```unique()``` method to 