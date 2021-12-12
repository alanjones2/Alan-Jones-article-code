# SQL, Pandas or Both
## Pandas is great for analysing and plotting data but should you store your data in a database and and select it with SQL. Let's take a look at some common operations using Pandas and SQL and see how they compare



I do not claim to be an SQL expert. In fact it's one of the two things that that I have tried to avoid for most of my professional life (the other one is Visual Basic). But there are those who scoff at the idea of using R or Python for data analysis because... well, that's what SQL was designed for.

Well, certainly SQL has been around for a while - 50 years or so - and is still very much in use today in the database world in popular products like SQLite, MySQL, MariaDB and Postgresql, despite the emergence of no-SQL databases such as MongoDB.

So, which should you use, Python and Pandas, or SQL?

I'm going to go through some common tasks to do a little analysis on some UK election data and I'm going to use both; that way you can decide for yourself which approach you think is better.

We'll use data from the UK 2019 General Election, so while we compare SQL and Pandas, we can learn a little bit about how democracy works in Britain, too.

There are two files, a CSV file (to be used by Pandas) and a SQLite database - both contain exactly the same data. The data are a matter of public record and were derived from election results held by the House of Commons Library. This data may be used freely under the Open Parliament Licence 3.0 and my version of it is freely downloadable from my Github repo.

My interest here is to see just how representative the UK Parliament is. Given that the current Conservative goverment recieved much less than 50% of the popular vote, how come they have such a large majority in the House of Commons?

Actually, anyone who is familiar with Britains _first past the post_ voting system already knows the answer but let's make it clear and do the analysis anyway.

