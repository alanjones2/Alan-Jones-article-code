# SQL, Pandas or Both
## Pandas is great for analysing and plotting data but should you store your data in a database and and select it with SQL. Let's take a look at some common operations using Pandas and SQL and see how they compare



I am not a an SQL expert. In fact it's something that I have generally avoided for a long time. But there are those who scoff at the idea of using R or Python for data analysis because that's what SQL was designed for.

Well, certainly SQL has been around for a while - 50 years or so - and is still very much in use today in the database world in popular products like SQLite, MySQL, MariaDB and Postgresql, despite the emergence of no-SQL databases such as MongoDB.

So, which should you use, Python and Pandas or SQL?

I'm going to go through some common tasks using both and you can decide for yourself which approach is better.

We'll use data from the UK 2019 General Election, so while we compare SQL and Pandas, we can learn a little bit about how democracy works in Britain, too.

There are two files, a CSV file (to be used by Pandas) and a SQLite database - both contain exactly the same data. The data are a matter of public record and were derived from election results held by the House of Commons Library. This data may be used freely under the Open Parliament Licence 3.0 and my version of it is freely downloadable from my Github repo.



